result = ""
userText = input("input a text to decypher\n>>")

numberOfShifts = int(input("input for how much you want it to shift\n>>"))
#loop for each element of string
for element in userText:
    characterCode = ord(element)
    #if A-Z characterCode
    if characterCode >= 65 and characterCode <= 90:
            #shifting a character by user number
            characterCode = characterCode + numberOfShifts
            #buf if its higher than Z
            while characterCode > 90:
                #count by how higher
                outOfBoundsValue = characterCode % 90
                #add it to characterCode 
                characterCode = 64 + outOfBoundsValue 
            element = chr(characterCode)  
    #if a-z characterCode  
    if characterCode >= 97 and characterCode <= 122:
            characterCode = characterCode + numberOfShifts
            while characterCode >= 123:
                outOfBoundsValue = characterCode % 123
                characterCode = 97 + outOfBoundsValue 
            element = chr(characterCode)    

    #adding characters step by step to make a text with shifted characters
    result += element
    
print(result)