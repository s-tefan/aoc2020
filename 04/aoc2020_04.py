

def add_from_file_to_wordlist(f, word_list):
    line = f.readline()
    eof = not line
    line = line.strip()
    if line:
        word_list += line.split()
        return add_from_file_to_wordlist(f, word_list)
    else:
        return word_list, eof

    
def get_passport_from_file(f):
    blurp = add_from_file_to_wordlist(f, [])
    word_list, eof = blurp
    passport = {}
    for word in word_list:
        pair = word.split(":")
        if len(pair) != 2:
            raise Exception("Fel i data!")
        passport[pair[0]] = pair[1]
    return passport, eof

def one():
    filename = "input.txt"
    with open(filename) as f:
        eof = False
        valid_count = 0
        req_fields = {
            'byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid'}
        while not eof:
            passport, eof = get_passport_from_file(f)
            #print(passport)
            valid_count += req_fields.issubset(passport)
        print(valid_count)

def hgt_check(hgt_str):
    if hgt_str[-2:] == "cm":
        bu = int(hgt_str.strip("cm"))
        return 150 <= bu and bu <= 193
    elif hgt_str[-2:] == "in":
        bu = int(hgt_str.strip("in"))
        return 59 <= bu and bu <= 76
    else:
        return False

def hcl_check(hcl_str):
    if len(hcl_str) != 7:
        return False    
    if hcl_str[0] != "#":
        return False
    return sum(x in "0123456789abcdef" for x in hcl_str[1:])

def two():
    filename = "input.txt"
    with open(filename) as f:
        eof = False
        valid_count = 0
        req_fields = {
            'byr',
            'iyr',
            'eyr',
            'hgt',
            'hcl',
            'ecl',
            'pid'}
        while not eof:
            passport, eof = get_passport_from_file(f)
            if req_fields.issubset(passport):
                ok = \
                    1920 <= int(passport["byr"]) and  int(passport["byr"]) <= 2002 and \
                    2010 <= int(passport["iyr"]) and int(passport["iyr"]) <= 2020 and \
                    2020 <= int(passport["eyr"]) and int(passport["eyr"]) <= 2030 and \
                    hgt_check(passport["hgt"]) and \
                    hcl_check(passport["hcl"]) and \
                    passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"} and \
                    len(passport["pid"]) == 9 and sum([c in "0123456789" for c in passport["pid"]]) == 9
            else:
                ok = False
            valid_count += ok
        print(valid_count)

one()
two()