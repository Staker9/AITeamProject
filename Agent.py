from Wumpus import *
from Sensor import add_breeze, add_glitter, add_stench
import numpy as np

class Agent:
def init(self, grid_size):
self.x = 1  # 시작 위치 X
self.y = 1  # 시작 위치 Y
self.grid_size = grid_size
self.has_gold = False  # 금을 가지고 있는지 여부
self.is_alive = True  # 에이전트가 살아있는지 여부


def move(self, direction, grid): # 랜덤으로 돌아가게 하는 부분도 있어야함
    if direction == 'UP':
        new_y = self.y - 1
        if self.is_valid_move(self.x, new_y, grid):
            self.y = new_y
        else:
            self.bump()
    elif direction == 'DOWN':
        new_y = self.y + 1
        if self.is_valid_move(self.x, new_y, grid):
            self.y = new_y
        else:
            self.bump()
    elif direction == 'LEFT':
        new_x = self.x - 1
        if self.is_valid_move(new_x, self.y, grid):
            self.x = new_x
        else:
            self.bump()
    elif direction == 'RIGHT':
        new_x = self.x + 1
        if self.is_valid_move(new_x, self.y, grid):
            self.x = new_x
        else:
            self.bump()

    self.check_current_cell(grid)

def is_valid_move(self, x, y, grid):
    if x < 0 or x >= self.grid_size or y < 0 or y >= self.grid_size or 'Wall' in grid[x][y]:
        return False
    return True

def bump(self):
    print("Bump! Hit a wall.")

def check_current_cell(self, grid):
    current_cell = grid[self.x][self.y]
    if 'Gold' in current_cell:
        self.pick_up_gold()
    elif 'Pit' in current_cell or 'Wumpus' in current_cell:
        self.reset()

def pick_up_gold(self):
    print("Picked up gold!")
    self.has_gold = True

def reset(self):
    print("Resetting agent...")
    self.x = 1
    self.y = 1
    self.has_gold = False
    self.is_alive = False  # 이 부분은 게임의 룰에 따라 조정할 수 있습니다. 죽음 대신 리셋을 원한다면 is_alive를 True로 유지하고 다른 처리를 할 수 있습니다.
