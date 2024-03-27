import random


class Agent:
    def __init__(self, grid_size):
        self.x = 1  # 시작 위치 X
        self.y = 1  # 시작 위치 Y
        self.grid_size = grid_size
        self.has_gold = False  # 금을 가지고 있는지 여부
        self.is_alive = True  # 에이전트가 살아있는지 여부

    def move(self, grid):
        directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        random.shuffle(directions)  # 방향을 랜덤하게 섞습니다.

        moved = False
        for direction in directions:
            if direction == 'UP':
                new_y = self.y - 1
                if self.is_valid_move(self.x, new_y, grid):
                    self.y = new_y
                    moved = True
            elif direction == 'DOWN':
                new_y = self.y + 1
                if self.is_valid_move(self.x, new_y, grid):
                    self.y = new_y
                    moved = True
            elif direction == 'LEFT':
                new_x = self.x - 1
                if self.is_valid_move(new_x, self.y, grid):
                    self.x = new_x
                    moved = True
            elif direction == 'RIGHT':
                new_x = self.x + 1
                if self.is_valid_move(new_x, self.y, grid):
                    self.x = new_x
                    moved = True

            if moved:  # 유효한 이동이 이루어졌다면 현재 셀을 확인합니다.
                break

        if not moved:
            print("Can't move in any direction.")

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
        self.is_alive = False
