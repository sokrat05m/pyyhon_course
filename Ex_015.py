coins = [1, 1, 1, 1, 1, 0, 1, 0, 0, 0]
count0 = 0
count1 = 0
for i in range (len(coins)):
    if coins [i] == 0:
        count0+=1
    elif coins [i] == 1:
        count1+=1
print(count0, count1)