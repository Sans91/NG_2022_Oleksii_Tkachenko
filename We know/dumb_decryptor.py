textList = []
alphabetHigh = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")

#function that tries to add characters into string in list
#if there are no way to add character in string in list making string in the list
def AddNumToArrOfStr(numberOfIter):
    try:
        textList[numberOfIter] += element
    except:
        textList.append(element)
    numberOfIter += 1
    return numberOfIter

#waiting for user input and converting the text to uppercase
userText = input("input a text to decypher\n>>")
userText = userText.upper()

#loop to shift every letter in userText string
for element in userText:
    numberOfIter = 0
    #if letter in text are present in alphabet set
    if element in alphabetHigh:
        #making it go through 26 variations of text
        while(numberOfIter< len(alphabetHigh)):
            #making shifted numberOfIterbased on index of letter
            #from text + number of iterations
            shiftedNumber = alphabetHigh.index(element) + numberOfIter
            if shiftedNumber >= len(alphabetHigh):
                shiftedNumber %= len(alphabetHigh)
            element = alphabetHigh[shiftedNumber]
            numberOfIter= AddNumToArrOfStr(numberOfIter)
    else:
        while(numberOfIter< len(alphabetHigh)):
            numberOfIter = AddNumToArrOfStr(numberOfIter)

for num in range(len(alphabetHigh)):
    print(f"{num}. {textList[num]}")