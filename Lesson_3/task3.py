def countTheLetters(letter, inputSet):
    print(f"{letter} = {userInput.count(letter)}")
    inputSet = inputSet[0:-1]
    try:
        countTheLetters(inputSet[-1], inputSet)
    except:
        print("finished")

userInput = input("your string: ")
inputSet = list(set(userInput))
print(list(set(userInput)))
countTheLetters(inputSet[-1], inputSet)