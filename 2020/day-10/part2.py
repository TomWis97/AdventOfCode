import itertools

with open('input.txt', 'rt') as f:
    input_data = f.readlines()

data = [ int(x) for x in input_data ]
data.sort()

def validate_combination(combination):
    diff_1 = 0
    diff_3 = 0
    previous_value = 0
    for line in combination:
        #if previous_value == 0:
        #    previous_value = line
        #    continue
        if line - previous_value == 1:
            diff_1 += 1
            #print("Added 1. Line: {}, Previous: {}, diff_1: {}".format(line, previous_value, diff_1))
        elif line - previous_value == 3:
            diff_3 += 1
            #print("Added 3. Line: {}, Previous: {}, diff_3: {}".format(line, previous_value, diff_3))
        else:
            #print("Line: {}, Previous: {}".format(line, previous_value))
            return False
        previous_value = line
    return True

valid_combos = 0
for combination in itertools.permutations(data, len(data)):
    if validate_combination(combination):
        valid_combos += 1

print("Valid combinations:", valid_combos)
