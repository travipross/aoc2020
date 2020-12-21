
import itertools

def read_data(filename):
    with open(filename) as f:
        raw_data = f.read()
    return raw_data

def parse_data(raw_data):
    return [ int(l) for l in raw_data.splitlines() ]

def pair_sums(preamble, blacklist=[]):
    pairs = itertools.combinations([ p for p in  preamble if p not in blacklist ], 2)
    return [ sum(pair) for pair in pairs ]


def next_is_valid(all_nums, next_idx, preamble_len=25):
    assert(next_idx >= preamble_len and next_idx < len(all_nums))
    preamble = all_nums[next_idx-preamble_len:next_idx]

    return all_nums[next_idx] in pair_sums(preamble)

def find_contiguous_set(all_nums, target_sum):
    for starting_idx in range(0, len(all_nums)-1):
        for ending_idx in range(starting_idx+1, len(all_nums)):
            candidate_set = all_nums[starting_idx:ending_idx]
            candidate_sum = sum(candidate_set)
            if candidate_sum > target_sum:
                break
            elif candidate_sum == target_sum:
                return candidate_set


def part_a(parsed_data, preamble_len=25):
    for n in range(preamble_len, len(parsed_data)):
        if not next_is_valid(parsed_data, n, preamble_len=preamble_len):
            return parsed_data[n]

def part_b(parsed_data, ans_a):
    contiguous_set = find_contiguous_set(parsed_data, ans_a)
    return min(contiguous_set) + max(contiguous_set)


if __name__ == "__main__":
    raw_data = read_data('input.txt')
    parsed_data = parse_data(raw_data)

    a = part_a(parsed_data)
    print(f"Answer A: {a}")
    
    b = part_b(parsed_data, a)
    print(f"Answer B: {b}")
