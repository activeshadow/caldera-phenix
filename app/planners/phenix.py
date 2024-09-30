import logging


class LogicalPlanner:
    def __init__(self, operation, planning_svc, stopping_conditions=()):
        self.operation    = operation
        self.planning_svc = planning_svc

        self.stopping_conditions    = stopping_conditions
        self.stopping_condition_met = False

        self.log = logging.getLogger("phenix_planner")

    async def execute(self):
        facts  = await self.operation.all_facts()
        agents = [] # list of hostnames running an agent

        # Default to operating with all agents.
        operators = self.operation.agents

        for fact in facts:
            if fact.trait.endswith('.planner.phenix.agent'):
                agents.append(fact.value) # fact value is expected to be a hostname

        # If specific agents were provided as fact traits, limit to operating
        # with only the agents specified, as long as they've registered with
        # the operation.
        if agents:
            operators = []

            # There are more efficient ways of detecting list intersection, but
            # this approach maintains agent ordering as specified via fact
            # traits.
            for host in agents: # `agents` is a list of hostnames
                found = False

                for agent in self.operation.agents:
                    if agent.host == host:
                        operators.append(agent)
                        found = True
                        break

                if not found:
                    self.log.warning(f'agent {host} not found')

        for agent in operators:
            self.log.info(f'Starting to operate with {agent.host} agent...')

            links = await self.planning_svc.get_links(operation=self.operation, agent=agent)
            ids   = [await self.operation.apply(link) for link in links]

            # Wait for each agent's links to complete before operating with the
            # next agent. This could become another planner option we could
            # define via a fact trait, if we want to operate with all agents in
            # parallel.
            await self.operation.wait_for_links_completion(ids)

            self.log.info(f'Done operating with {agent.host} agent.')
