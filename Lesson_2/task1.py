characterCountDictionary={}
#user input
userText = input("input your string\n>>")

#using set() to make a set of unique characters 
charSet = set(userText)
#for every character in charSet we add a pair of char:count to dictionary
for char in charSet:
   characterCountDictionary[char] = userText.count(char)
   
#sorting dictionary by keys, using sorted(item, key=), items[0] is key in dictionary.items list
print(f"sorted by character:\n{sorted(characterCountDictionary.items(), key=lambda items: items[0])}")
#sorting dictionary by values, using sorted(item, key=), items[1] is value in dictionary.items list
print(f"sorted by value:\n{sorted(characterCountDictionary.items(), key=lambda items: items[1])}")