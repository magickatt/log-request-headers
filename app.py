from aiohttp.web import Application, Request, Response, run_app
from structlog import get_logger


logger = get_logger()


def parse_headers(raw_headers: tuple):
    return {key.decode('ascii'): value.decode('ascii') for key, value in raw_headers}

async def request_logger(request: Request) -> Response:
    """Log the request headers
    https://docs.aiohttp.org/en/stable/web_reference.html#aiohttp.web.BaseRequest.headers."""
    logger.debug(parse_headers(request.raw_headers))
    return Response(status=200)


app = Application()
app.router.add_route('POST', '/{tail:.*}', request_logger)
app.router.add_route('PUT', '/{tail:.*}', request_logger)
app.router.add_route('DELETE', '/{tail:.*}', request_logger)
app.router.add_route('PATCH', '/{tail:.*}', request_logger)
app.router.add_route('GET', '/{tail:.*}', request_logger)
app.router.add_route('HEAD', '/{tail:.*}', request_logger)
app.router.add_route('CONNECT', '/{tail:.*}', request_logger)
app.router.add_route('OPTIONS', '/{tail:.*}', request_logger)
app.router.add_route('TRACE', '/{tail:.*}', request_logger)


if __name__ == '__main__':
    logger.msg("Starting log request headers...")
    run_app(app)
