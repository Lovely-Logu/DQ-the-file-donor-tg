from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response({"message": "Tr_Movies"})

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)
