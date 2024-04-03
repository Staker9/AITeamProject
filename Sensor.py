# Sensor.py 파일
#0401 시영
#6, 15 line 'Wall' -> '~'로 변경

#0403 재현
#S 제거함수 추가

def add_breeze(grid, x, y, grid_size):
    for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= i < grid_size and 0 <= j < grid_size and '~' not in grid[i][j]:
            grid[i][j].append('Br')

def add_glitter(grid, x, y):
    if '~' not in grid[x][y]:
        grid[x][y].append('glit')

def add_stench(grid, x, y, grid_size):
    for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= i < grid_size and 0 <= j < grid_size and '~' not in grid[i][j]:
            grid[i][j].append('S')
            
def del_stench(grid, x, y, grid_size):
    for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= i < grid_size and 0 <= j < grid_size and '~' not in grid[i][j]:
            grid[i][j].remove('S')
