A simple python sever, thats uses aiohttp.

- Files are mobilized, and the server is run from the server.py file.
- Container controller with simle logic to handle the requests.
- Routes have all HTTP request methods, and are handled by the controllers.
- Middleware are place on all routes, and are used to log the requests going through the server and checks for an API key in the headers of each request.


### Installation
- Install aiohttp and cors
```sh
pip install aiohttp aiohttp-cors aiohttp_middlewares watchdog

```

- Start the server normally
```sh   
python server.py
```

- Start the sever with auto restart when changes are made to the files
```sh
watchmedo auto-restart --patterns="*.py" --recursive -- python server.py
```

API_KEY = 'YrIrUjTXqKENSzo5rdHg' 

# Freshdesk
BearerToken = WXJJclVqVFhxS0VOU3pvNXJkSGc= 

#Freshchat
Bearer_token = 

eyJraWQiOiJjdXN0b20tb2F1dGgta2V5aWQiLCJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmcmVzaGNoYXQiLCJzdWIiOiIyNWQ0ZDViZS1kNDUyLTRjMTktOTRmZi1kYzI5MTE0NTZjODAiLCJjbGllbnRJZCI6ImZjLTBiMjNkZTZkLTM4YTYtNGJiMi1iMWE3LWJmNzBiODU3YTBmNiIsInNjb3BlIjoiYWdlbnQ6cmVhZCBhZ2VudDpjcmVhdGUgYWdlbnQ6dXBkYXRlIGFnZW50OmRlbGV0ZSBjb252ZXJzYXRpb246Y3JlYXRlIGNvbnZlcnNhdGlvbjpyZWFkIGNvbnZlcnNhdGlvbjp1cGRhdGUgbWVzc2FnZTpjcmVhdGUgbWVzc2FnZTpnZXQgYmlsbGluZzp1cGRhdGUgcmVwb3J0czpmZXRjaCByZXBvcnRzOmV4dHJhY3QgcmVwb3J0czpyZWFkIHJlcG9ydHM6ZXh0cmFjdDpyZWFkIGRhc2hib2FyZDpyZWFkIHVzZXI6cmVhZCB1c2VyOmNyZWF0ZSB1c2VyOnVwZGF0ZSB1c2VyOmRlbGV0ZSBvdXRib3VuZG1lc3NhZ2U6c2VuZCBvdXRib3VuZG1lc3NhZ2U6Z2V0IG1lc3NhZ2luZy1jaGFubmVsczptZXNzYWdlOnNlbmQgbWVzc2FnaW5nLWNoYW5uZWxzOm1lc3NhZ2U6Z2V0IG1lc3NhZ2luZy1jaGFubmVsczp0ZW1wbGF0ZTpjcmVhdGUgbWVzc2FnaW5nLWNoYW5uZWxzOnRlbXBsYXRlOmdldCBmaWx0ZXJpbmJveDpyZWFkIGZpbHRlcmluYm94OmNvdW50OnJlYWQgcm9sZTpyZWFkIGltYWdlOnVwbG9hZCIsImlzcyI6ImZyZXNoY2hhdCIsInR5cCI6IkJlYXJlciIsImV4cCI6MTk0MTUzMjgyNCwiaWF0IjoxNjI2MDAwMDI0LCJqdGkiOiIzYTI5OWE1Ni02NzFhLTRjOTEtYmQyMi1iMWIzM2JkZjE3YzUifQ.BPO3ofWd8eJF6NHGfp_Jf_APVwJonVpJRzIG5JdxOCA

LIST OF TICKETS (Emails) - Requester ID - https://domain.freshdesk.com/api/v2/tickets #see how many tickets agents have responede to 
List of agent (MAP AGENT ID TO USER ) - https://newaccount1627234890025.freshdesk.com/api/v2/agents 

