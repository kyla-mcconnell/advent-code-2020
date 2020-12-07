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
                    bag = item.split(" ")[1] + " " + item.split(" ")[2]
                    contains.append(bag)
            elif contains == "no other bags":
                contains = ["None"]
            else: #if there's only one bag
                contains = [contains.split(" ")[1] + " "  + contains.split(" ")[2]]
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
                if bag in values:
                    interior_bags.append(key) #adds any bag that can contain any of the interior bags
     
    for bag in interior_bags: #once all interior bags have been collected, check which bags can contain any of these
        for key, values in all_rules.items():
            if bag in values:
                exterior_bags.append(key)

    return len(set(exterior_bags))

print(bag_finder(file, "shiny gold"))

