import progressbar

def read_data(filename):
    with open(filename) as f:
        raw_data = f.read()
    return raw_data

def parse_data(raw_data):
    parsed_data = [int(d) for d in raw_data.split(",")]

    return parsed_data

def speak_number(hist_dict):
    # get the last number spoken, and the turn that it was last spoken before that
    last_num = hist_dict['last_num']
    last_time_spoken = hist_dict.get(last_num)
    
    # if last time was the first time, speak 0 next
    if last_time_spoken is None:
        new_num = 0
    # if the number was spoken during a previous turn, get difference in turn numbers
    else:
        new_num = hist_dict['last_turn'] - last_time_spoken
    
    # update history dict for next iteration
    hist_dict[last_num] = hist_dict['last_turn']
    hist_dict['last_num'] = new_num
    hist_dict['last_turn'] += 1

def speak_numbers_until_limit(parsed_data, limit):
    # Initialize hist dict for pre-defined numbers
    hist_dict = {n: idx+1 for idx, n in list(enumerate(parsed_data))[:-1]}
    hist_dict.update({
            'last_turn': len(parsed_data),
            'last_num': parsed_data[-1]
        })

    with progressbar.ProgressBar(max_value=limit) as bar:
        bar.update(0)
        # iterate specified number of turns
        while hist_dict['last_turn'] < limit:
            speak_number(hist_dict)
            if hist_dict['last_turn'] % (limit/20) == 0:
                bar.update(hist_dict['last_turn'])

    return hist_dict['last_num']

def part_a(parsed_data):
    return speak_numbers_until_limit(parsed_data, 2020)

def part_b(parsed_data):
    return speak_numbers_until_limit(parsed_data, 3e7)

if __name__ == "__main__":
    raw_data = read_data('input.txt')
    parsed_data = parse_data(raw_data)

    a = part_a(parsed_data)
    print(f"Answer A: {a}")

    b = part_b(parsed_data)
    print(f"Answer B: {b}")
