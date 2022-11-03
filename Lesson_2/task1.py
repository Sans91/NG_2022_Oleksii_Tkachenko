dct = {

}
arr = []
string = input("input your string\n>>")
for char in string:
    arr.append(ord(char))
arr.sort()
for char in arr:
    print(chr(char), end="")

charSet = set(string)
print("")

for char in charSet:
    characterCount = string.count(char)
    dct[char] = characterCount
    print(f"{dct[char]} = {char} ")            

    
