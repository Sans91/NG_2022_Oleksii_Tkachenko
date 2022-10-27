#user types in seconds number
print("Please input the amount of seconds")
time = int(input(">>"))

seconds = time % 60
#converting to int type for no floating point
minutes = int(time / 60)
hours = int(minutes / 60)
days = int(hours / 24)

#making minutes and hours not exceed their limit
if(minutes >= 60):
    minutes %= 60
if(hours >= 24):
    hours %= 24

#output calculated time   
print("Days - " + str(days) + "\nHours - " + str(hours) + "\nMinutes - " + str(minutes) + "\nSeconds - " + str(seconds))