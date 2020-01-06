import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
from random import randint


class Game2048(gym.Env):

    def __init__(self):
        self.reset()
        self.UP = 0
        self.LEFT = 1
        self.RIGHT = 2
        self.DOWN = 3

    def step(self, action):
        if action == self.UP:
            reward = self._move_up()
        elif action == self.LEFT:
            reward = self._move_left()
        elif action == self.RIGHT:
            reward = self._move_right()
        elif action == self.DOWN:
            reward = self._move_down()
        self.done = not self._add_random_block()
        return self._render(), reward, self.done, None

    def reset(self):
        self.grid = np.zeros((4, 4))
        self.done = False
        self._add_random_block()
        return self._render()

    def _render(self, mode='human'):
        return np.copy(self.grid)

    def render(self, mode='human'):
        new_grid = np.copy(self.grid)
        for i in range(4):
            for j in range(4):
                if new_grid[i, j] != 0:
                    new_grid[i, j] = 2 ** (new_grid[i, j])
        return new_grid

    def _add_random_block(self):
        empty_cells = self._empty_cell()
        if len(empty_cells) == 0:
            return False
        else:
            x, y = empty_cells[randint(0, len(empty_cells) - 1)]
            value = randint(1, 2)
            self.grid[x, y] = value
            return True

    def _empty_cell(self):
        empty_cells = []
        for i in range(4):
            for j in range(4):
                if self.grid[i, j] == 0:
                    empty_cells.append((i, j))
        return empty_cells

    def _move_up(self):
        reward = 0
        for j in range(4):
            for i in range(4):
                if self.grid[i, j] == 0:
                    for k in range(i + 1, 4):
                        if self.grid[k, j] > 0:
                            self.grid[i, j] = self.grid[k, j]
                            self.grid[k, j] = 0
                            break
        for j in range(4):
            for i in range(4):
                k = i
                while k < 3 and self.grid[k + 1, j] == self.grid[i, j]:
                    k += 1
                if k > i and self.grid[i, j] > 0:
                    reward += 2 ** self.grid[i,j]
                    self.grid[i, j] += 1
                    self.grid[k, j] = 0
        for j in range(4):
            for i in range(4):
                if self.grid[i, j] == 0:
                    for k in range(i + 1, 4):
                        if self.grid[k, j] > 0:
                            self.grid[i, j] = self.grid[k, j]
                            self.grid[k, j] = 0
                            break
        return reward

    def _move_left(self):
        reward = 0
        for i in range(4):
            for j in range(4):
                if self.grid[i, j] == 0:
                    for k in range(j + 1, 4):
                        if self.grid[i, k] > 0:
                            self.grid[i, j] = self.grid[i, k]
                            self.grid[i, k] = 0
                            break
        for i in range(4):
            for j in range(4):
                k = j
                while k < 3 and self.grid[i, k + 1] == self.grid[i, j]:
                    k += 1
                if k > j and self.grid[i, j] > 0:
                    reward += 2 ** self.grid[i,j]
                    self.grid[i, j] += 1
                    self.grid[i, k] = 0
        for i in range(4):
            for j in range(4):
                if self.grid[i, j] == 0:
                    for k in range(j + 1, 4):
                        if self.grid[i, k] > 0:
                            self.grid[i, j] = self.grid[i, k]
                            self.grid[i, k] = 0
                            break
        return reward

    def _move_right(self):
        reward = 0
        for i in range(4):
            for j in reversed(range(4)):
                if self.grid[i, j] == 0:
                    for k in reversed(range(j)):
                        if self.grid[i, k] > 0:
                            self.grid[i, j] = self.grid[i, k]
                            self.grid[i, k] = 0
                            break
        for i in range(4):
            for j in reversed(range(4)):
                k = j
                while k > 0 and self.grid[i, k - 1] == self.grid[i, j]:
                    k -= 1
                if k < j and self.grid[i, j] > 0:
                    reward += 2 ** self.grid[i,j]
                    self.grid[i, j] += 1
                    self.grid[i, k] = 0
        for i in range(4):
            for j in reversed(range(4)):
                if self.grid[i, j] == 0:
                    for k in reversed(range(j)):
                        if self.grid[i, k] > 0:
                            self.grid[i, j] = self.grid[i, k]
                            self.grid[i, k] = 0
                            break
        return reward

    def _move_down(self):
        reward = 0
        for j in range(4):
            for i in reversed(range(4)):
                if self.grid[i, j] == 0:
                    for k in reversed(range(i)):
                        if self.grid[k, j] > 0:
                            self.grid[i, j] = self.grid[k, j]
                            self.grid[k, j] = 0
                            break
        for j in range(4):
            for i in reversed(range(4)):
                k = i
                while k > 0 and self.grid[k - 1, j] == self.grid[i, j]:
                    k -= 1
                if k < i and self.grid[i, j] > 0:
                    reward += 2 ** self.grid[i, j]
                    self.grid[i, j] += 1
                    self.grid[k, j] = 0
        for j in range(4):
            for i in reversed(range(4)):
                if self.grid[i, j] == 0:
                    for k in reversed(range(i)):
                        if self.grid[k, j] > 0:
                            self.grid[i, j] = self.grid[k, j]
                            self.grid[k, j] = 0
                            break
        return reward


if __name__ == "__main__":
    env = Game2048()
    done = False
    print(env.render())
    while not done:
        move = input('Next Move?\n')
        if move == 'up':
            move = env.UP
        elif move == 'left':
            move = env.LEFT
        elif move == 'right':
            move = env.RIGHT
        elif move == 'down':
            move = env.DOWN
        _, reward, done, _ = env.step(move)
        print('reward: ', reward)
        print(env.render())
