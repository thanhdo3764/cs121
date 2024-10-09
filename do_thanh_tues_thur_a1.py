import time

def milesToKilo(miles):
    return miles*1.60934

def milesToKiloTest(value, test):
    if milesToKilo(value) == test:
        return True
    else:
        return False

#Calculate x to the power of 3
def builtIn1(x):
    return pow(x,3)

#Convert x to an integer by truncating
def builtIn2(x):
    return int(x)

#Convert x to an integer by rounding
def builtIn3(x):
    return round(x)

#Take the absolute value of x and convert it to a floating point number.
def builtIn4(x):
    return float(abs(x))

print(milesToKiloTest(2,5))
print(builtIn1(4))
print(builtIn2(4.9))
print(builtIn3(4.9))
print(builtIn4(-200))