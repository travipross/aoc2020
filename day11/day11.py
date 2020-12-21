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

    arr = np.array(raw_lists)
    return arr


def get_adjacent_seats(seat_arr, seat_row, seat_col, allow_skip=False):
    seat_vals = []
    if not allow_skip:
        for r in range(seat_row-1, seat_row+2):
            for c in range(seat_col-1, seat_col+2):
                if r == seat_row and c == seat_col:
                    continue
                if r < 0 or r >= seat_arr.shape[0]:
                    continue
                if c < 0 or c >= seat_arr.shape[1]:
                    continue
                seat_vals.append(seat_arr[r][c])
    else:
        dir_vecs = [
            [0, 1],
            [0, -1],
            [1, 1],
            [1, 0],
            [1, -1],
            [-1, 1],
            [-1, 0],
            [-1, -1],
        ]
        for dir_vec in dir_vecs:
            skip_num = 1
            while True:
                r = seat_row + dir_vec[0]*skip_num
                c = seat_col + dir_vec[1]*skip_num
                if r < 0 or r >= seat_arr.shape[0]:
                    break
                if c < 0 or c >= seat_arr.shape[1]:
                    break
                if seat_arr[r][c] == '.':
                    skip_num += 1
                    continue
                seat_vals.append(seat_arr[r][c])
                break

        
                

    return seat_vals

def change_seats(seat_arr, occupied_threshold=4, allow_skip=False):
    new_arr = seat_arr.copy()
    for r in range(seat_arr.shape[0]):
        for c in range(seat_arr.shape[1]):
            if seat_arr[r][c] == '.':
                continue
            adjacent_seats = get_adjacent_seats(seat_arr, r, c, allow_skip=allow_skip) 

            if seat_arr[r][c] == 'L' and sum([ s == '#' for s in adjacent_seats ]) == 0:
                new_arr[r][c] = '#'
                
            elif seat_arr[r][c] == '#' and sum([ s == '#' for s in adjacent_seats ]) >= occupied_threshold:
                new_arr[r][c] = 'L'
    return new_arr

def part_a(original_seats):
    new_seats = change_seats(original_seats)
    seat_changes = 1
    while not np.array_equal(new_seats, original_seats):
        original_seats = new_seats
        new_seats = change_seats(original_seats)
        seat_changes += 1
    
    print(f"Solution found after {seat_changes} seat changes")

    return np.count_nonzero(new_seats == '#')

def part_b(original_seats):
    new_seats = change_seats(original_seats, allow_skip=True, occupied_threshold=5)
    seat_changes = 1
    while not np.array_equal(new_seats, original_seats):
        original_seats = new_seats
        new_seats = change_seats(original_seats, allow_skip=True, occupied_threshold=5)
        seat_changes += 1
        
    print(f"Solution found after {seat_changes} seat changes")
    return np.count_nonzero(new_seats == '#')

if __name__ == "__main__":
    raw_data = read_data('input.txt')
    seat_arr = parse_data(raw_data)

    print(f"Seat arr: {seat_arr.shape}")

    a = part_a(seat_arr)
    print(f"Answer A: {a}")
    
    b = part_b(seat_arr)
    print(f"Answer B: {b}")
