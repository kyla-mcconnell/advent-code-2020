file = "data/input8_TEST.txt"

def command_follower(filename):
    with open(file, "r") as f:
        commands = f.read().split("\n")
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
            else:
                print("ERROR")

        return current_value

#Part One: Where acc is the only command that adds to the current value, nop jumps 1 and jmp jumps the given number, return the final value before the program enters an infinite loop.
print("Part One: The final value before the program enters an infinite loop is: " + str(command_follower(file)))