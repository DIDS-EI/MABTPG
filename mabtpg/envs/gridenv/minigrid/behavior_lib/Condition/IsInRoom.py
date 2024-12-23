from mabtpg.behavior_tree.base_nodes import Condition
from mabtpg.behavior_tree import Status

import numpy as np
from minigrid.core.constants import DIR_TO_VEC


# is agent near and facing to the target object
class IsInRoom(Condition):
    num_args = 2

    def __init__(self,*args):
        super().__init__(*args)

        # first arg may agent or obj
        self.target_agent = None
        self.target_obj = None

        self.room_id = int(''.join(filter(str.isdigit, args[1]))) # get room id
        self.room_index_ls = []




    def update(self) -> Status:

        is_in_predict, is_true = self.check_if_in_predict_condition()
        if is_in_predict:
            if is_true:
                return Status.SUCCESS
            else:
                return Status.FAILURE

        self.room_index_ls = []

        if "agent" in self.args[0]:
            if self.target_agent is None:
                agent_id = int(self.args[0].split("-")[-1])
                self.target_agent = self.env.agents[agent_id]

            self.room_index_ls = [self.env.get_room_index(self.target_agent.position)]

            # If the agent is at the door's position, it belongs to both connected rooms
            cell = self.env.grid.get(self.target_agent.position[0], self.target_agent.position[1])
            if cell is not None and cell.type == "door":
                self.room_index_ls.extend(list(self.env.doors_to_adj_rooms[cell.id]))
        else:
            self.target_obj = self.env.id2obj[self.args[0]]
            self.room_index_ls = [self.env.get_room_index(self.target_obj.cur_pos)]


        if self.room_id in self.room_index_ls:
            # print("IsInRoom", self.target_agent,self.target_obj,self.room_index_ls)
            return Status.SUCCESS
        else:
            return Status.FAILURE
