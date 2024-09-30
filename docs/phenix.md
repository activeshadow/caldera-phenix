# phenix Plugin

The `phenix` plugin provides a specialized operations planner (aptly called
`phenix`) that will only execute abilities once per agent, even if the ability
is repeatable.

In addition, the planner will only operate on agents whose host names match a
`<unique>.planner.phenix.agent` fact trait value (unless no facts with that
trait name exist).
