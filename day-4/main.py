with open('input.txt', 'rt') as f:
    input_data = f.read()

passports = input_data.split('\n\n')
passports_list = []
for passport in passports:
    passport_dir = {}
    for field in passport.split():
        field_name = field.split(':')[0]
        field_value = field.split(':')[1]
        passport_dir[field_name] = field_value
    passports_list.append(passport_dir)

# Now we have interpreted the input data.
invalid_passports = 0
print("Passports:", len(passports_list))
for passport in passports_list:
    check_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passport_invalid = False
    for field in check_fields:
        # A required field is not in the passport.
        if field not in passport:
            passport_invalid = True
            invalid_passports += 1
            break


print("Valid passports:", len(passports_list) - invalid_passports)
        
