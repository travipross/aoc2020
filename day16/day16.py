import re
import json
import numpy as np

def read_data(filename):
    with open(filename) as f:
        raw_data = f.read()
    return raw_data

def parse_data(raw_data):
    constraints_raw, your_ticket_raw, nearby_tickets_raw = raw_data.split('\n\n')

    constraint_pattern = '(.+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)'
    constraints = re.findall(constraint_pattern, constraints_raw)

    your_ticket = [ int(v) for v in your_ticket_raw.split('\n')[1].split(',') ]

    nearby_tickets = [
       [ int(v) for v in l.split(',') ] for l in nearby_tickets_raw.split('\n')[1:]
    ]
    
    parsed_data = {
        'constraints': {
            c[0]: {
                'min0': int(c[1]),
                'max0': int(c[2]),
                'min1': int(c[3]),
                'max1': int(c[4])
            } for c in constraints
        },
        'your_ticket': your_ticket,
        'nearby_tickets': nearby_tickets
    }
    return parsed_data

def satisfies_rule(rule, num):
    return rule['min0'] <= num <= rule['max0'] \
        or rule['min1'] <= num <= rule['max1']

def ticket_fails_all_rules(ticket, constraints):
    for num in ticket:
        passed_a_rule = False 
        for rule in constraints.values():
            # print(f"num: {num}, rule: {rule}")
            if satisfies_rule(rule, num):
                passed_a_rule = True
                break 
        if not passed_a_rule:
            return num
    return False

def part_a(parsed_data):
    error_rate = 0
    for ticket in parsed_data['nearby_tickets']:
        error_rate += ticket_fails_all_rules(ticket, parsed_data['constraints'])
    return error_rate

def part_b(parsed_data):
    valid_tickets = [ t for t in parsed_data['nearby_tickets'] if not ticket_fails_all_rules(t, parsed_data['constraints'])]
        
    potential_fields = {
        n: list(parsed_data['constraints'].keys())
        for n in range(len(parsed_data['constraints']))
    }

    determined_fields = reduce_potential_fields(valid_tickets, potential_fields, parsed_data['constraints'])

    vals = [ get_field_by_name(parsed_data['your_ticket'], name, determined_fields) for name in parsed_data['constraints'] if name.startswith('departure') ]
    return np.prod(vals)

def get_field_by_name(ticket, fieldname, determined_fields):
    for idx, field in determined_fields.items():
        if field == fieldname:
            return ticket[int(idx)]
    return None


def reduce_potential_fields(tickets, potential_fields, constraints):
    potential_fields = potential_fields.copy()

    # first, looping over each index in the ticket pattern
    for idx in potential_fields:
        # looping over each valid ticket
        for t in tickets:
            # if a constraint isn't satisfied, then this index can't be this field
            for field, rule in constraints.items():
                if not satisfies_rule(rule, t[int(idx)]):
                    potential_fields[idx].remove(field)
                    break

    # next, look for indexes having only one potential field, "locking it in"
    determined_fields = {}
    max_iter = 50 
    iter = 0
    # loop as long as all fields have yet to be determined
    while len(determined_fields) != len(potential_fields) and iter <= max_iter:
        determined_field = None
        iter += 1
        # for each index, check if it has length = 1. If so, it's determined. Break after finding one
        for idx in potential_fields:
            if len(potential_fields[idx]) == 1:
                determined_field = potential_fields[idx][0]
                determined_fields[idx] = determined_field
                break

        # if any fields were found to be determined, remove them from potential fields lists
        if determined_field is not None: 
            for idx in potential_fields:
                if determined_field in potential_fields[idx]:
                    potential_fields[idx].remove(determined_field)
        else:
            print(f"NO DETERMINED FIELD THIS ITER ({iter})")
    

    return determined_fields


if __name__ == "__main__":
    raw_data = read_data('input.txt')
    parsed_data = parse_data(raw_data)

    sample_data = parse_data(read_data('sample1.txt'))

    a = part_a(parsed_data)
    print(f"Answer A: {a}")
    
    b = part_b(parsed_data)
    print(f"Answer B: {b}")
