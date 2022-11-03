#waiting for user input
userInput = input("Write the words you want to see, separated by comma\n>>")

#firstly splitting our input, so it will be array of strings without comma
#(the ", " arguement inside it), then converting this array to set, which will
#remove all repeatable strings in it.
print(set(userInput.split(", ")))