#user types in seconds number
seconds = int(input("Please input the amount of second\n>>"))

#counting minutes, hours and days by using floor division for no floating point
minutes = seconds // 60
hours = minutes // 60
days = hours // 24

#making seconds, minutes and hours not exceed their limit
seconds %= 60
minutes %= 60
hours %= 24

#output calculated time   
print("Days - " + str(days) + "\nHours - " + str(hours) + "\nMinutes - " + str(minutes) + "\nSeconds - " + str(seconds))