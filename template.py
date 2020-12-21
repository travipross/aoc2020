
def read_data(filename):
    with open(filename) as f:
        raw_data = f.read()
    return raw_data

def parse_data(raw_data):
    parsed_data = raw_data 

    return parsed_data

def part_a(parsed_data):
    pass

def part_b(parsed_data):
    pass

if __name__ == "__main__":
    raw_data = read_data('input.txt')
    parsed_data = parse_data(raw_data)

    a = part_a(parsed_data)
    print(f"Answer A: {a}")
    
    b = part_b(parsed_data)
    print(f"Answer B: {b}")
