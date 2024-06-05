from aiohttp import web
from .route import routes

async def web_server():
    web_app = web.Application(client_max_size=1024**2)  # Example: 1MB client max size
    web_app.add_routes(routes)
    return web_app

if __name__ == '__main__':
    web.run_app(web_server())
  
