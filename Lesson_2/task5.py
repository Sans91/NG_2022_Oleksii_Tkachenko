#asking for user input and then making list from it by splitting
userList = input("enter numbers to the programm\n>>").split(", ")

#initializing var so it can be used for calculations
sumOtherNumbers = 0

#converting every number in list into int type
#using userList.index(element) to show programm
#where to put the converted element
for element in userList:
    userList[userList.index(element)] = int(element)
#sorting list from min to max number
userList.sort()

#assigning the last element of sorted list, which is max
maxNumber = userList[-1]
#removing max number from list, for further calculations
userList.pop(-1)

#assigning the first element of sorted list, which is min
minNumber = userList[0]
#removing min number from list for further calculations
userList.pop(0)

#calculating the sum of all remaining elements in list
for element in userList:
    sumOtherNumbers += element

#(there are three separate prints for shorter code)
#outputting the maximum, minimum, and sum of all remaining numbers
print(f"the maximum number is {maxNumber}")
print(f"the minimum number is {minNumber}")
print(f"the sum of all other numbers is {sumOtherNumbers}")