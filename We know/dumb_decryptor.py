
buffer = ""
print("input a text to decypher")
text = input(">>")

print("input for how much you want it to shift")
numberOfShifts = int(input(">>"))
for element in text:
    c = ord(element)
    if c >= 65 and c<= 90:
            c = c + numberOfShifts
            while c > 90:
                d = c % 90
                c = 64 + d
            element = chr(c)  
    if c >= 97 and c<= 122:
            c = c + numberOfShifts
            while c >= 123:
                d = c % 123
                c = 97 + d
            element = chr(c)    
    buffer += element
    
print(buffer)