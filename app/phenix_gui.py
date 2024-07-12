import logging

from aiohttp_jinja2 import template

from app.service.auth_svc   import for_all_public_methods, check_authorization
from app.utility.base_world import BaseWorld

from plugins.phenix.app.phenix_svc import PhenixService

@for_all_public_methods(check_authorization)
class PhenixGUI(BaseWorld):
    def __init__(self, services, name, description):
        self.name        = name
        self.description = description
        self.services    = services
        self.modbus_svc  = PhenixService(services)

        self.data_svc = services.get('data_svc')
        self.auth_svc = services.get('auth_svc')

        self.log = logging.getLogger('phenix_gui')

    @template('phenix.html')
    async def splash(self, request):
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
