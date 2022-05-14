# RULES:
# A cell with less than 2 neighbors dies of isolation
# A cell with more than 3 neighbors dies of over population
# A dead cell is replaced with living cell if it has exactly 3 neighbors
# The status of a cell stays the same if it has exactly 2 neighbors
# All deaths and births happen all at the same time
# The changes happenend to a generation can only effect the next generation
from copy import deepcopy
import random
from time import sleep
import colorama
from colorama import Fore
colorama.init(autoreset=True, convert=True)

SIZE = int(input("Size of grid: "))
grid = [[random.randrange(0, 2) for _ in range(SIZE)] for _ in range(SIZE)]


def is_alive(cell):
    if cell == 1:
        return True
    return False


def get_neighbors(row, cell, grid):
    neighbors = []
    positions = [(row-1, cell-1), (row-1, cell), (row-1, cell+1), (row, cell-1), (row, cell+1), (row+1, cell-1), (row+1, cell), (row+1, cell+1)]
    for r, c in positions:
        if (SIZE > r >= 0) and (SIZE > c >= 0):
            neighbors.append(grid[r][c])
    return neighbors


def count_alive_neighbors(row, cell, grid):
    neighbors = get_neighbors(row, cell, grid)
    return sum(neighbors)


def new_gen():
    old_grid = deepcopy(grid)
    for row in range(SIZE):
        for cell in range(SIZE):
            alive_neighbors = count_alive_neighbors(row, cell, old_grid)
            if alive_neighbors > 3:
                grid[row][cell] = 0  # Dies of over population

            elif alive_neighbors == 3:
                grid[row][cell] = 1  # New alive cell

            elif alive_neighbors < 2:
                grid[row][cell] = 0  # Dies of isolation
    


def print_grid():
    for row in grid:
        cells = ""
        for c in row:
            cells += f"{Fore.GREEN}{c}{Fore.WHITE} " if c == 1 else f"{Fore.WHITE}{c} "
        print(cells)
    print("\n")


print_grid()
while True:
    sleep(0.6)
    new_gen()
    print_grid()

