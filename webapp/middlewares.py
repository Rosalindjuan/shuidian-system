import base64
import aiohttp_jinja2

from time import time
from aiohttp import web
from aiohttp_session import get_session
from aiohttp_session import session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage

# from .utils import get_userinfo, oauth, redirect, set_session, convert_json
# from store.models import User


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


async def authorize(app, handler):
    async def middleware(request):
        def check_path(path):
            result = False
            if path in request.app.route_path:
                result = True
            return result


        # session = await get_session(request)
        # openid = session.get('openid')
        # request.app.logger.info(openid)
        # if openid:
        #     if await User.check_user(openid):
        #         return await handler(request)
        #     else:
        #         del session['openid']
        #         return redirect(request, 'index')
        # elif check_path(request.path):
        #     # url = request.app.router['login'].url()
        #     # return web.HTTPFound(url)
        #     user_info = await get_userinfo(request)
        #     if isinstance(user_info, web.HTTPFound):
        #         return user_info
        #     await User.create_user(user_info)
        #     if 'unionid' in user_info:
        #         session['openid'] = user_info['unionid']
        #     else:
        #         session['openid'] = user_info['openid']
        #     session['last_visit'] = time()
        #     return await handler(request)
        # else:
        #     return await handler(request)

        return await handler(request)


    return middleware

def setup_middlewares(app):

    # conf = app.config
    #
    # #session middleware
    # secret_key = base64.urlsafe_b64decode(conf['fernet_key'].encode('utf8'))
    # app.middlewares.append(session_middleware(EncryptedCookieStorage(secret_key)))

    error_middleware = error_pages({404: handle_404,
                                    500: handle_500})
    app.middlewares.append(error_middleware)
    #authorize middleware
    # app.middlewares.append(authorize)
    #db middleware
    #app.middlewares.append(db_handler)
    #debugtoolbar middleware
    # if app.config['debugtoolbar_enable']:
    #     from aiohttp_debugtoolbar import toolbar_middleware_factory
    #     app.middlewares.append(toolbar_middleware_factory)
