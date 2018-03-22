import base64
import aiohttp_jinja2

from time import time
from aiohttp import web
from aiohttp_session import get_session,session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage


# from .utils import get_userinfo, oauth, redirect, set_session, convert_json
from store.models import Users


async def handle_404(request, response):
    response = aiohttp_jinja2.render_template('404.html',
                                              request,
                                              {})
    return response


async def handle_500(request, response):
    response = aiohttp_jinja2.render_template('500.html',
                                              request,
                                              {})
    return response


def error_pages(overrides):
    async def middleware(app, handler):
        async def middleware_handler(request):
            try:
                response = await handler(request)
                override = overrides.get(response.status)
                if override is None:
                    return response
                else:
                    return await override(request, response)
            except web.HTTPException as ex:
                override = overrides.get(ex.status)
                if override is None:
                    raise
                else:
                    return await override(request, ex)
        return middleware_handler
    return middleware


async def db_handler(app, handler):
    async def middleware(request):
        if request.path.startswith('/static/') or request.path.startswith('/_debugtoolbar'):
            response = await handler(request)
            return response

        request.db = app.db
        response = await handler(request)
        return response
    return middleware

def setup_middlewares(app):

    conf = app.config
    #
    # #session middleware
    secret_key = base64.urlsafe_b64decode(conf['fernet_key'].encode('utf8'))
    app.middlewares.append(session_middleware(EncryptedCookieStorage(secret_key)))

    error_middleware = error_pages({404: handle_404,
                                    500: handle_500})
    app.middlewares.append(error_middleware)

    #db middleware
    #app.middlewares.append(db_handler)
    #debugtoolbar middleware
    # if app.config['debugtoolbar_enable']:
    #     from aiohttp_debugtoolbar import toolbar_middleware_factory
    #     app.middlewares.append(toolbar_middleware_factory)
