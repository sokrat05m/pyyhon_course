a = 3
b = 2
c = 3
if (c > a * b):
    print ("no")
elif (c < a and c < b):
    print ("no")
elif (c % a == 0 or c % b == 0):
    print ("yes")
else:
    print ("no")