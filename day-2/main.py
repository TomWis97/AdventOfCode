with open('input.txt', 'rt') as f:
    input_data = f.readlines()

invalid_num = 0
valid_num = 0

for line in input_data:
    reqs, password = line.split(':')
    req_char = reqs.split(' ')[1]
    req_min, req_max = reqs.split(' ')[0].split('-')
    if int(req_min) <= password.strip().count(req_char) <= int(req_max):
        valid_num += 1
    else:
        invalid_num += 1

print("Number of valid passwords:", valid_num)
