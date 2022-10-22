numberA = ""
numberB = ""
processSymbol = ""

while(type(numberA) != int):
    print("please input number A")
    try:
        numberA = int(input())
    except:
        print("you have not entered a number, try again")        

while(type(numberB) != int):
    print("please input number B")
    try:
        numberB = int(input())
    except:
        print("you have not entered a number, try again")    

while(processSymbol != "/" and processSymbol != "*" and processSymbol != "+" and processSymbol != "-"):
    print("please enter process you want(example: /, *, +, -)")
    processSymbol = input()
    print(type(processSymbol))

match processSymbol:
    case "/":
        result = numberA / numberB
    case "+":
        result = numberA + numberB
    case "-":
        result = numberA - numberB
    case "*":
        result = numberA * numberB                     

print(result)