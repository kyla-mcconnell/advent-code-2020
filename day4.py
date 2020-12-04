import re

file = "data/input4.txt"

def prepare_pps(filename):
    with open(filename, "r") as f:
        all_pps = []
        current_pp = ""
        for line in f.readlines():
            line = line.strip()
            if line != "":
                current_pp = current_pp + " " + line
            else:
                all_pps.append(current_pp.lstrip())
                current_pp = ""
        all_pps.append(current_pp.lstrip())
        return all_pps

def pp_checker(filename):
    valid_pps = 0
    needed_fields = {'byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'}
    for pp in prepare_pps(filename):
        fields_present = {section.split(":")[0] for section in pp.split(" ")}
        if needed_fields.issubset(fields_present):
            valid_pps +=1
    print(f'The number of passports with all fields is {valid_pps}.')

#Challenge 1: Given passport info, return how many contain all necessary fields
pp_checker(file)

def byr_validator(byr):
    if len(str(byr)) == 4 and int(byr) >= 1920 and int(byr) <= 2002:
        return True

def iyr_validator(iyr):
    if len(str(iyr)) == 4 and int(iyr) >= 2010 and int(iyr) <= 2020:
        return True
        
def eyr_validator(eyr):
    if len(str(eyr)) == 4 and int(eyr) >= 2020 and int(eyr) <= 2030:
        return True

def hgt_validator(hgt):
    if "cm" in hgt:
        height = int(hgt.strip("cm"))
        if height >= 150 and height <= 193:
            return True
    elif "in" in hgt:
        height = int(hgt.strip("in"))
        if height >= 59 and height <= 76:
            return True

def hcl_validator(hcl):
    return re.match("#[a-f0-9]{6}", str(hcl))

def ecl_validator(ecl):
    if str(ecl) in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True

def pid_validator(pid):
    if len(pid) == 9:
        try: 
            pid = int(pid)
            return True
        except ValueError:
            pass

def pp_validator(filename):
    valid_pps = 0
    for pp in prepare_pps(filename):
        pp_dict = {section.split(":")[0]:section.split(":")[1] for section in pp.split(" ")}
        try:
            if byr_validator(pp_dict["byr"]) and iyr_validator(pp_dict["iyr"]) and eyr_validator(pp_dict["eyr"]) and hgt_validator(pp_dict["hgt"]) and hcl_validator(pp_dict["hcl"]) and ecl_validator(pp_dict["ecl"]) and pid_validator(pp_dict["pid"]):
                valid_pps += 1
        except KeyError:
            pass
    print(f'The number of passports where all fields are formatted correctly is {valid_pps}.')



#Challenge 2: Given passport info, return how many contain all necessary fields and have all fields correctly formatted
pp_validator(file)