def onetwo():
    filename = "input.txt"
    uset = {chr(x) for x in range(ord('a'),ord('z')+1)}
    current_set, current_set_int = set(), uset
    list_of_sets = []

    with open(filename) as f:
        for line in f:
            a_str = line.strip()
            if a_str:
                current_set.update(set(a_str))
                current_set_int = \
                    current_set_int.intersection(set(a_str))
            elif current_set: # First of a seq of blank rows
                    list_of_sets.append(
                        (current_set, current_set_int))
                    current_set, current_set_int = set(), uset
        if current_set:
            # Update if there is not a last blank row
            list_of_sets.append(
                (current_set, current_set_int))
    print(sum(len(s[0]) for s in list_of_sets))
    print(sum(len(s[1]) for s in list_of_sets))

onetwo()
