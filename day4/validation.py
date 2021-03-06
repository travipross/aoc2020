import re 

def validate_int_range(val, min, max):
    return min <= int(val) <= max

def validate_height(hgt, min_in, max_in, min_cm, max_cm):
    res = re.search('([0-9]+)(cm|in)', hgt)
    if res is None:
        return False

    n, unit = res.groups()
    if unit == 'in':
        return validate_int_range(n, min_in, max_in)
    else:
        return validate_int_range(n, min_cm, max_cm)

def validate_hair(hcl):
    return re.search('#[a-f0-9]{6}$', hcl) is not None

def validate_eye(ecl):
    return ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def validate_passport_id(pid):
    return re.search('^[0-9]{9}$', pid) is not None

def is_valid(passport, required_fields, strict=False, DEBUG=False): 
    has_req_fields = set(required_fields).issubset(set(passport.keys()))

    # always invalid
    if not has_req_fields:
        return False

    # if not strict, this is good enough
    if not strict:
        return True

    # if strict, must check each field
    else:
        if not validate_int_range(passport['byr'], 1920, 2002):
            if DEBUG: print(f"bad byr: {passport['byr']}")
            return False
        elif not validate_int_range(passport['iyr'], 2010, 2020):
            if DEBUG: print(f"bad iyr: {passport['iyr']}")
            return False
        elif not validate_int_range(passport['eyr'], 2020, 2030):
            if DEBUG: print(f"bad eyr: {passport['eyr']}")
            return False
        elif not validate_height(passport['hgt'], 59, 76, 150, 193):
            if DEBUG: print(f"bad hgt: {passport['hgt']}")
            return False
        elif not validate_hair(passport['hcl']):
            if DEBUG: print(f"bad hcl: {passport['hcl']}")
            return False
        elif not validate_eye(passport['ecl']):
            if DEBUG: print(f"bad ecl: {passport['ecl']}")
            return False
        elif not validate_passport_id(passport['pid']):
            if DEBUG: print(f"bad pid: {passport['pid']}")
            return False

    # if nothing was invalid, return valid
    return True        
 