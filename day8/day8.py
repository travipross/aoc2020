import re 

def read_data(filename):
    with open('input.txt') as f:
        raw_data = f.read()
    return raw_data

def parse_data(raw_data):
    pattern = '([a-z]{3}) (\+|-)([0-9]+)'
    matches = re.findall(pattern, raw_data)

    parsed_data = matches
    return parsed_data

def follow_instructions(instructions, index=0, accumulator=0, past_indexes=[]):
    if index in past_indexes:
        return accumulator, False
    elif index == len(instructions):
        return accumulator, True

    past_indexes.append(index)

    op, sign, num = instructions[index]
    sign = 1 if sign == '+' else -1
    num = int(num)

    if op == 'nop':
        index += 1
    elif op == 'acc':
        accumulator += sign*num
        index += 1
    elif op == 'jmp':
        index += sign*num
    else:
        print(f"Unrecognized instruction: {(op, sign, num)}")

    return follow_instructions(instructions, index=index, accumulator=accumulator, past_indexes=past_indexes)
        
def swap_instructions(instructions, index_to_toggle):
    op, sign, num = instructions[index_to_toggle]

    if op == 'jmp':
        new_op = 'nop'
    elif op == 'nop':
        new_op = 'jmp'
    else:
        return None

    fixed_instructions = instructions[:]
    fixed_instructions[index_to_toggle] = (new_op, sign, num)
    return fixed_instructions

def part_a(instructions):
    acc, successful = follow_instructions(instructions, index=0, accumulator=0, past_indexes=[])
    return acc 

def part_b(instructions):
    for i in range(len(instructions)):
        fixed_instructions = swap_instructions(instructions, i)
        if fixed_instructions is not None:
            acc, successful = follow_instructions(fixed_instructions, index=0, accumulator=0, past_indexes=[])
            if successful:
                return acc

if __name__ == "__main__":
    raw_data = read_data('input.txt')
    instructions = parse_data(raw_data)

    a = part_a(instructions)
    print(f"Answer A: {a}")
    
    b = part_b(instructions)
    print(f"Answer B: {b}")
