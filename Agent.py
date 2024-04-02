import random

class Agent:
    def __init__(self, grid_size):
        self.x = 1  # 시작 위치 X
        self.y = 1  # 시작 위치 Y
        self.grid_size = grid_size
        self.directions = ['UP', 'RIGHT', 'DOWN', 'LEFT']  # 가능한 방향
        self.direction_index = 1  # 현재 방향을 directions 리스트의 인덱스로 표현
        self.has_gold = False  # 금을 가지고 있는지 여부
        self.is_alive = True  # 에이전트가 살아있는지 여부
        self.arrows = 2

    def move(self, grid):
        action = random.choice(['GoForward', 'TurnLeft', 'TurnRight'])
        print(f"Action: {action}")  # 선택된 행동을 출력
        if action == 'GoForward':
            self.go_forward(grid)
        elif action == 'TurnLeft':
            self.turn_left()
        elif action == 'TurnRight':
            self.turn_right()

        print(f"New Direction: {self.directions[self.direction_index]}")  # 새로운 방향을 출력
        self.check_current_cell(grid)

    def go_forward(self, grid):
        direction = self.directions[self.direction_index]
        if direction == 'UP':
            new_y = self.y - 1
        elif direction == 'DOWN':
            new_y = self.y + 1
        else:
            new_y = self.y

        if direction == 'LEFT':
            new_x = self.x - 1
        elif direction == 'RIGHT':
            new_x = self.x + 1
        else:
            new_x = self.x

        if self.is_valid_move(new_x, new_y, grid):
            self.x, self.y = new_x, new_y
            print(f"Moved {direction}")
        else:
            self.bump()

    def turn_left(self):
        self.direction_index = (self.direction_index - 1) % len(self.directions)
        print("Turned left")

    def turn_right(self):
        self.direction_index = (self.direction_index + 1) % len(self.directions)
        print("Turned right")

    def is_valid_move(self, x, y, grid):
        if x < 0 or x >= self.grid_size or y < 0 or y >= self.grid_size or 'Wall' in grid[x][y]:
            return False
        return True

    def bump(self):
        print("Bump! Hit a wall or an invalid space.")

    def check_current_cell(self, grid):
        current_cell = grid[self.x][self.y]
        if 'Gold' in current_cell:
            self.pick_up_gold(grid)
        elif 'Pit' in current_cell or 'Wumpus' in current_cell:
            self.reset()

    def pick_up_gold(self,grid):
        print("Picked up gold!")
        self.has_gold = True
        grid[self.x][self.y].remove('Gold')

    def reset(self):
        print("Resetting agent...")
        self.x = 1
        self.y = 1
        self.direction_index = 1  # 방향 초기화
        self.has_gold = False
        self.is_alive = True
