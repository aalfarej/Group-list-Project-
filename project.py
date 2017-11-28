import random 
my_list = ["Tom", "Bill", "Josh", "David", "Ali", "Robert", "Johnny", "Danny", "Ethan", "james", "Alex", "lilly", "Selena", "Emma", "olivia", "Ava", "Mia", "Emily", "Spohia", "Michelle"]
gsize = input("How big do you want your group to be")
def cgroups(size,list):
    random.shuffle(list)
    if size == "2":
        return list 
    
newlist = cgroups(gsize,my_list)
