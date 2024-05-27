#0401 시영
#Agent 초록색/ pit 빨간색/ Wumpus 보라색/ Gold 노란색
#움직일때마다 Step 추가
#25 line 'Wall'-> '~' 로 수정

#0402 재현
#44line 왈람쓰 위치저장 추가 ,33line 함수로 수정

#0527 시영
# Agent 화살표 추가

import Agent
from Sensor import add_breeze, add_glitter, add_stench
import numpy as np
from colorama import Fore, Style



class GridWorld:

    def __init__(self):
        self.grid_size = 6
        self.grid = [[[] for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.wumpus_location = None

    def setup_grid(self):
        # 테두리를 Wall로 설정
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if i == 0 or i == self.grid_size - 1 or j == 0 or j == self.grid_size - 1:
                    self.grid[i][j].append('~')

        # 1,1은 Safe로, 4,4는 Gold로 설정
        self.grid[1][1].append('Safe')
        self.grid[4][4].append('Gold')
        add_glitter(self.grid, 4,4, self.grid_size)

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
                        self.wumpus_location = (i, j)  # Wumpus 위치 저장

    def print_grid(self, agent_x=None, agent_y=None, step=None):
        if step is not None:
            print(f"Step: {step}")  # 단계 출력

        cell_width = 14
        horizontal_line = "-" * (self.grid_size * (cell_width + 1) + 1)

        direction_symbols = {
            'UP':'↑',
            'RIGHT':'→',
            'DOWN':'↓',
            'LEFT':'←'
        }

        for i, row in enumerate(self.grid):
            print(horizontal_line)
            for j, cell in enumerate(row):
                if agent_x == i and agent_y == j:
                    cell_content = Fore.GREEN + 'Agent'.center(cell_width) + Style.RESET_ALL
                    if agent.directions:
                        cell_content +=Fore.BLUE+f"{direction_symbols[agent.directions[agent.direction_index]]}" +Style.RESET_ALL
                elif not cell:
                    cell_content = 'None'.center(cell_width)
                elif 'Wumpus' in cell:
                    cell_content = Fore.MAGENTA + ','.join(cell).center(cell_width) + Style.RESET_ALL
                elif 'Pit' in cell:
                    cell_content = Fore.RED + ','.join(cell).center(cell_width) + Style.RESET_ALL
                elif 'Gold' in cell:
                    cell_content = Fore.YELLOW + ','.join(cell).center(cell_width) + Style.RESET_ALL


                else:
                    cell_content = ','.join(cell).center(cell_width)
                print("|" + cell_content, end="")
            print("|")
        print(horizontal_line + "\n")


world = GridWorld()
world.setup_grid()
world.print_grid()

