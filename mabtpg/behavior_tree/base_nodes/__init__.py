from mabtpg.behavior_tree.base_nodes.Action import Action
from mabtpg.behavior_tree.base_nodes.Condition import Condition
from mabtpg.behavior_tree.base_nodes.Inverter import Inverter
from mabtpg.behavior_tree.base_nodes.Selector import Selector
from mabtpg.behavior_tree.base_nodes.Sequence import Sequence


base_node_map = {
    "act": Action,
    "cond": Condition,
}

base_node_type_map={
    "act": "Action",
    "cond": "Condition",
}

composite_node_map = {
    "not": Inverter,
    "selector": Selector,
    "sequence": Sequence
}