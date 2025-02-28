from app.utility.base_world import BaseWorld

from plugins.phenix.app.phenix_svc import PhenixService

name = 'phenix'
description = 'The phenix plugin for Caldera provides custom planners useful to the phenix orchestration tool.'
address = '/plugin/phenix/gui'
access = BaseWorld.Access.RED


async def enable(services):
    phenix_svc = PhenixService(services, name, description)
    app        = services.get('app_svc').application

    app.router.add_route('GET', '/plugin/phenix/gui',  phenix_svc.splash)
    app.router.add_route('GET', '/plugin/phenix/data', phenix_svc.plugin_data)
