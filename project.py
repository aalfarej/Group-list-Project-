import random 
my_list = ["Tom", "Bill", "Josh", "David", "Ali", "Robert", "Johnny", "Danny", "Ethan", "james", "Alex", "lilly", "Selena", "Emma", "olivia", "Ava", "Mia", "Emily", "Spohia", "Michelle"]
gsize = input("How big do you want your group to be")
def cgroups(size,list):
    random.shuffle(list)
    if size == "2":
        count=0
        for i in list:
##         for i in range(len(list)):
            if count < len(list)-1:
                print(list[count],list[count+1])
            count += 1
        return list
    
    
    
newlist = cgroups(gsize,my_list)
print (newlist)
