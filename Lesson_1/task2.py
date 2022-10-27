square = 0
n = 0
numberA = ""
numberB = ""

#waiting for user input and converting it into a number(float) type
print("please input number A")
numberA = float(input(">>"))   

print("please enter process you want\n(available process: /, *, +, -, square, sqroot)")
#Matching user input
match input(">>"):
    case "/":
        print("please input number B")
        numberB = float(input(">>"))
        #trying except the zerodivisionproblem
        try:
            result = numberA / numberB
        except:
            result = "Infinity"
    
    case "+":
        print("please input number B")
        numberB = float(input(">>"))
        result = numberA + numberB
    
    case "-":
        print("please input number B")
        numberB = float(input(">>"))
        result = numberA - numberB
    
    case "*":
        print("please input number B")
        numberB = float(input(">>"))
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
        n -= 0.1
        numberB = n
        square = 0

        #finding .01 part of a number by finding square higher than square of our number
        while(square <= numberA):
            n+=0.01
            square = n * n
        
        #rounding result to .01
        result = round(n, 2)

#output of any result that we get
print(result)