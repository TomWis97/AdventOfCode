with open('input.txt', 'rt') as f:
    input_data = f.readlines()

instructions = []
for line in input_data:
    cmd, value = line.split(' ')
    instructions.append((cmd, int(value)))

def run_program(instructions):
    current_instruction = 0
    executed_instructions = []
    accumulator = 0
    while True:
        if current_instruction in executed_instructions:
            return False
        try:
            cur = instructions[current_instruction]
        except IndexError:
            # We hit the end!
            return accumulator
        if cur[0] == "acc":
            accumulator += cur[1]
            executed_instructions.append(current_instruction)
            current_instruction += 1
        elif cur[0] == "jmp":
            executed_instructions.append(current_instruction)
            current_instruction += cur[1]
        elif cur[0] == "nop":
            executed_instructions.append(current_instruction)
            current_instruction += 1
        else:
            print("Unkown instruction!")
            exit()

for line_nr in range(len(instructions)):
    orig_instruction = instructions[line_nr]
    if orig_instruction[0] == "jmp":
        mod_instruction = ("nop", orig_instruction[1])
    elif orig_instruction[0] == "nop":
        mod_instruction = ("jmp", orig_instruction[1])
    elif orig_instruction[0] == "acc":
        # We don't have to change and test this one
        continue
    else:
        print("Unexpected instruction!")
        exit()
    mod_instructions = instructions.copy()
    mod_instructions[line_nr] = mod_instruction
    result = run_program(mod_instructions)
    if result:
        print("End accumulator value:", result)

