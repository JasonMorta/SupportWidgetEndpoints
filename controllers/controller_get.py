from aiohttp import web, ClientSession
from collections import defaultdict
import aiohttp
import urllib.parse

# Fetch tickets from Freshdesk API
async def fetch_tickets(session, page, dateStamp):
    url = f"https://newaccount1627234890025.freshdesk.com/api/v2/tickets?updated_since={dateStamp}T00:00:00Z&order_by=created_at&order_type=asc&per_page=100&page={page}"
    print('url = ', url)

    bearer_token = "WXJJclVqVFhxS0VOU3pvNXJkSGc="

    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    try:
        print(f"Fetching page {page}...")
        async with session.get(url, headers=headers) as response:
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
            
            if response.status == 401:
                print("Authentication failed: Invalid credentials.")
                return None
            
            if response.status == 400:
                print(f"Bad Request: Invalid date format. response: {response}")
                return None
            
            return await response.json()
    
    except aiohttp.ClientResponseError as http_err:
        print(f"HTTP error occurred: {http_err}, response: {response}")
        return None
    except aiohttp.ClientError as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    
    return []  # Return an empty list in case of error

# Fetch agents from Freshdesk API
async def fetch_agents(session):
    url = "https://newaccount1627234890025.freshdesk.com/api/v2/agents?per_page=100"
    bearer_token = "WXJJclVqVFhxS0VOU3pvNXJkSGc="

    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    try:
        print(f"Fetching agents...")
        async with session.get(url, headers=headers) as response:
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
            
            if response.status == 401:
                print("Authentication failed: Invalid credentials.")
                return None
            agents = await response.json()
            print(f"{len(agents)} agents fetched.")
            return agents
    
    except aiohttp.ClientResponseError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except aiohttp.ClientError as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    
    return []  # Return an empty list in case of error

async def fetch_all_tickets(session, dateStamp):
    print(f"🏳️ Fetching all tickets since: {dateStamp}...")
    page = 1
    all_tickets = []
    error_details = None

    while True:
        try:
            tickets = await fetch_tickets(session, page, dateStamp)

            if tickets is None:  # Authentication failed
                return [], "Authentication failure or no tickets."

            if len(tickets) < 100:  # Stop if the response length is less than 100
                all_tickets.extend(tickets)
                print(f"Fetched all tickets up to page {page}. Total tickets: {len(all_tickets)}")
                break

            all_tickets.extend(tickets)
            print(f"Page {page} fetched. Total tickets so far: {len(all_tickets)}")
            page += 1  # Move to the next page

        except Exception as err:
            print(f"An error occurred while fetching tickets: {err}")
            error_details = str(err)
            break

    return all_tickets, error_details


async def get_req(request):
    dateStamp = request.headers.get('date_req')
    print(f"🔞 DATE: {dateStamp}")

    async with ClientSession() as session:
        # Fetch tickets
        all_tickets, ticket_error = await fetch_all_tickets(session, dateStamp)

        # If there was an error fetching tickets, return the error response
        if not all_tickets:
            error_message = f"Failed to fetch tickets. Date: {dateStamp}. Error: {ticket_error or 'No tickets found.'}"
            return web.Response(text=error_message, status=500)

        # Fetch agents only if fetching tickets was successful
        agents = await fetch_agents(session)

        # If fetching agents failed, return an error response
        if not agents:
            return web.Response(text="Failed to fetch agents.", status=500)

    # Continue processing only if both tickets and agents were successfully fetched
    responder_ticket_map = defaultdict(list)

    # Group tickets by agent ID
    for ticket in all_tickets:
        if isinstance(ticket, dict):  # Ensure the ticket is a dictionary
            if ticket.get("status") in [4, 5] and ticket.get("responder_id") is not None and ticket.get("updated_at") >= dateStamp:
                responder_id = ticket["responder_id"]
                responder_ticket_map[responder_id].append(ticket)
        else:
            print(f"Unexpected ticket format: {ticket}")

    agent_map = {agent["id"]: agent["contact"]["name"] for agent in agents}

    result = [
        {
            "responder_id": responder_id,
            "name": agent_map.get(responder_id, "Unknown"),
            "tickets_completed": len(tickets),  # Count the number of completed tickets
            "ticket_items": tickets  # List of all tickets for this agent
        }
        for responder_id, tickets in responder_ticket_map.items()
    ]
    
    return web.json_response(result)
