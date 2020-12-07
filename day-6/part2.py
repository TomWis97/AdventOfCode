with open('input.txt', 'rt') as f:
    input_data = f.read()

groups = input_data.split('\n\n')

total_yes = 0

for group in groups:
    answers_found = {}
    group_length = 0
    for answers in group.split('\n'):
        if len(answers.strip()) == 0:
            continue
        # Single line of characters.
        group_length += 1
        for question in answers.strip():
            # Single character
            if not question in answers_found:
                answers_found[question] = 1
            else:
                answers_found[question] += 1
    total_group = 0
    for question in answers_found:
        if answers_found[question] == group_length:
            total_group += 1
    total_yes += total_group

print("Sum of counts:", total_yes)
