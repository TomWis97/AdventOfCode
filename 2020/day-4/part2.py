import re

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
for passport in passports_list:
    check_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    passport_invalid = False
    for field in check_fields:
        # A required field is not in the passport.
        if field not in passport:
            passport_invalid = True
            break
        if field == "byr":
            r = re.compile('^\d{4}$')
            if not r.match(passport["byr"]):
                passport_invalid = True
            if not 1920 <= int(passport["byr"]) <= 2002:
                passport_invalid = True
        elif field == "iyr":
            r = re.compile('^\d{4}$')
            if not r.match(passport["iyr"]):
                passport_invalid = True
            if not 2010 <= int(passport["iyr"]) <= 2020:
                passport_invalid = True
        elif field == "eyr":
            r = re.compile('^\d{4}$')
            if not r.match(passport["eyr"]):
                passport_invalid = True
            if not 2020 <= int(passport["eyr"]) <= 2030:
                passport_invalid = True
        elif field == "hgt":
            r = re.compile('^\d*(cm|in)$')
            if not r.match(passport["hgt"]):
                passport_invalid = True
            else:
                if passport["hgt"].endswith("cm"):
                    if not 150 <= int(passport["hgt"][:-2]) <= 193:
                        passport_invalid = True
                else:
                    if not 59 <= int(passport["hgt"][:-2]) <= 76:
                        passport_invalid = True
        elif field == "hcl":
            r = re.compile('^#[a-f0-9]{6}$')
            if not r.match(passport["hcl"]):
                passport_invalid = True
        elif field == "ecl":
            if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                passport_invalid = True
        elif field == "pid":
            r = re.compile('^\d{9}$')
            if not r.match(passport["pid"]):
                passport_invalid = True
    if passport_invalid:
        invalid_passports += 1

print("Valid passports:", len(passports_list) - invalid_passports)
        
