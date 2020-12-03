#Challenge 1: Given a pattern of dots and hashtags, figure out how many hashtags you'd hit if you started at 0 and moved right 3 spaces for each line you descended

#Challenge 2: Given a pattern of dots and hashtags, figure out how many hashtags you'd hit if you started at 0 and moved in a variety of given patterns. return the product

with open("data/input3.txt", "r") as f:
    line_counter = 0
    positions = [0, 0, 0, 0, 0]
    hits = {0:0, 1:0, 2:0, 3:0, 4:0} #0: R1, D1 -- 1: R3, D1 -- 2: R5, D1 -- 3: R7, D1 -- 4: R1, D2
    for line in f.readlines():
        line = line.strip()
        for index, position in enumerate(positions):
            if index == 4:
                if line_counter == 0 or line_counter % 2 == 0:
                    if position < len(line):
                        obstacle = line[position]
                    else:
                        position = position - len(line)
                        obstacle = line[position]

                    if obstacle == "#":
                        hits[index] += 1

                    positions[4] = position + 1
                   
            else: 
                if position < len(line):
                    obstacle = line[position]
                else:
                    position = position - len(line)
                    obstacle = line[position]

                if obstacle == "#":
                    hits[index] += 1
            
                if index == 0:
                    positions[0] = position + 1
                elif index == 1:
                    positions[1] = position + 3
                elif index == 2:
                    positions[2] = position + 5
                elif index == 3:
                    positions[3] = position + 7

        line_counter += 1

    print(f'Part 1: The amount of trees hit in a right 3, down 1 pattern is {hits[1]}.')
    print(f'Part 2: The product of the amount of trees hit in the given variety of patterns is {hits[0] * hits[1] * hits[2] * hits[3] * hits[4]}.')