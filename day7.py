file = "data/input7.txt"

def bag_ruler(filename):
    with open(file, "r") as f:
        all_rules = {}
        for line in f.read().split("\n"):
            main_bag = line.split(" bags")[0] #split the key from the contents
            try:
                contains = line.split("contain ")[1].strip(".") #return the contents, remove trailing period
            except IndexError:
                pass
            
            if "," in contains: #if bag contains two or more items
                inner_bags = [x for x in contains.split(", ")]
                contains = []
                for item in inner_bags:
                    bag = (int(item.split(" ")[0]), item.split(" ")[1] + " " + item.split(" ")[2])
                    contains.append(bag)
            elif contains == "no other bags":
                contains = [(0, "None")]
            elif len(contains.split(" ")) == 4: #if there's only one bag (4 words, sanity check)
                contains = [(int(item.split(" ")[0]), contains.split(" ")[1] + " "  + contains.split(" ")[2])]
            all_rules[main_bag] = contains
        return all_rules #returns dict of exterior bag to all bags that could be inside


def bag_finder(input, bag_type):
    all_rules = bag_ruler(input) #returns dict of all bags and what can be inside them
    interior_bags = [bag_type] #starts out looking for bags that include only the given type
    old_set = []
    exterior_bags = []

    while interior_bags != old_set: #keeps running this loop until nothing new is found
        old_set = interior_bags
        for bag in interior_bags:
            for key, values in all_rules.items():
                for value in values:
                    try: 
                        if bag == value[1]:
                            interior_bags.append(key) #adds any bag that can contain any of the interior bags
                    except TypeError:
                        pass
     
    for bag in interior_bags: #once all interior bags have been collected, check which bags can contain any of these
        for key, values in all_rules.items():
             for value in values:
                try:
                    if bag == value[1]:
                        exterior_bags.append(key)
                except TypeError:
                        pass

    return len(set(exterior_bags))

print("Part One: " + str(bag_finder(file, "shiny gold")) + " bags contain a shiny gold bag.")


def bag_counter(input, bag_type):
    all_rules = bag_ruler(input) #returns dict of all bags and what can be inside them
    total_bags = {bag_type: 0} 
    this_round = [bag_type]
    next_round = []

    while this_round != []:
        for bag_outside in this_round:
            for value in all_rules[bag_outside]:
                bag_inside = value[1]
                number = value[0]
                for x in range(0, number):
                    next_round.append(bag_inside)
                
                if bag_inside in total_bags:
                    total_bags[bag_inside] = total_bags[bag_inside] + number
                else:
                    total_bags[bag_inside] = number
        
        this_round = [x for x in next_round if x != "None"]
        next_round = []
    
    return(sum(total_bags.values()))
    
    

print("Part Two: One shiny gold bag contains " + str(bag_counter(file, "shiny gold")) + " other bags.")

