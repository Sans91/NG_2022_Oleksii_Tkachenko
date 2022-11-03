#user inputs a number which we will be using
userNumber = int(input("enter whole number you want to see interesting thing with\n>>"))

#initial constant number
initialNumber = userNumber

#buffer number to count cycle's number
cycleNumber = 0

#making cycle in cycle to make what it seems to be, a 2d array, where first cycle
#makes rows and second "in" cycle makes columns
while cycleNumber < initialNumber:
    #reinitializing userNumber to make further calculations
    userNumber = initialNumber - cycleNumber
    while userNumber > 0:
        print(userNumber, end=" ")
        userNumber -= 1
    #printing empty input to make another row
    print("")
    cycleNumber += 1