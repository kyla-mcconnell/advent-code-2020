#Challenge 1: Given the list of passwords and their restrictions (how many instances of each letter must appear), return the number of valid passwords

with open("data/input2.txt", "r") as f:
    acceptable_passwords = 0
    acceptable_p2 = 0
    for line in f.readlines():
        num1, num2 = line.split()[0].split("-")
        letter = line.split()[1][0]
        password = line.split()[2]
        if password.count(letter) >= int(num1) and password.count(letter) <= int(num2):
            acceptable_passwords += 1

#Challenge 2: Given the list of passwords and their restrictions (WHERE each letter should appear -- at one of the two indices), return the number of valid passwords
        index1 = password[int(num1) - 1] == letter
        try:
            index2 = password[int(num2) - 1] == letter
        except IndexError:
            index2 = False
        if index1 + index2 == 1:
            acceptable_p2 += 1
  
print(f'Part 1: The number of acceptable passwords is {acceptable_passwords} if you count the number of letters.')
print(f'Part 2: The number of acceptable passwords is {acceptable_p2} if you look at index positions.')