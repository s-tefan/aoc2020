
from functools import reduce

def range_read(s):
    a, b = s.split('-')
    return range(eval(a),eval(b+1))

def tuple_read(s):
    return eval(tuple_line)

def rule_read(rule_line, rule_dict):
    if rule_line:
        try:
            a, b = rule_line.split(': ')
            d = map(lambda x: x.split('-'), b.split(' or ')) # split interval strings to [str(first), str(last)]
            e = map(lambda x: eval('range({},{} + 1)'.format(x[0],x[1])), d) # list of ranges
            rule_dict.update({a:tuple(e)})
            return True
        except:
            return False

def ticket_read(ticket_line, ticket_set = None):
    try:
        ticket_tuple = eval(ticket_line)
        if ticket_set != None:
            ticket_set.add(ticket_tuple) # add the ticket field values as a tuple to ticket_set
        return ticket_tuple
    except:
        return False

def read(filename):
    with open(filename) as f:
        rule_dict = {}
        ticket_set = set()
        while rule_read(f.readline().strip(), rule_dict): pass
        while f.readline().strip() != "your ticket:": pass
        my_ticket = ticket_read(f.readline().strip())
        while f.readline().strip() != "nearby tickets:": pass
        while ticket_read(f.readline().strip(), ticket_set): pass
    return rule_dict, my_ticket, ticket_set

def error_generator(rule_dict, ticket_set):
    for ticket in ticket_set:
        for field in ticket:
            check = False
            for rule in rule_dict.values():
                if reduce(lambda first, next: field in first or field in next, rule):
                    check = True
                    break
            if not check:
                yield field
                break

rule_dict, my_ticket, ticket_set = read("input.txt")
print("Part 1:",sum(error_generator(rule_dict, ticket_set)))
