import py_trees as ptree
from typing import Any

class Sequence(ptree.composites.Sequence):
    print_name = "sequence"
    ins_name = "Sequence"
    type = "Sequence"
    is_composite = True

    def __init__(self,memory=False):
        super().__init__(memory = memory,name = "Sequence")

    def bind_agent(self,agent):
        pass