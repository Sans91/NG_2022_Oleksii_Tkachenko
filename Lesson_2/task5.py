#asking for user input and then making list from it by splitting
userList = input("enter numbers to the programm\n>>").split(", ")

#converting every number in list into int type
#using userList.index(element) to show programm
#where to put the converted element
for element in userList:
    userList[userList.index(element)] = int(element)
#sorting list from min to max number
userList.sort()

#(there are three separate prints for shorter code)
#outputting the maximum, minimum, and sum of all remaining numbers
print(f"the maximum number is {max(userList)}")
print(f"the minimum number is {min(userList)}")
print(f"the sum of all other numbers is {sum(userList[1:-1])}")