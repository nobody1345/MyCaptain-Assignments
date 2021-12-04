# A python program to print all positive numbers in a range

myList = []
list1 = int(input("Enter the range's lower limit: "))
list2 = int(input("Enter the range's upper limit: "))

print("Positive numbers in the the following range: ")
for i in range(list1, list2):
    if i >= 0:
	    print(i, end = " ")
