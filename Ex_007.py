a = 4
b = 5
c = 6
if (c > a * b):
    print ("no")
elif (c < a and c < b):
    print ("no")
elif (c % a == 0 or c % b == 0):
    print ("yes")
else:
    print ("no")
