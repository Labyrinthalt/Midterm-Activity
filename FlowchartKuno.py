my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] # creates a list of numbers from 0 to 9

print("Original list:", my_list) # prints the label "Original list:" followed by the actual list
print("Length of list:", len(my_list)) # it will print 9 because there are 9 numbers (0–9)

y = 1 # initializes a variable y and sets it to 1

for x in range(len(my_list)): # loops through the list using index values (0 up to length-1)
    if x < len(my_list):  # check if x is within the current list length
        if my_list.count(my_list[x]) > 1: # check if the current element is a duplicate
            del my_list[x] # remove the duplicate element
        else:
            y = y + 1  # increment y if the element is unique
    else:
        break # stop the loop if x exceeds the list length

print("The list with unique elements only.")  # print label before showing final list
print(my_list) # print the final list after removing duplicates
