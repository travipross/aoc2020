
def parse_data(raw_data):
    return [ group.split('\n') for group in raw_data.split("\n\n") ]

def part_a(group_responses):
    total=0
    for group_response in group_responses:
        responses = set()
        for individual_response in group_response:
            responses = responses.union(individual_response)
        total += len(responses)
    return total


def part_b(group_responses):
    total = 0
    for group_response in group_responses:
        responses = set.intersection(*[set(g) for g in group_response])
        total += len(responses)
    return total

if __name__ == "__main__":
    with open('input.txt') as f:
        raw_data = f.read()
    
    group_responses = parse_data(raw_data)

    a = part_a(group_responses)
    print(f"Answer A: {a}")
    
    b = part_b(group_responses)
    print(f"Answer B: {b}")