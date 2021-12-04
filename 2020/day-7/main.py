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

found_bags = 0
for colour in rules:
    if check_bag(colour, "shiny gold", rules):
        found_bags += 1

print("Result:", found_bags)
