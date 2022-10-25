time = ""
#user types in seconds number
while (type(time) != int):
    print("please write amount of seconds")
    try:    #excepting misinput
        time = int(input())
    except:
        print("amount of seconds needs to be a number")
seconds = time % 60
#converting to int type for no floating point
minutes = int(time / 60)
hours = int(minutes / 60)
days = int(hours / 24)

#making minutes hours and days not exceed their limit
if(minutes >= 60):
    minutes %= 60
if(hours >= 24):
    hours %= 24
if(days > 99):
    days = 99

#making every number in a 00 format
if seconds < 10:
    seconds = "0" + str(seconds)
if minutes < 10:
    minutes = "0" + str(minutes)
if hours < 10:
    hours = "0" + str(hours)
if days < 10:
    days = "0" + str(days)

#output calculated time   
print(f"Calculated time DD:HH:MM:SS = {days}:{hours}:{minutes}:{seconds}")