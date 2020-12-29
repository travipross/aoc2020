import numpy as np


def read_data(filename):
    with open(filename) as f:
        raw_data = f.read()
    return raw_data

def parse_data(raw_data):
    lines = raw_data.splitlines()

    raw_lists = []
    for line in lines:
        raw_lists.append(list(line))

    arr = np.where(np.array(raw_lists) == '.', 0, 1)
    return arr

def preallocate_array(arr_orig, n_cycles=6):
    h_0, w_0 = arr_orig.shape
    h_f = h_0 + 2*(n_cycles-1)
    w_f = w_0 + 2*(n_cycles-1)
    d_f = 1 + 2*n_cycles

    arr = np.zeros((h_f, w_f, d_f))

    r_start = int((h_f - h_0)/2)
    r_end = r_start + h_0

    c_start = int((w_f - w_0)/2)
    c_end = c_start + w_0

    arr[n_cycles, r_start:r_end, c_start:c_end] = arr_orig

    return arr

def get_new_val(cube_val, neighbors):
    if cube_val == 1 and sum(neighbors) not in [2, 3]:
        return 0
    elif cube_val == 0 and sum(neighbors) == 3:
        return 1
    else:
        return cube_val
    
def perform_cycle(arr):
    new_arr = arr.copy()
    d, h, w = arr.shape 
    for z in range(d):
        for r in range(h):
            for c in range(w):
                new_arr[z,r,c] = get_new_val(arr[z,r,c], get_neighboring_cubes((z,r,c), arr))
    return new_arr

def get_neighboring_cubes(coord_tup, arr):
    neighbors = []
    d, h, w = arr.shape
    for z in range(coord_tup[0]-1, coord_tup[0]+2):
        if z < 0 or z >= d:
            continue
        for r in range(coord_tup[1]-1, coord_tup[1]+2):
            if r < 0 or r >= h:
                continue
            for c in range(coord_tup[2]-1, coord_tup[2]+2):
                if c < 0 or c >= w or (z, r, c) == coord_tup:
                    continue
                # print(f"(z, r, c)={z}, {r}, {c}")
                neighbors.append(arr[z, r, c])
    return neighbors

def part_a(parsed_data):
    arr = preallocate_array(parsed_data, 12)
    
    for _ in range(6):
        arr = perform_cycle(arr)
    return np.sum(arr)



def part_b(parsed_data):
    pass

if __name__ == "__main__":
    raw_data = read_data('input.txt')
    parsed_data = parse_data(raw_data)

    sample_data = parse_data(read_data('sample.txt'))

    a = part_a(parsed_data)
    print(f"Answer A: {a}")
    
    b = part_b(parsed_data)
    print(f"Answer B: {b}")
