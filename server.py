
from aiohttp import web
from app_setup import create_app

app = web.Application()
app = create_app()

web.run_app(app, host='0.0.0.0', port=3001)