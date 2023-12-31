# Re-write of Engineer Man's Snowstorm project:
# https://www.youtube.com/watch?v=_chP0a4PMTM&list=RDCMUCrUL8K81R4VBzm-KOYwrcxQ&index=3

import os
import random
import time

SNOW_DENSITY = 10
DELAY = .2

snowflakes = ['❄', '❅', '❆', '•', '·']

term = os.get_terminal_size()

w = term.columns
h = term.lines

grid = []

for _ in range(h):
    grid.append([' '] * w)

def draw_grid():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('\033[?25l')

    output = ''

    for row in grid:
        output += ''.join(row) + '\n'

    output = output.strip('\n')

    print(output, end='')

while True:
    row = []

    for _ in range(w):
        if random.random() < SNOW_DENSITY / 100:
            row.append(random.choice(snowflakes))
        else:
            row.append(' ')

    grid.insert(0, row)
    grid.pop()
    draw_grid()

    time.sleep(DELAY)