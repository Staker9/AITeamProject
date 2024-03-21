# 주어진 코드와 같은 파일 내에 이 코드를 추가하거나 별도의 파일로 분리할 수 있습니다.
# Sensor.py 모듈을 임포트합니다.
from Sensor import add_breeze, add_glitter, add_stench
import numpy as np


class GridWorld:

    def __init__(self):
        self.grid_size = 4
        self.grid = [[[] for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def setup_grid(self):
        self.grid[0][0].append('Safe')

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if (i, j) != (0, 0) and (i, j) != (3, 3):
                    if np.random.rand() < 0.1:
                        self.grid[i][j].append('Pit')
                        add_breeze(self.grid, i, j, self.grid_size)
                    if np.random.rand() < 0.1:
                        self.grid[i][j].append('Wumpus')
                        add_stench(self.grid, i, j, self.grid_size)

        # 금 위치 설정 및 Glitter 추가
        gold_x, gold_y = (3, 3)
        self.grid[gold_x][gold_y].append('Gold')
        add_glitter(self.grid, gold_x - 1, gold_y)
        add_glitter(self.grid, gold_x, gold_y - 1)

    def print_grid(self):
        cell_width = 14
        horizontal_line = "-" * 61

        for row in self.grid:
            print(horizontal_line)
            for cell in row:
                if not cell:
                    cell_content = 'None'.center(cell_width)
                else:
                    cell_content = ','.join(cell).center(cell_width)
                print("|" + cell_content, end="")
            print("|")
        print(horizontal_line)


world = GridWorld()
world.setup_grid()
world.print_grid()