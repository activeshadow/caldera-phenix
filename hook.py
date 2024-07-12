from app.utility.base_world import BaseWorld

from plugins.phenix.app.phenix_gui import PhenixGUI
from plugins.phenix.app.phenix_api import PhenixAPI

name = 'phenix'
description = 'The phenix plugin for Caldera provides custom planners useful to the phenix orchestration tool.'
address = '/plugin/phenix/gui'
access = BaseWorld.Access.RED


async def enable(services):
    app        = services.get('app_svc').application
    phenix_gui = PhenixGUI(services, name=name, description=description)
    phenix_api = PhenixAPI(services)

    app.router.add_static('/phenix', 'plugins/phenix/static/', append_version=True)
    app.router.add_route('GET', '/plugin/phenix/gui', phenix_gui.splash)

    # Add API routes here
    app.router.add_route('POST', '/plugin/phenix/mirror', phenix_api.mirror)

