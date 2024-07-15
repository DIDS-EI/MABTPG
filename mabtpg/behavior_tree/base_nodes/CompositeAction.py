from mabtpg.behavior_tree.base_nodes.BehaviorNode import BahaviorNode, Status
from mabtpg.behavior_tree.base_nodes.Action import Action

class CompositeAction(Action):
    print_name_prefix = "action "
    type = 'Action'
    subtree_func = None

    def __init__(self,*args):
        self.subtree = self.subtree_func()
        super().__init__(*args)


    def bind_agent(self,agent):
        self.agent = agent
        self.env = agent.env
        self.subtree.bind_agent(agent)


    def update(self) -> Status:
        self.subtree.tick()
        return self.subtree.root.status
