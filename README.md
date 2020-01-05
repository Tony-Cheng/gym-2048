# gym-2048
This is an implementation of the game [2048](<https://en.wikipedia.org/wiki/2048_(video_game)>) for the OpenAI Gym environment.
Some game mechanics may be different from that of the original game.

## Installation
Install OpenAi Gym by following the instruction [here](https://github.com/openai/gym).

The 2048 gym environment can be installed by:
```
git clone https://github.com/Tony-Cheng/gym-2048.git
cd gym-2048
pip install -e .
```

## Basics
Create the environment by:
```python
import gym
env = gym.make('gym_2048:2048-v0')
```
