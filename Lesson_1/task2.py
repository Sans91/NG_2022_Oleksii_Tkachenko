#waiting for user input and converting it into a number(float) type
numberA = float(input("please input number A\n>>"))   

numberB = float(input("please input number B\n>>"))
#Matching user input
match input("please enter process you want\n(available process: /, *, +, -, square, sqroot)\n>>"):
    case "/":
        #trying except the zerodivisionproblem
        try:
            result = numberA / numberB
        except:
            result = "Infinity"
    
    case "+":
        result = numberA + numberB
    
    case "-":
        result = numberA - numberB
    
    case "*":
        result = numberA * numberB    
    
    case "square":
        result = pow(numberA, 2)
    
    case "sqroot":
        result = round(pow(numberA, 1/2), 2)

#output of any result that we get
print(result)