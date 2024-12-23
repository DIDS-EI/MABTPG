from __future__ import annotations
import gymnasium as gym
from mabtpg.envs.gridenv.base.magrid_env import MAGridEnv
from mabtpg.envs.gridenv.base.magrid import MAGrid

from minigrid.core.world_object import Goal,Lava,Ball,Key,Door
from gymnasium.envs.registration import register

from minigrid.core.mission import MissionSpace


class EmptyEnv(MAGridEnv):
    def __init__(
        self,
        size,
        num_agent,
        agents_start_pos,
        agents_start_dir,
        **kwargs,
    ):
        self.agents_start_pos = agents_start_pos
        self.agents_start_dir = agents_start_dir

        super().__init__(
            num_agent=num_agent,
            grid_size=size,
            **kwargs,
        )

    @staticmethod
    def _gen_mission():
        return "get to the green goal square"


    def _gen_grid(self, width, height):
        self.grid = MAGrid(width, height)

        # 创建墙壁
        self.grid.wall_rect(0, 0, width, height)
        self.grid.horz_wall(3, 3, 10)
        self.grid.vert_wall(5, 3, 10)

        # 生成物体
        self.add_object(Goal(), width - 2, height - 2)
        self.add_object(Lava(), 2, 8)
        self.add_object(Ball("purple"), 6, 8)
        self.add_object(Key("yellow"), 10, 8)
        self.add_object(Door("yellow"), 14, 8)


        # 生成智能体
        if self.agents_start_pos is not None:
            for i in range(self.num_agent):
                self.agents[i].position = self.agents_start_pos[i]
                self.agents[i].direction = self.agents_start_dir[i]
        else:
            self.place_agent()


#注册该环境
register(
    id="MABTPG-Empty-16x16-v0",
    entry_point=__name__ + ":EmptyEnv",
    kwargs={"size": 16},
)


#主要场景参数
num_agent = 3
agents_start_pos = ((1, 1), (2, 1), (6, 6))
agents_start_dir = (0, 1, 2)


#其他场景参数
env_id = "MABTPG-Empty-16x16-v0"
tile_size = 32
agent_view_size =7
screen_size = 640

env = gym.make(
    env_id,
    num_agent=num_agent,
    agents_start_pos=agents_start_pos,
    agents_start_dir=agents_start_dir,

    tile_size=tile_size,
    render_mode="human",
    agent_view_size=agent_view_size,
    screen_size=screen_size
)


# BT规划算法，这里就直接加载随机行为树
from mabtpg import BehaviorTree, BehaviorLibrary

behavior_lib_path = f"../mabtpg/envs/gridenv/minigrid/behavior_lib"
behavior_lib = BehaviorLibrary(behavior_lib_path)
print(behavior_lib)

# 绑定行为树
for agent in env.agents:
    bt = BehaviorTree("random.btml", behavior_lib)
    agent.bind_bt(bt)



# 运行环境
env.reset(seed=0)
env.render()
while True:
    env.step(None)

