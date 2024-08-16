import random
import pgzrun

WIDTH = 400
HEIGHT = 400

BLOCK_POSITIONS = [
    (350, 50),
    (350, 350),
    (50, 350),
    (50, 50),
]

BLOCK_MOVEMENTS = [
    {'type': 'bounce', 'duration': 1},
    {'type': 'slide', 'duration': 2},
    {'type': 'rotate', 'duration': 3},
]

SHIP_MOVEMENTS = [
    {'type': 'straight', 'duration': 1},
    {'type': 'curve', 'duration': 2},
    {'type': 'zigzag', 'duration': 3},
]

block = Actor('block', center=(50, 50))
ship = Actor('ship', center=(200, 200))

def draw():
    screen.clear()
    block.draw()
    ship.draw()

def move_block():
    movement = random.choice(BLOCK_MOVEMENTS)
    if movement['type'] == 'bounce':
        block.pos = next_block_position()
    elif movement['type'] == 'slide':
        block.pos = next_block_position()
    elif movement['type'] == 'rotate':
        block.angle += 10

def next_block_position():
    return random.choice(BLOCK_POSITIONS)

def move_ship():
    ship.pos = random.randint(100, 300), random.randint(100, 300)

move_block()  # start one move now
clock.schedule_interval(move_block, 2)  # schedule subsequent moves

move_ship()  # start one move now
clock.schedule_interval(move_ship, 2)  # schedule subsequent moves

pgzrun.go()