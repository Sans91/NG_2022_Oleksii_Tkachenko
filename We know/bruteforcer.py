textList = []
alphabetBoth = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")


number = 0
userText = input("input a text to decypher\n>>")

for element in userText:
    for char in alphabetBoth:
        if element == char:
            while(number < 26):
                shiftedNumber = alphabetBoth.index(char) + number
                if shiftedNumber >= 26:
                    shiftedNumber %= len(alphabetBoth)
                element = alphabetBoth[shiftedNumber]
                try:
                    textList[number] += element
                except:
                    textList.append(element)
                number += 1
        elif element == char:
            number = 26
            while(number < 52):
                shiftedNumber = alphabetBoth.index(char) + number
                if shiftedNumber >= 52:
                    shiftedNumber %= len(alphabetBoth)
                element = alphabetBoth[shiftedNumber]
                try:
                    textList[number] += element
                except:
                    textList.append(element)
                number += 1  
        else:
            try:
                textList[number] += element
            except:
                textList.append(element)
    number = 0

for num in range(26):
    print(f"{num}. {textList[num]}")