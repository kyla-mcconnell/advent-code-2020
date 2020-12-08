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
                contains = [(int(contains.split(" ")[0]), contains.split(" ")[1] + " "  + contains.split(" ")[2])]
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
    total_bags = {} 
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



# --- Day 7: Handy Haversacks ---

# You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

# Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

# For example, consider the following rules:

# light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

# You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

# In the above rules, the following options would be available to you:

# A bright white bag, which can hold your shiny gold bag directly.
# A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
# A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
# So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

# How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

# Your puzzle answer was 248.

# --- Part Two ---

# It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

# Consider again your shiny gold bag and the rules from the above example:

# faded blue bags contain 0 other bags.
# dotted black bags contain 0 other bags.
# vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
# dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
# So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

# Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

# Here's another example:

# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.
# In this example, a single shiny gold bag must contain 126 other bags.

# How many individual bags are required inside your single shiny gold bag?

# Your puzzle answer was 57281.

# Both parts of this puzzle are complete! They provide two gold stars: **