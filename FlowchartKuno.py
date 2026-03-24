my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Original list:", my_list)
print("Length of list:", len(my_list))

y = 1

for x in range(len(my_list)):
    if x < len(my_list): 
        if my_list.count(my_list[x]) > 1:
            del my_list[x]
        else:
            y = y + 1
    else:
        break

print("The list with unique elements only.")
print(my_list)