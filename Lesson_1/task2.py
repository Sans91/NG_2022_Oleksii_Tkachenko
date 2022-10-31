square = 0
bufferNumber = 0

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
        result = numberA * numberA
    
    case "sqroot":
        #finding root by approximation of other square number
        while(square < numberA):
            bufferNumber+=0.01
            
            #rounding result for no crazy numbers
            bufferNumber = round(bufferNumber, 2)
            
            square = bufferNumber * bufferNumber



        result = bufferNumber

#output of any result that we get
print(result)