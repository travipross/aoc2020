
def part_a(numbers, target_sum):
    for i in numbers:
        for j in numbers:
            if i+j == target_sum:
                print(f"Found 2 numbers which add to {target_sum}: {[i,j]}")
                return i*j
    return None

def part_b(numbers, target_sum):
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i+j+k == target_sum:
                    print(f"Found 3 numbers which add to {target_sum}: {[i,j,k]}")
                    return i*j*k
    return None

if __name__ == "__main__":
    with open('input.txt') as f:
        numbers = [int(x) for x in f.readlines()]

    target_sum = 2020

    a = part_a(numbers, target_sum)
    print(f"Answer A: {a}")

    b = part_b(numbers, target_sum)
    print(f"Answer B: {b}")