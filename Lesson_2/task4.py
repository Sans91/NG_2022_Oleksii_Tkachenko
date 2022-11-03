#asking for user input for further calculations
userNumber = int(input("input a number you want factorial of\n>>"))

#storing initial user number to use it in further calculations
initialNumber = userNumber

#cycling through all numbers that are higher than one 
#and doing factorial calculations
while initialNumber > 1:
    #lowering init number by one for calculations and out of loop condition
    initialNumber -= 1

    #multiplying user number by its initial user number minus number 
    #of current iteration(which was at a line 11)
    userNumber *= initialNumber
#printing factorial to user
print(userNumber)