import numpy as np

def parse_data(raw_data):
    lines = raw_data.splitlines()

    substituted = []
    for line in lines:
        line = line.replace('.', '0')
        line = line.replace('#', '1')
        substituted.append([int(l) for l in line])

    return np.array(substituted)

def is_tree(arr, row, col):
    _, w = arr.shape
    return arr[row][col % w]  # wrap around horizontally

def count_trees_from_corner(arr, step):
    loc = np.array([0, 0])
    treecount = 0
    while loc[0] < arr.shape[0]:
        treecount += is_tree(arr, *loc)
        loc += step 

    return treecount

def part_a(arr, step):
    initial_loc = np.array([0, 0])
    step = np.array(step)
    treecount = count_trees_from_corner(arr, step)
    return treecount

def part_b(arr, step_list):
    return np.prod(
            [
                count_trees_from_corner(arr, step) 
                for step in step_list
            ]
        )

if __name__ == "__main__":
    with open('input.txt') as f:
        raw_data = f.read()
    
    arr = parse_data(raw_data)
    step = [1, 3]

    a = part_a(arr, step)
    print(f"Answer A: {a}")

    steps = [
        [1, 1],
        [1, 3],
        [1, 5],
        [1, 7],
        [2, 1]
    ]
    b = part_b(arr, steps)
    print(f"Answer B: {b}")