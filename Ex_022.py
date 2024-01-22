arr = [10, 0, 6, 4, 9, 2, 7, 10]
sum = 0
max_sum = sum
for i in range (len(arr)):
    if (i == 0):
        sum = arr[i] + arr[i + 1] + arr[-1]
        if sum > max_sum:
            max_sum = sum
            sum = 0
    elif (i == len(arr) - 1):
        sum = arr[i] + arr[i - 1] + arr [0]
        if sum > max_sum:
            max_sum = sum
            sum = 0
    else:
        sum = arr[i] + arr[i-1] + arr[i+1]
        if sum > max_sum:
            max_sum = sum
            sum = 0

print(max_sum)