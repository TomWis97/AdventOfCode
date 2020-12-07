with open('input.txt', 'rt') as f:
    input_data = f.readlines()

for number1 in input_data:
    for number2 in input_data:
        for number3 in input_data:
            if int(number1) + int(number2) + int(number3) == 2020:
              print("Answer:", int(number1) * int(number2) * int(number3))
              exit()
