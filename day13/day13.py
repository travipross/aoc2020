
def read_data(filename):
    with open(filename) as f:
        raw_data = f.read()
    return raw_data

def parse_data(raw_data):
    current_time, schedule = raw_data.splitlines()
    full_schedule = [ None if x == 'x' else int(x) for x in schedule.split(',') ]
    
    parsed_data = {
        'time': int(current_time),
        'bus_ids': [ b for b in full_schedule if b is not None ],
        'raw': full_schedule
    }
    return parsed_data

def departure_matches_offset(time, bus_ids):
    for idx, bus_id in enumerate(bus_ids):
        if bus_id is None:
            continue
        elif (time + idx) % bus_id != 0:
            return False
    return True

def part_a(parsed_data):
    current_time = parsed_data['time']
    bus_found = False
    bus_time = None
    while not bus_found:
        for bus_id in parsed_data['bus_ids']:
            if current_time % bus_id == 0:
                selected_bus = bus_id
                selected_time = current_time
                bus_found = True
                break
        current_time += 1
    
    return (selected_time - parsed_data['time']) * selected_bus

def part_b(parsed_data):
    bus_defs = [ (idx, bus_id) for idx, bus_id in enumerate(parsed_data['raw']) if bus_id is not None ]
    current_time = 0
    lcm = 1
    for i in range(len(bus_defs) - 1):
        idx = bus_defs[i+1][0]
        bus_id = bus_defs[i+1][1]
        lcm *= bus_defs[i][1]
        while (current_time + idx) % bus_id != 0:
            current_time += lcm
    
    return current_time
        

if __name__ == "__main__":
    raw_data = read_data('input.txt')
    parsed_data = parse_data(raw_data)

    sample_data = parse_data(read_data('sample.txt'))

    sample_a = part_a(sample_data)
    print(f"Sample A: {sample_a}")

    a = part_a(parsed_data)
    print(f"Answer A: {a}")

    sample_b = part_b(sample_data)
    print(f"Sample B: {sample_b}")

    b = part_b(parsed_data)
    print(f"Answer B: {b}")
