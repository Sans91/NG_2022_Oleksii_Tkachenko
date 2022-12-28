def luhnAlgorithm(bankCardNumber):
    result = 0
    number = 0
    while number < len(bankCardNumber):
        if number % 2 == 0:
            if int(bankCardNumber[number])*2 >= 10:
                result += int(bankCardNumber[number])*2 % 10
                result += 1
            else:
                result += int(bankCardNumber[number])*2
        else:
            result += int(bankCardNumber[number])
        number+=1
    return result
def validCheck(result):
    if result % 10 == 0:
        match bankCardNumber[0]:
            case "2":
                print("mastercard")
            case "4":
                print("visa")
            case "5":
                print("mastercard")
            case "3":
                print("amex")
            case _:
                print("invalid")
    else: 
        print("invalid")    
bankCardNumber = input().replace(" ", "") 
validCheck(luhnAlgorithm(bankCardNumber))
    