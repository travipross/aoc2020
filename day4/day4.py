from validation import is_valid

def parse_data(raw_data):
    passports_raw = raw_data.split("\n\n")

    passports = [
        dict(map(lambda x: x.split(':'), passport_raw.replace('\n', ' ').split(' '))) for passport_raw in passports_raw
    ]

    return passports


def part_a(passports, required_fields):
    return len(
        [ p for p in passports if is_valid(p, required_fields) ]
    )

def part_b(passports, required_fields):
    return len(
        [ p for p in passports if is_valid(p, required_fields, strict=True) ]
    )

if __name__ == "__main__":
    with open('input.txt') as f:
        raw_data = f.read()

    required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]
    
    passports = parse_data(raw_data)

    a = part_a(passports, required_fields)
    print(f"Answer A: {a}")
    
    b = part_b(passports, required_fields)
    print(f"Answer B: {b}")
