

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
        print(passport)
        valid_count += req_fields.issubset(passport)
    print(valid_count)




