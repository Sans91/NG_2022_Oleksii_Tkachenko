
buffer = ""
print("input a text to decypher")
a = input(">>")
i = 0
b = [5000]
print("input for how much you want it to shift")
numberOfShifts = int(input(">>"))
for element in a:
    b[i] = element
    c = ord(b[i])
    if c >= 65 and c<= 90:
            c = c + numberOfShifts
            while c > 90:
                d = c % 90
                c = 64 + d
            b[i] = chr(c)  
    if c >= 97 and c<= 122:
            c = c + numberOfShifts
            while c >= 123:
                d = c % 123
                c = 97 + d
            b[i] = chr(c)    
    buffer += b[i]
    
print(buffer)