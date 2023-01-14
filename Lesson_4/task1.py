WriteFile = open('PCchars.txt', "w")
y = True

def userInputMenu():
    alphabet = "abcdefghijklmnopqrstuvwxz"
    alphabetOrder = 0
    for key in choiceDict:
        print(f"{alphabet[alphabetOrder]}){key}: {choiceDict[key]}")
        alphabetOrder += 1
        
def choiceFunc(item):
    if choiceDict[item] == "no":
        choiceDict[item] = "yes"
    else:
        choiceDict[item] = "no"

def choiceWrite():
    for key in choiceDict:
                if choiceDict[key] == "yes":
                    match key:
                        case "CPU core count":
                            WriteFile.write(f"CPU: {psutil.cpu_count()} cores\n")
                        case "CPU max frequency":
                            WriteFile.write(f"CPU: {psutil.cpu_freq()[2]} MHz max frequency\n")
                        case "CPU current frequency":
                            WriteFile.write(f"CPU: {psutil.cpu_freq()[0]} MHz current frequency\n")
                        case "CPU family":
                            WriteFile.write(f"CPU: {platform.processor()}\n")
                        case "RAM total":
                            WriteFile.write(f"RAM: {psutil.virtual_memory().total /1024/1024/1024} GB total with OS \n")
                        case "RAM available":
                            WriteFile.write(f"RAM: {psutil.virtual_memory().available /1024/1024/1024} GB available to use \n")
                        case "RAM used":
                            WriteFile.write(f"RAM: {psutil.virtual_memory().used /1024/1024/1024} GB used right now \n") 
                        case "platform":
                            WriteFile.write(f"Platform: {platform.platform()}  \n")
                        case "architecture":
                            WriteFile.write(f"Architecture: {platform.architecture()[0]}, {platform.architecture()[1]} \n")  
                        case "node":
                            WriteFile.write(f"Node: {platform.node()}\n")
import platform, os, socket, sys
import psutil 
choiceDict = {
    "CPU core count": "no",
    "CPU max frequency": "no",
    "CPU current frequency": "no",
    "CPU family": "no",
    "RAM total": "no",
    "RAM available": "no",
    "RAM used": "no",
    "platform": "no",
    "architecture": "no",
    "node": "no"

}

while y != False:
    os.system('cls')
    userInputMenu()
    match input():
        case "a":
            choiceFunc("CPU core count")
        case "b":
            choiceFunc("CPU max frequency")
        case "c":
            choiceFunc("CPU current frequency")
        case "d":
            choiceFunc("CPU family")
        case "e":
            choiceFunc("RAM total")
        case "f":
            choiceFunc("RAM available")
        case "g":
            choiceFunc("RAM used")
        case "h":
            choiceFunc("platform")
        case "i":
            choiceFunc("architecture")
        case "j":
            choiceFunc("node")
        case "y":
            y = False
            choiceWrite()
           
WriteFile.write("Thank you for using this app, more at https://github.com/oleksiy-tkachenko/NG_2022_Oleksii_Tkachenko")
WriteFile.close()
