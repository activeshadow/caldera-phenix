import logging

from aiohttp        import web
from aiohttp_jinja2 import template


class PhenixService:
    def __init__(self, services, name, description):
        self.services    = services
        self.name        = name
        self.description = description

        self.data_svc = services.get('data_svc')
        self.log      = logging.getLogger('phenix_svc')


    @template('phenix.html')
    async def splash(self, request):
        data = await self._get_plugin_data()
        return data


    async def plugin_data(self, request):
        data = await self._get_plugin_data()
        return web.json_response(data)


    async def _get_plugin_data(self):
        planners = {
            p.planner_id: {
                "name"        : p.name,
                "description" : p.description.replace('\n', '<br>')
            }
            for p in await self.data_svc.locate('planners')
            if await p.which_plugin() == 'phenix'
        }

        planners = list(planners.values())
        return dict(name=self.name, description=self.description, planners=planners)
