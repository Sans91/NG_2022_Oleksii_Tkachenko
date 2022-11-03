dct = {

}
arr = []
string = input("input your string\n>>")

charSet = set(string)
print("")

for char in charSet:
    characterCount = string.count(char)
    dct[characterCount] = char
dct.keys.sort()
print(f"{dct[characterCount]} = {characterCount} ")            

    
