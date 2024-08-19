# MABTPG

MRBTP: Efficient Multi-Robot Behavior Tree Planning and Collaboration.

![Python Version](images/python310.svg)
![GitHub license](images/license.svg)
![](images/framework.pdf)


## 🛠️ Installation

### Create a conda environment
```shell
conda create --name mabtpg python=3.10
conda activate mabtpg
```

### Install MABTPG.
```shell
cd MABTPG
pip install -e .
```

### 1. Download the VirtualHome executable for your platform (Only Windows is tested now):

| Operating System | Download Link                                                                      |
|:-----------------|:-----------------------------------------------------------------------------------|
| Linux            | [Download](http://virtual-home.org/release/simulator/v2.0/v2.3.0/linux_exec.zip)   |
| MacOS            | [Download](http://virtual-home.org/release/simulator/v2.0/v2.3.0/macos_exec.zip)   |
| Windows          | [Download](http://virtual-home.org/release/simulator/v2.0/v2.3.0/windows_exec.zip) |

### 2. 运行 MiniGrid 和 BabyAI 原有环境:
## 运行 MiniGrid 和 BabyAI 原有环境
1. 在 MiniGrid所有场景.txt 中选择一个想要运行的场景
2. 在 test_gridworld/minigrid_env.py 文件中，输入想要运行的场景和 num_agent，智能体会默认加载随机动作的行为树


## 自定义环境
在 test_gridworld/custom_env.py 文件中，自定义一个房间，用 self.grid.horz_wall, self.put_obj 等函数来创建场景



## 📂 Directory Structure

```
btpg
│
├── agent - Configuration for intelligent agents.
├── algos - Training and decision-making algorithms.
├── bt_planning - Behavior tree planning algorithms.
│   ├── ReactivePlanning 
│   ├── BTExpansion
│   ├── OBTEA
│   └── HOBTEA
├── llm_client - Modules for large language model integration.
│   └── vector_database_env_goal.py - Core vector database functionality.
├── behavior_tree - Behavior tree engine components.
├── envs - Scene environments for agent interaction.
│   ├── base - Foundational elements for environments.
│   ├── gridworld - Grid-based testing environment.
│   ├── RoboWaiter - Café service robot scenario.
│   ├── VirtualHome - Household robot scenario.
│   ├── RobotHow - Testing environment for household robots.
│   └── RobotHow_Small - Smaller version of the household robot testing environment.
└── utils - Supporting functions and utilities.

simulators - Platforms for realistic training environments.

test_exp - Testing modules for behavior trees planning, LLMs, and scene environments.
```

## 🚀 Usage



## 📖 Getting Started