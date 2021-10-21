# This function identifies the max number out of two numbers.
def maxFunction(x, y):
    if x > y:
      return x
    else: 
        return y

# This function identifies the max number out of three numbers.
def maxThreeNumbers(x, y, z):
    return maxFunction(x, maxFunction(y,z))

returnVal= maxThreeNumbers(1000,3000,10000)
print((returnVal), "is max number")