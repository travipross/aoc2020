import re

LEFT_TURN = {
    'N': 'W',
    'E': 'N',
    'S': 'E',
    'W': 'S'
}

RIGHT_TURN = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N'
}

TURN_DICTS = {
    'R': RIGHT_TURN,
    'L': LEFT_TURN
}

def read_data(filename):
    with open(filename) as f:
        raw_data = f.read()
    return raw_data

def parse_data(raw_data):
    pattern = '([NSEWLRF])([0-9]+)'
    instructions = list(re.findall(pattern, raw_data))

    return instructions

def rotate_waypoint_around_ship(position, dir):
    if dir == 'R':
        waypoint_x = position['waypoint']['y']
        waypoint_y = -position['waypoint']['x']
    elif dir == 'L':
        waypoint_x = -position['waypoint']['y']
        waypoint_y = position['waypoint']['x']

    position['waypoint'] = {
        'x': waypoint_x,
        'y': waypoint_y
    }

def move_ship(position, instruction):
    if instruction[0] == 'E':
        position['x'] += int(instruction[1])
    elif instruction[0] == 'W':
        position['x'] -= int(instruction[1])
    elif instruction[0] == 'N':
        position['y'] += int(instruction[1])
    elif instruction[0] == 'S':
        position['y'] -= int(instruction[1])
    elif instruction[0] in ['L', 'R']:
        n_turns = int(int(instruction[1]) / 90)
        for _ in range(n_turns):
            position['heading'] = TURN_DICTS[instruction[0]][position['heading']]
    elif instruction[0] == 'F':
        move_ship(position, (position['heading'], instruction[1]))
    else:
        print("Unrecognized instruction")

def move_ship_waypoint(position, instruction):
    if instruction[0] == 'E':
        position['waypoint']['x'] += int(instruction[1])
    elif instruction[0] == 'W':
        position['waypoint']['x'] -= int(instruction[1])
    elif instruction[0] == 'N':
        position['waypoint']['y'] += int(instruction[1])
    elif instruction[0] == 'S':
        position['waypoint']['y'] -= int(instruction[1])
    elif instruction[0] in ['L', 'R']:
        n_turns = int(int(instruction[1]) / 90)
        for _ in range(n_turns):
            rotate_waypoint_around_ship(position, instruction[0])
    elif instruction[0] == 'F':
        move_ship(position, ('E', int(instruction[1])*position['waypoint']['x']))
        move_ship(position, ('N', int(instruction[1])*position['waypoint']['y']))
    else:
        print("Unrecognized instruction")

def part_a(position, instructions):
    for inst in instructions:
        move_ship(position, inst)
    return abs(position['x']) + abs(position['y'])

def part_b(position, instructions):
    for inst in instructions:
        move_ship_waypoint(position, inst)
    return abs(position['x']) + abs(position['y'])

if __name__ == "__main__":
    raw_data = read_data('input.txt')
    instructions = parse_data(raw_data)

    position_dict = {
        'heading': 'E',
        'x': 0,
        'y': 0,
    }

    a = part_a(position_dict, instructions)
    print(f"Answer A: {a}")
    
    position_dict = {
        'heading': 'E',
        'x': 0,
        'y': 0,
        'waypoint': {
            'x': 10,
            'y': 1
        }
    }
        
    b = part_b(position_dict, instructions)
    print(f"Answer B: {b}")
