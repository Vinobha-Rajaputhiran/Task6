list1= list(input("Enter the values of list 1: ").split())
list2= list(input("Enter the values of list 2: ").split())
list3= list(input("Enter the values of list 3: ").split())

consolidated_list1= [x for x in list1 if x in list2]

consolidated_list2=[x for x in consolidated_list1 if x in list3]

print("The Duplicate Values in the lists are: ", consolidated_list2)