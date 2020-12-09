f = open("data/input8_TEST.txt", "r")
instruction_input = [line for line in f.read().split("\n") if line != ""]

def command_follower(commands):
    current_value = 0
    index = 0
    commands_visited = set()
    
    while index not in commands_visited and index < len(commands):
        commands_visited.add(index)
        command, number = commands[index].split(" ") #retrieve command and value separately
        number = int(number)
        if command == "acc":
            current_value += number
            index += 1
        elif command == "jmp":
            index += number
        elif command == "nop":
            index += 1

    return current_value

#Part One: Where acc is the only command that adds to the current value, nop jumps 1 and jmp jumps the given number, return the final value before the program enters an infinite loop.
print("Part One: The final value before the program enters an infinite loop is: " + str(command_follower(instruction_input)))

def input_fixer(commands):
    current_value = 0
    index = 0
    problematic_index = "None"
    new_input = commands.copy()

    while problematic_index == "None" and index < len(commands):
        new_input = commands.copy()
        command, number = commands[index].split(" ") #retrieve command and value separately
        number = int(number)
        if command == "acc":
            current_value += number
            index += 1
        elif command == "jmp":
            new_input[index] = "nop " + str(number)
            try:
                number = command_follower(new_input)
                index += number
            except IndexError:
                problematic_index = index
        elif command == "nop":
            new_input[index] = "jmp " + str(number)
            try:
                number = command_follower(new_input)
                index += 1
            except IndexError:
                problematic_index = index

    return new_input

print(command_follower(input_fixer(instruction_input)))

# def re_reader(commands):
#     current_value = 0
#     value = 0
#     index = 0
        
#     while index < len(commands) - 1:
#         command, number = commands[index].split(" ") #retrieve command and value separately
#         number = int(number)
#         value = current_value
#         if command == "acc":
#             current_value += number
#             index += 1
#         elif command == "jmp":
#             index += number
#         elif command == "nop":
#             index += 1

#     return value

# print(re_reader(input_fixer(instruction_input)))


f.close()