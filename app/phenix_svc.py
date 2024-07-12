import logging


class PhenixService:
    def __init__(self, services):
        self.services = services
        self.file_svc = services.get('file_svc')

        self.log = logging.getLogger('phenix_svc')

    async def foo(self):
        return 'bar'
