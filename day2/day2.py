import re 
import json

def parse_input(raw_data):
    pattern = '([0-9]+)-([0-9]+) (.): (.*)'
    matches = re.findall(pattern, raw_data)

    pass_dicts = []
    for m in matches:
        pass_dicts.append(
            {
                'min': int(m[0]),
                'max': int(m[1]),
                'char': m[2],
                'pass': m[3]
            }
        )
    return pass_dicts

def logical_xor(a, b):
    return bool(a) ^ bool(b)

def is_valid_password(match_dict, mode='a'):
    if mode == 'a':
        return match_dict['min'] <= match_dict['pass'].count(match_dict['char']) <= match_dict['max']
    elif mode == 'b':
        first_match = match_dict['pass'][match_dict['min']-1] == match_dict['char'] 
        second_match = match_dict['pass'][match_dict['max']-1] == match_dict['char']
        return logical_xor(first_match, second_match)
    else:
        raise NotImplementedError(f"Unsupported mode: {mode}")

def part_a(pass_dicts):
    return sum([is_valid_password(p) for p in pass_dicts])

def part_b(pass_dicts):
    return sum([is_valid_password(p, mode='b') for p in pass_dicts])

if __name__ == "__main__":
    with open('input.txt') as f:
        raw_data = f.read()
    
    pass_dicts = parse_input(raw_data)

    a = part_a(pass_dicts)
    print(f"Answer A: {a}")

    b = part_b(pass_dicts)
    print(f"Answer B: {b}")