import logging
from aiohttp import web
import aiohttp

async def get_gists_for_user(user):
    """Make a call to retrieve the public gists for the user {user} """
    url = f"https://api.github.com/users/{user}/gists?per_page=100"
    headers = {
           'Accept': 'application/vnd.github+json',
           'X-GitHub-Api-Version': '2022-11-28'
       }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:

            if response.status == 200:
                return  response.status, await response.json()
            return response.status, {}

if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    routes = web.RouteTableDef()

    @routes.get('/{username}')
    async def get_user_gists(request):
        """Incoming Route /{User"} """
        logger = request.app['logger']
        username = request.match_info['username']

        logger.debug(f"Getting public Gists for {username}")
        status_code, json_response = await get_gists_for_user(username)
        logger.debug(f"Server Returned Status: {status_code}")

        return web.json_response(json_response,status=status_code)

    app = web.Application()
    app['logger'] = logging.getLogger(__name__)
    app.add_routes(routes)
    web.run_app(app)
