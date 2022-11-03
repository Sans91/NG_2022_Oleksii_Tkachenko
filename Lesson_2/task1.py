
dct = {

}
character = 97
buffer = []
string = input("input your string\n>>")

while character < 123:
    characterCount = string.count(chr(character))
    if characterCount != 0:
        print(f"{chr(character)} = {characterCount}", end= " ")
        dct[chr(character)] = characterCount
        buffer.append(dct[chr(character)])
        
    character += 1
buffer.sort()

print("")
for char in buffer:
    print(f"{dct.get(char)} = {char}", end = " ")
    
