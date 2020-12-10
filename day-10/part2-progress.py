import itertools
import math

with open('input2.txt', 'rt') as f:
    input_data = f.readlines()

data = [ int(x) for x in input_data ]
data.sort()

def validate_combination(combination):
    previous_value = 0
    for line in combination:
        if line - previous_value == 1:
            pass
        elif line - previous_value == 3:
            pass
        else:
            return False
        previous_value = line
    return True

valid_combos = 0
total_amount = math.factorial(len(data))
current_amount = 0
for combination in itertools.permutations(data, len(data)):
    if validate_combination(combination):
        valid_combos += 1
    current_amount += 1
    if current_amount % 10000 == 0:
        # Don't update the progress that often
        percent = round((current_amount / total_amount) * 100, 5)
        print("\rProgress: {}".format(percent), end="")

print("\nValid combinations:", valid_combos)
