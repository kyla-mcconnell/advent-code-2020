f = open("data/input8_TEST.txt", "r")
instruction_input = f.read().split("\n")

def command_follower(commands):
    current_value = 0
    index = 0
    commands_visited = set()
    
    while index not in commands_visited:
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

def index_finder(commands):
    current_value = 0
    index = 0
    problematic_index = "None"
    new_input = commands.copy()

    while problematic_index == "None":
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

    return command, number, problematic_index, new_input

def index_fixer(commands):
    command, number, problematic_input, new_input = index_finder(instruction_input)

    return new_input

print(index_fixer(instruction_input))


f.close()