import py_trees as ptree
from mabtpg.behavior_tree.base_nodes.BehaviorNode import BahaviorNode, Status

class Condition(BahaviorNode):
    print_name_prefix = "condition "
    type = 'Condition'

    def __init__(self,*args):
        super().__init__(*args)

