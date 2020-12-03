#Challenge 1: Given the input list, find the two numbers that sum to 2020 and return their product.

with open("data/input1.txt", "r") as f:
    all_numbers = []
    for line in f.readlines():
        num1 = int(line.strip())
        all_numbers.append(num1)
        if 2020 - num1 in all_numbers:
            num2 = 2020-num1
            print(f'Part 1: The two numbers that sum to 2020 are {num1} and {num2}. The product is {num1*num2}.')

#Challenge 2: Given the same input list, find three numbers that sum to 2020 and return their product.
        leftover = 2020-num1
        for num2_p2 in all_numbers:
            if leftover - num2_p2 in all_numbers:
                num3_p2 = leftover - num2_p2
                print(f'Part 2: The three numbers that sum to 2020 are {num1}, {num2_p2} and {num3_p2}. The product is {num1*num2_p2*num3_p2}.')
                break