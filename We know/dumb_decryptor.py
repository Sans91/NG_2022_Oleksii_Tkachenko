textList = []
alphabetLow = "abcdefghijklmnopqrstuvwxyz"
numberOfIter = 0

#waiting for user input
userText = input("input a text to decypher\n>>").lower()

#making it go through 26 variations of text
while(numberOfIter< len(alphabetLow)):
    #loop to shift every letter in userText string
    for element in userText:
        #if letter in text are present in alphabet set
        if element in alphabetLow:
                #making shifted number based on index of letter
                #from text + number of iterations
                shiftedNumber = alphabetLow.index(element) + numberOfIter
                
                #making it not exceed the alphabetLow length
                if shiftedNumber >= len(alphabetLow):
                    shiftedNumber %= len(alphabetLow)
                
                #assigning shifted letter to shifted element variable
                elementShifted = alphabetLow[shiftedNumber]

                #tries to add characters into string in list
                #if there are no way to add character in string in list,
                #its making new string in the list
                try:
                    textList[numberOfIter] += elementShifted
                except:
                    textList.append(elementShifted)
        #else if its a letter that doesn't match the alphabet, don't shift it
        else:
                textList[numberOfIter] += element
    numberOfIter+=1

#printing texts of text list 
for num in range(len(alphabetLow)):
    print(f"{num}. {textList[num]}")