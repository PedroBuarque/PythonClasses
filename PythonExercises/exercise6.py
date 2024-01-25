"""
Make a program that ask the user what time is it, and based on the time inputed by the user, shows the proper salutation

"Good morning 0-11", "Good afternoon 12-17" and "Good evening 18-23"
"""

time = input("Type what time is it (0-23:0-60): ")
time_hour = time[0] + time[1]


try:
    time_hour_int = int(time_hour)
    if time_hour_int <= 11:
        print("Good morning")
    elif time_hour_int > 11 and time_hour_int <= 17:
        print("Good afternoon")
    elif time_hour_int > 17 and time_hour_int <= 23:
        print("Good evening")
    else:
        print('I do not recognized this hour')
except:
    print("You didn't typed a number")