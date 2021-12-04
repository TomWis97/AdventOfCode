with open('input.txt', 'rt') as f:
    input_data = f.readlines()

for current_number in input_data:
    for test_number in input_data:
        if int(current_number) + int(test_number) == 2020:
          print("Answer:", int(current_number) * int(test_number))
          exit()
