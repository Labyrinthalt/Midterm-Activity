my_list = []  # create an empty list to store numbers

for x in range(1, 10):  # loop through numbers 1 to 9
    my_list.append(x)  # add each number to the list

print("Original list:", my_list)  # print the list before removing duplicates
print("Length of list:", len(my_list))  # print how many elements are in the list

y = 1  # initialize a variable y to 1 (used for tracking, but not necessary here)

for x in range(len(my_list)):  # loop through list indexes
    if x < len(my_list):  # check that the index is still valid
        if my_list.count(my_list[x]) > 1:  # check if the current element is a duplicate
            del my_list[x]  # delete the duplicate element
        else:
            y = y + 1  # increment y if the element is unique
    else:
        break  # stop the loop if x exceeds the current list length

print("The list with unique elements only.")  # print label before showing final list
print(my_list)  # print the list after removing duplicates
