with open('input.txt', 'rt') as f:
    input_data = f.readlines()

data = [ int(x) for x in input_data ]
data.sort()

diff_1 = 0
diff_3 = 0
previous_value = 0
for line in data:
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
        raise ValueError("Other difference than 1 or 3")
    previous_value = line

# Add +3 for device itself
diff_3 += 1

result = diff_1 * diff_3
#print("diff_1", diff_1, ", diff_3", diff_3)
print("Result:", result)
