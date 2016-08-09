#!/usr/bin/env python
#-*-coding:utf-8-*-
import logging;
logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>')

async def init(loop):
    #create an Application
    app=web.Application(loop=loop)
    #add router
    app.router.add_route('GET','/',index)
    #await srv
    srv=await loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('Server start...')
    return srv

loop=asyncio.get_event_loop()

loop.run_until_complete(init(loop))

loop.run_forever()
'''
def init():
    app=web.Application()
    app.router.add_route('GET','/',index)
    return web.run_app(app)
init()
'''
