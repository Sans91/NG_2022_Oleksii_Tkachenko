dct = {

}
arr = []
string = input("input your string\n>>")

charSet = set(string)
print("")
i = 0
for char in charSet:
    characterCount = string.count(char)
    dct[char] = characterCount
for key in sorted(dct.keys()):
    print(f"{key} = {dct[key]}", end = ", ")

print("\nsorted by value")
print(dct.items()[0])
# for char in charSet:
#     for value in sorted(dct.values()):
#         if value == dct[char]:
#             print(f"{char} = {value}", end = " ")
#             charSet.remove(char)
#             break
#         else:
#             charSet.remove(char)
#             charSet.append(char)
#             break
print(sorted(dct.values()))
print("")
