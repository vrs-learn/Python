
## Two type of errors :
# 1. Syntax Errors
# 2. Exception

print(1)
int 9


#####
a = 1
b = "2"
print ( a + b)


###########################
### Exception Handling ###

def divide(a,b):
    try:
        return a/b
    except:
        return "Zero division is meaningless"

print(divide(1,0))  # in this case except will catch the error and send a return as "Zero division is meaningless"
