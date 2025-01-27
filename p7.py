set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
#difference_update() 
#method will also keep the items 
#from the first set that are not in the other set, but it will change the original set instead of returning a new set.