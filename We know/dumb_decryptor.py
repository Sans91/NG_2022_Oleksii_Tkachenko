number = 0
textList = []
alphabetHigh = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")


def AddNumToArrOfStr(number):
    try:
        textList[number] += element
    except:
        textList.append(element)
    number += 1
    return number
userText = input("input a text to decypher\n>>")
userText = userText.upper()
for element in userText:
    if element in alphabetHigh:
        while(number < 26):
            shiftedNumber = alphabetHigh.index(element) + number
            if shiftedNumber >= 26:
                shiftedNumber %= len(alphabetHigh)
            element = alphabetHigh[shiftedNumber]
            number = AddNumToArrOfStr(number)

    else:
        while(number < 26):
            number = AddNumToArrOfStr(number)

    number = 0

for num in range(26):
    print(f"{num}. {textList[num]}")