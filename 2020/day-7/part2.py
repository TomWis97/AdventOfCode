with open('input.txt', 'rt') as f:
    input_data = f.readlines()

def check_bag(source, target, rules):
    """Check if colour source contains a bag target.
    Returns if target is found in source."""
    if target in rules[source]:
        return True
    else:
        for item in rules[source]:
            if check_bag(item, target, rules):
                return True
    return False

def count_bag(source, rules):
    """Returns dict of all bags"""
    data = rules[source]
    bags = 0
    for bag in data:
        bags += data[bag] * (count_bag(bag, rules) + 1 )
    return bags

rules = {}
for line in input_data:
    name = line.split('bags contain')[0].strip()
    name_rules_string = line.split('bags contain')[1].strip()
    name_rules = {}
    if not name_rules_string == "no other bags.":
        for name_rule in name_rules_string.split(', '):
            amount = int(name_rule.split(' ')[0])
            colour = " ".join(name_rule.split(' ')[1:3])
            name_rules[colour] = amount
    rules[name] = name_rules

found_bags = count_bag('shiny gold', rules)

print("Result:", found_bags)
