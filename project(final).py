import random 
my_list = ["Tom", "Bill", "Josh", "David", "Ali", "Robert", "Johnny", "Danny", "Ethan", "james", "Alex", "lilly", "Selena", "Emma", "olivia", "Ava", "Mia", "Emily", "Spohia", "Michelle"]
gsize = input("How big do you want your group to be")
def cgroups(size,list):
    random.shuffle(list)
    if size == "2":
            print(list[0], list[1])
            print(list[2], list[3])
            print(list[4], list[5])
            print(list[6], list[7])
            print(list[8], list[9])
            print(list[10], list[11])
            print(list[12], list[13])
            print(list[14], list[15])
            print(list[16], list[17])
            print(list[18], list[19])
    
    if size == "4":
            print(list[0], list[1],list[2], list[3])
            print(list[4], list[5],list[6], list[7])
            print(list[8], list[9],list[10], list[11])
            print(list[12], list[13],list[14], list[15])
            print(list[16], list[17],list[18], list[19])
            
    if size == "5":
            print(list[0], list[1],list[2], list[3], list[4])
            print(list[5], list[6],list[7], list[8], list[9])
            print(list[10], list[11],list[12], list[13], list[14])
            print(list[15], list[16],list[17], list[18], list[19])
            
    if size == "10":
            print(list[0], list[1],list[2], list[3], list[4], list[5], list[6],list[7], list[8], list[9])
            print(list[10], list[11],list[12], list[13], list[14], list[15], list[16],list[17], list[18], list[19])
            
          
    
newlist = cgroups(gsize,my_list)
print (newlist)