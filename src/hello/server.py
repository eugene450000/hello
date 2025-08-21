import socket
from aiohttp import web


async def handle_name(request):
    # http://0.0.0.0:8080/?name=User
    params = request.rel_url.query
    name = params["name"] if "name" in params else "Anonymous"
    text = f"Hello {name} from my  {socket.gethostname()}!\n"
    return web.Response(text=text, content_type="text/html")


def setup_webserver():
    app = web.Application()
    app.add_routes([
        web.get("/", handle_name),
    ])
    return app


def run_web_app(host="0.0.0.0", port=8080):
    app = setup_webserver()
    web.run_app(app, host=host, port=port)
