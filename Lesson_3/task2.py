vowels = "aeiuo"
consonants = "qwrtpsdfghjklzxcvbnm"
# deletes leters which is chosen by the type arguement(vowels or consonants) by translate()
def ConsVowDeletion(type):
    mytable = userInput.maketrans("","",type)
    print(userInput.translate(mytable))
# prints menu
def MenuOutput():
    print("Menu:\n0) output the menu again\n1) sort the input\n2) count the elements\n3) output vowels or consonants only\n"
    "4) output words from the last to first\n5) output words by their number\n6) input the string again\n"
    "7) exit the program\nTo choose the option enter its number(from 1 to 7)")

work = 1 # a simple variable for cycle
userInput = input("please input the string you want to do operations with: ").lower()
MenuOutput()
while work:
    match input():
        case "0":
            MenuOutput()
        case "1":
            # prints sorted input by their character codes
            print(sorted(userInput))
        case "2":
            # prints the length of input string
            print(len(userInput))
        case "3":
            match input("vowels or consonants?: "):
                case "vowels":
                    ConsVowDeletion(consonants)
                case "consonants":
                    ConsVowDeletion(vowels)
                # if no cases matched print the warning
                case _:
                    print("only \"consonants\" or \"vowels\" can be an answer")
        case "4":
            # for each number in range of words quantity
            for num in range(len(userInput.split())):
                print(userInput.split()[len(userInput.split()) - num - 1])
        case "5":
            print(userInput.split()[int(input(f"enter the number of word you want to see(1 - {len(userInput.split())}): ")) - 1])
        case "6":
            userInput = input("new input: ")
        case "7":
            work = 0
            print("Exiting the program...")