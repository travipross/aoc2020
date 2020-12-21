import re 

def read_data(filename):
    with open('input.txt') as f:
        raw_data = f.read()
    return raw_data

def parse_data(raw_data):
    main_pattern = '(.*) bags? contain (.*).'
    contained_pattern = '([0-9]+) (.+?) bags?'

    main_groups = re.findall(main_pattern, raw_data)

    rules_dict = {}

    for rule in main_groups:
        containable_matches = re.findall(contained_pattern, rule[1])
        rules_dict[rule[0]] = dict(
            [ (b, int(a)) for (a, b) in containable_matches ]
        )
    
    return rules_dict


def holds_bag_recursive(rules_dict, holding_bag, target_bag):
    if target_bag in rules_dict.get(holding_bag, {}):
        return True
    elif rules_dict.get(holding_bag) is None:
        return False
    else:
        return any(
            [ 
                holds_bag_recursive(rules_dict, b, target_bag)
                for b in rules_dict.get(holding_bag)
            ]
        )


def part_a(rules_dict, target_bag):
    total_true = 0
    for bag in list(rules_dict.keys()):
        bag_flag = holds_bag_recursive(rules_dict, bag, target_bag)
        total_true += bag_flag
    return total_true

def part_b(rules_dict, target_bag):
    n_contained_bags = 0
    for bag, ct in rules_dict.get(target_bag).items():
        n_contained_bags += ct * (1 + part_b(rules_dict, bag))
    return n_contained_bags

if __name__ == "__main__":
    raw_data = read_data('input.txt')
    rules_dict = parse_data(raw_data)
    
    target_bag = 'shiny gold'

    a = part_a(rules_dict, target_bag)
    print(f"Answer A: {a}")
    
    b = part_b(rules_dict, target_bag)
    print(f"Answer B: {b}")
