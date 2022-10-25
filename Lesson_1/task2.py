square = 0
n = 0
numberA = ""
numberB = ""
process = ""

#User makes an input number A, while loop for excepting misinput
while(type(numberA) != float):
    print("please input number A")
    try:    #trying to catch misinput
        numberA = float(input())
    except:
        print("you have not entered a number, try again")   

#User makes an input on which process he wants, while loop for excepting misinput
while(process != "/" and process != "*" and process != "+" and process != "-" and process != "square" and process != "sqroot"):
    print("please enter process you want\n(available process: /, *, +, -, square, sqroot)")
    process = input()

#Matching user input
match process:
    case "/":
        while(type(numberB) != float):
            print("please input number B")
            try:
                numberB = float(input())
            except:
                print("you have not entered a number, try again")  
        #trying except the zerodivisionproblem
        try:
            result = numberA / numberB
        except:
            result = "Infinity"
    
    case "+":
        while(type(numberB) != float):
            print("please input number B")
            try:
                numberB = float(input())
            except:
                print("you have not entered a number, try again") 
        result = numberA + numberB
    
    case "-":
        while(type(numberB) != float):
            print("please input number B")
            try:
                numberB = float(input())
            except:
                print("you have not entered a number, try again") 
        result = numberA - numberB
    
    case "*":
        while(type(numberB) != float):
            print("please input number B")
            try:
                numberB = float(input())
            except:
                print("you have not entered a number, try again") 
        result = numberA * numberB    
    
    case "square":
        square = numberA * numberA
    
    case "sqroot":
        #finding whole part of a number by finding square higher than square of our number
        while(square <= numberA):
            n += 1
            square = n * n
        n -= 1 #reverting n to when its not higher than number
        numberB = n
        square = 0 #nullifying variable for next calculation
        
        #finding .1 part of a number by finding square higher than square of our number
        while(square <= numberA):  
            n += 0.1
            square = n * n
        numberB = n - 0.1
        square = 0
        n -= 0.1
        
        #finding .01 part of a number by finding square higher than square of our number
        while(square <= numberA):
            n+=0.01
            square = n * n
        
        #rounding result to .01
        result = round(n, 2)

#output of any result that we get
print(result)