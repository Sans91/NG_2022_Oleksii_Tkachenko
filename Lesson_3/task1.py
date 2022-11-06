def AskForNumber(numberName):  #waiting for user input and converting it into a number(float) type
    return float(input(f"please input number {numberName}\n>>"))

def NumberDivision(num1, num2):
     #trying except the zerodivisionproblem
        try:
            return num1 / num2
        except:
            return "Infinity"

def NumberAddition(num1, num2):
    return num1 + num2

def NumberMultiplication(num1, num2):
    return num1 * num2

def NumberSubstraction(num1, num2):
    return num1 - num2

def SquareOfNumber(num1):
    return pow(num1, 2)

def SqrootOfNumber(num1):
    return round(pow(num1, 1/2), 2)

def AskForProcess(): #waiting for process
    return input("please enter process you want\n(available process: /, *, +, -, square, sqroot)\n>>")

def Calculation(processSymbol, num1, num2):
    match processSymbol:
        case "/":
            return NumberDivision(num1, num2)
        
        case "+":
            return NumberAddition(num1, num2)
        
        case "-":
            return NumberSubstraction(num1, num2)
        
        case "*":
            return NumberMultiplication(num1, num2)    
        
        case "square":
            return SquareOfNumber(num1)
        
        case "sqroot":
            return SqrootOfNumber(num1)

print(Calculation(AskForProcess() ,AskForNumber("A"), AskForNumber("B")))