##### Creating a Custom Function :

def minutes_to_hours(minutes,seconds):
    hours = minutes / 60 + seconds / 3600
    return hours

print(minutes_to_hours(70,300))
#print(type(minutes_to_hours(70)))
#print(seconds_to_hours(7200))


################################################
#### Defining a function with default paramters

def seconds_to_hours(seconds,minutes=70):
    hours = minutes / 60 + seconds / 3600
    return hours


print(seconds_to_hours(300)) # this will call seconds_to_hours function with only seconds as input param. The minutes will be taken as default.


print(seconds_to_hours(300,200)) # this will call seconds_to_hours function with both secnods and minutes as input param. the action will be taken.
