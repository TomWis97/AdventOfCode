with open('input.txt', 'rt') as f:
    input_data = f.readlines()

valid_num = 0

for line in input_data:
    reqs, password = line.split(':')
    req_char = reqs.split(' ')[1]
    place1, place2 = reqs.split(' ')[0].split('-')
    verify1 = False
    verify2 = False
    try:
        if password.strip()[int(place1)-1] == req_char: verify1 = True
        if password.strip()[int(place2)-1] == req_char: verify2 = True
        if ( verify1 != verify2 and ( verify1 or verify2 )):
            #print(line.strip(), ":", verify1, verify2)
            valid_num += 1
    except IndexError:
        #print(line.strip(), ": IndexError")
        continue

print("Number of valid passwords:", valid_num)
