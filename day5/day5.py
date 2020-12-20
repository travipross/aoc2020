
def row_str_to_int(row_str):
    assert(len(row_str) == 7)
    row_num_binary = row_str.replace('F', '0').replace('B', '1')
    return int(row_num_binary, 2)

def col_str_to_int(col_str):
    assert(len(col_str) == 3)
    col_num_binary = col_str.replace('L', '0').replace('R', '1')
    return int(col_num_binary, 2)

def seat_coord_from_string(full_str):
    row_str = full_str[0:7]
    col_str = full_str[7:]
    return (row_str_to_int(row_str), col_str_to_int(col_str))

def parse_data(raw_data):
    seat_coords = [
        seat_coord_from_string(l) for l in raw_data.splitlines() 
    ]
    return seat_coords

def seat_id_from_coord(row, col):
    return row*8 + col

def part_a(seats):
    return max(
        [ seat_id_from_coord(*seat) for seat in seats ]
    )

def part_b(seats):
    seat_ids_sorted = sorted([ seat_id_from_coord(*seat) for seat in seats ])
    seat_id_init = seat_ids_sorted[0]
    for idx in range(len(seat_ids_sorted)-1):
        if seat_ids_sorted[idx]+1 != seat_ids_sorted[idx+1]:
            return seat_ids_sorted[idx] + 1

if __name__ == "__main__":
    with open('input.txt') as f:
        raw_data = f.read()
    
    seat_coords = parse_data(raw_data)

    a = part_a(seat_coords)
    print(f"Answer A: {a}")
    
    b = part_b(seat_coords)
    print(f"Answer B: {b}")