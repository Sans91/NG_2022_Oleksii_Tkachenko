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
# for key in sorted(dct.keys()):
#     print(f"{key} = {dct[key]}", end = ", ")
print(sorted(dct.items(), key=lambda x: x[0]))
print("\nsorted by value")
print(str(sorted(dct.items(), key=lambda x: x[1])))

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

