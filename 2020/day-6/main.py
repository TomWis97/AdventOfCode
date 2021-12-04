with open('input.txt', 'rt') as f:
    input_data = f.read()

groups = input_data.split('\n\n')

total_yes = 0

for group in groups:
    answers_found = []
    for answers in group.split('\n'):
        # Single line of characters.
        for question in answers.strip():
            # Single character
            if not question in answers_found:
                answers_found.append(question)
    total_yes += len(answers_found)

print("Sum of counts:", total_yes)
