import orm
import sys,asyncio
from Models import User,Blog,Comment
async def test(loop):
    await orm.create_pool(loop=loop,user='www-data',password='www-data',db='awesome')
    u=User(name='Test',email='test@123.com',passwd='123456',image='about:blank')
    await u.save()

if __name__=='__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([test(loop)]))
    loop.close()
    if loop.is_closed():
        sys.exit(0)
