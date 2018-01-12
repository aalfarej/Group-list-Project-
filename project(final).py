import random 
my_list = ["Tom", "Bill", "Josh", "David", "Ali", "Robert", "Johnny", "Danny", "Ethan", "james", "Alex", "lilly", "Selena", "Emma", "olivia", "Ava", "Mia", "Emily", "Spohia"]
gsize = input("How big do you want your group to be ")
def cgroups(size,list):
    random.shuffle(list)
    count = 0 
    if size == "2":
            for i in my_list:
                if count +1 < len(my_list) and count % 2 == 0:
                    print (i, my_list[count +1])
                count += 1
            if len(my_list) % 2 != 0:
                print(my_list[len(my_list) -1])
    
    elif size == "4":
            print(list[0], list[1],list[2], list[3])
            print(list[4], list[5],list[6], list[7])
            print(list[8], list[9],list[10], list[11])
            print(list[12], list[13],list[14], list[15])
            print(list[16], list[17],list[18], list[19])
            
    elif size == "5":
            print(list[0], list[1],list[2], list[3], list[4])
            print(list[5], list[6],list[7], list[8], list[9])
            print(list[10], list[11],list[12], list[13], list[14])
            print(list[15], list[16],list[17], list[18], list[19])
            
    elif size == "10":
            print(list[0], list[1],list[2], list[3], list[4], list[5], list[6],list[7], list[8], list[9])
            print(list[10], list[11],list[12], list[13], list[14], list[15], list[16],list[17], list[18], list[19])
            
    else:
        print("none")
            
    
    
newlist = cgroups(gsize,my_list)

