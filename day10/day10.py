from collections import defaultdict

def read_data(filename):
    with open(filename) as f:
        raw_data = f.read()
    return raw_data

def parse_data(raw_data):
    parsed_data = sorted([0] + [int(d) for d in raw_data.splitlines()])
    parsed_data.append(3+parsed_data[-1])
    return parsed_data

def summarize_deltas(voltage_list): 
    d = defaultdict(int)
    ct = defaultdict(int, {0: 1})
    for a, b in zip(voltage_list[1:], voltage_list):
        d[a-b] += 1
        ct[a] = ct[a-3] + ct[a-2] + ct[a-1]
    return d, ct

def part_a(parsed_data):
    deltas, _ = summarize_deltas(parsed_data)
    return deltas[1] * deltas[3]

def part_b(parsed_data):
    _, ct = summarize_deltas(parsed_data)
    return ct[parsed_data[-1]]

if __name__ == "__main__":
    raw_data = read_data('input.txt')
    parsed_data = parse_data(raw_data)

    a = part_a(parsed_data)
    print(f"Answer A: {a}")
    
    b = part_b(parsed_data)
    print(f"Answer B: {b}")
