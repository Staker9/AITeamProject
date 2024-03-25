# Sensor.py 파일

def add_breeze(grid, x, y, grid_size):
    for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= i < grid_size and 0 <= j < grid_size and 'Wall' not in grid[i][j]:
            grid[i][j].append('Br')

def add_glitter(grid, x, y):
    if 'Wall' not in grid[x][y]:
        grid[x][y].append('G')

def add_stench(grid, x, y, grid_size):
    for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= i < grid_size and 0 <= j < grid_size and 'Wall' not in grid[i][j]:
            grid[i][j].append('S')
