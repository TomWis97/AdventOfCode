from aoc import AdventOfCode as aoc

a = aoc(debug=False)

# PART 1
def list_processor(in_data):
    prev_mes = None
    counter = 0
    for raw_measurement in in_data:
        measurement = int(raw_measurement)
        if prev_mes == None:
            prev_mes = measurement
            continue
        if measurement > prev_mes:
            a.dp("Increased: {} to {}".format(prev_mes, measurement))
            counter += 1
        else:
            a.dp("Nothing: {} to {}".format(prev_mes, measurement))
        prev_mes = measurement
    return counter

a.sp(list_processor(a.d), part=1)
    
# PART 2
# First, build list of sliding windows.
windows = []
for index in range(len(a.d)-2):
    windows.append(
        int(a.d[index]) +
        int(a.d[index + 1]) +
        int(a.d[index + 2]))

a.sp(list_processor(windows), part=2)
