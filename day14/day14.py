import re 
from itertools import combinations

def read_data(filename):
    with open(filename) as f:
        raw_data = f.read()
    return raw_data

def parse_data(raw_data):
    pattern_mask = 'mask = ([0-9X]{36})'
    pattern_mem = 'mem\[([0-9]+)\] = ([0-9]+)'

    lines = raw_data.splitlines()
    instructions = []
    for l in lines:
        if l.startswith('mask'):
            instructions.append({
                'type': 'set_mask',
                'addr': None,
                'val': re.search(pattern_mask, l).groups()[0]
            })
        elif l.startswith('mem'):
            addr, val = re.search(pattern_mem, l).groups()
            instructions.append({
                'type': 'set_mem',
                'addr': addr,
                'val': val
            })
        else:
            print(f"Unrecognized instruction: {l}")

    return instructions

def apply_mask(val_dec, mask):
    val_bin = f'{int(val_dec):036b}'
    output = ''.join(
        [ char_mask if char_mask != 'X' else char_val for char_val, char_mask in zip(val_bin, mask)]
    )
    return int(output, 2)

def perform_instruction_a(inst, state):
    if inst['type'] == 'set_mask':
        state['current_mask'] = inst['val']
    elif inst['type'] == 'set_mem':
        state['memory'][inst['addr']] = apply_mask(inst['val'], state['current_mask'])
    else:
        print(f"Unrecognized instruction: {inst}")
    
    return state

def perform_instruction_b(inst, state):
    if inst['type'] == 'set_mask':
        state['current_mask'] = inst['val']
    elif inst['type'] == 'set_mem':
        all_addrs = get_all_memory_addrs(inst['addr'], state['current_mask'])
        for addr in all_addrs:
            state['memory'][addr] = inst['val']
    else:
        print(f"Unrecognized instruction: {inst}")
    
    return state

def get_all_memory_addrs(addr, mask):
    addr_bin = f"{int(addr):036b}"
    floating_bit_idxs = [ int(idx) for idx, bit in enumerate(mask) if bit == 'X'] 
    n_floating = len(floating_bit_idxs)
    
    bit_variants = [f'{x:036b}'[-n_floating:] for x in range(2**len(floating_bit_idxs)) ]
    mem_addrs = []
    for bit_variant in bit_variants:
        new_addr = [ addr_bit if mask_bit != '1' else '1' for addr_bit, mask_bit in zip(addr_bin, mask) ]
        for bit, float_idx in zip(bit_variant, floating_bit_idxs):
            new_addr[float_idx] = bit
        mem_addrs.append(int(''.join(new_addr), 2))
    return mem_addrs

def part_a(parsed_data):
    state = {
        'current_mask': None, 
        'memory': {}
    }
    for inst in parsed_data:
        state = perform_instruction_a(inst, state)
    
    return sum([int(v) for v in state['memory'].values()])

def part_b(parsed_data):
    state = {
        'current_mask': None, 
        'memory': {}
    }
    for inst in parsed_data:
        state = perform_instruction_b(inst, state)
    
    return sum([int(v) for v in state['memory'].values()])

if __name__ == "__main__":
    raw_data = read_data('input.txt')
    parsed_data = parse_data(raw_data)

    a = part_a(parsed_data)
    print(f"Answer A: {a}")

    b = part_b(parsed_data)
    print(f"Answer B: {b}")
