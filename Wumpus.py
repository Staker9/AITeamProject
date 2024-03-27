import Agent
from Sensor import add_breeze, add_glitter, add_stench
import numpy as np


class GridWorld:

    def __init__(self):
        self.grid_size = 6
        self.grid = [[[] for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def setup_grid(self):
        # 테두리를 Wall로 설정
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if i == 0 or i == self.grid_size - 1 or j == 0 or j == self.grid_size - 1:
                    self.grid[i][j].append('Wall')

        # 1,1은 Safe로, 4,4는 Gold로 설정
        self.grid[1][1].append('Safe')
        self.grid[4][4].append('Gold')
        add_glitter(self.grid, 4 - 1, 4)
        add_glitter(self.grid, 4, 4 - 1)

        # 나머지 위치에 대한 설정
        for i in range(1, self.grid_size - 1):
            for j in range(1, self.grid_size - 1):
                if (i, j) not in [(1, 1), (4, 4)]:
                    if np.random.rand() < 0.1:
                        self.grid[i][j].append('Pit')
                        add_breeze(self.grid, i, j, self.grid_size)
                    elif np.random.rand() < 0.1:
                        self.grid[i][j].append('Wumpus')
                        add_stench(self.grid, i, j, self.grid_size)

    def print_grid(self, agent_x=None, agent_y=None):
        cell_width = 14
        horizontal_line = "-" * (self.grid_size * (cell_width + 1) + 1)

        for i, row in enumerate(self.grid):
            print(horizontal_line)
            for j, cell in enumerate(row):
                if agent_x == i and agent_y == j:
                    cell_content = 'Agent'.center(cell_width)
                elif not cell:
                    cell_content = 'None'.center(cell_width)
                else:
                    cell_content = ','.join(cell).center(cell_width)
                print("|" + cell_content, end="")
            print("|")
        print(horizontal_line)


world = GridWorld()
world.setup_grid()
#world.print_grid()
