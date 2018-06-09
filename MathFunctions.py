def Add(a, b):
    return a + b

def Subtract(a, b):
    return a - b;

def Multiply(a, b):
    return a * b

def Divide(a, b):
    return a / b

def AddMultipleArgs(args):
    returnValue = 0
    for number in args:
        returnValue += number
    return returnValue