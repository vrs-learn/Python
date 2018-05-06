def divide(a,b):
    try:
        return a/b
    except: # in this except, all kinds of errors will be returned
        return "Zero division is meaningless"


print(divide(1,0))  # in this case except will catch the error and send a return as "Zero division is meaningless"

#####################################################

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:   # In this particular case, the below return is done only in case of ZeroDivisionError
        return "Zero division is meaningless"

print(divide(1,0))


#######################################################

def divide(a,b):
    try:
        return a/b
    except NameError:   # In this particular case, the below return is done only in case of ZeroDivisionError
        return "Variable not declared which is passed"

print(divide(1,a))
