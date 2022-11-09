textList = []
alphabetHigh = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
alphabetLow = list(map(lambda x: x.lower(), alphabetHigh))

#function that tries to add characters into string in list
#if there are no way to add character in string in list making string in the list
#also return a increased by one number of iterations
def AddNumToArrOfStr(numberOfIter):
    try:
        textList[numberOfIter] += elementShifted
    except:
        textList.append(elementShifted)
    numberOfIter += 1
    return numberOfIter

#waiting for user input and converting the text to uppercase
userText = input("input a text to decypher\n>>")


#loop to shift every letter in userText string
for element in userText:
    numberOfIter = 0
    while(numberOfIter< len(alphabetHigh)):
        #if letter in text are present in alphabet set
        if element in alphabetHigh:
            
            #making it go through 26 variations of text

                
                #making shifted numberOfIterbased on index of letter
                #from text + number of iterations
                shiftedNumber = alphabetHigh.index(element) + numberOfIter
                
                #making it not exceed the alphabetHigh length
                if shiftedNumber >= len(alphabetHigh):
                    shiftedNumber %= len(alphabetHigh)
                
                #assigning shifted letter to shifted element variable
                elementShifted = alphabetHigh[shiftedNumber]

                numberOfIter= AddNumToArrOfStr(numberOfIter)
        elif element in alphabetLow:

                
                #making shifted numberOfIterbased on index of letter
                #from text + number of iterations
                shiftedNumber = alphabetLow.index(element) + numberOfIter
                
                #making it not exceed the alphabetLow length
                if shiftedNumber >= len(alphabetLow):
                    shiftedNumber %= len(alphabetLow)
                
                #assigning shifted letter to shifted element variable
                elementShifted = alphabetLow[shiftedNumber]

                numberOfIter= AddNumToArrOfStr(numberOfIter)
        #else if its a letter that doesn't match the alphabet, don't shift it
        else:
                textList[numberOfIter] += element
                numberOfIter += 1

#printing texts of text list 
for num in range(len(alphabetHigh)):
    print(f"{num}. {textList[num]}")