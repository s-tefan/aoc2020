""" Advent of Code 2020, day 7."""
__author__ = "Stefan Karlsson"
__date__ = "2020-12-07"

def read(f): 
    """Read lines from file and make a corresponding dict."""
    contain_dict = {}
    for line in f:
        a, b = line.strip().split(" contain ") 
        a_cattr, a_color, _ = a.split(" ")
        b_list = b.strip(".").split(", ")
        contain_dict[(a_cattr, a_color)] = tuple() if b_list[0][:3] == "no " else tuple(map(fix, b_list))   
    return contain_dict

def fix(bagitem): 
    """Make a nice dict for the pair of a color and number."""
    n, cattr, color, _ = bagitem.split(" ")
    return {'c': (cattr,color), 'n': int(n)}

def simplify(contain_dict): 
    """Get rid of the numbers."""
    return {k:tuple(map(lambda a : a['c'], contain_dict[k])) for k in contain_dict}

def find_containers(bag, contain_dict): 
    """Find all bags that must contain a given bag."""
    return set(k for k in contain_dict if bag in contain_dict[k])

def find_containers_transitively(bags, contain_dict): 
    """Recursively take the transitive closure of containment."""
    new = set.union(*(find_containers(bag, contain_dict) for bag in bags))
    return bags if new.issubset(bags) else find_containers_transitively(bags.union(new), contain_dict)

def count_bags(bag, contain_dict): 
    """Recursively count the total number of bags in a given bag (including the bag itself)."""
    return sum(bag['n']*(1+count_bags(bag,contain_dict)) for bag in contain_dict[bag['c']])

"""Start the calculation!"""
with open("input.txt") as f: 
    bag_dict = read(f)
a_dict = simplify(bag_dict)
my_bag = ("shiny", "gold")
print("Part one:", len(find_containers_transitively(find_containers(my_bag, a_dict), a_dict)))
print("Part two:", count_bags({'c': my_bag, 'n': 1}, bag_dict))
