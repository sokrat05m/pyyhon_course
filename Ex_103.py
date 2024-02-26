height = [2, 3, 4, 5, 18, 17, 6]
l, r = 0, len(height) - 1
amount = 0
max_amount = 0
while l < r:
    amount = (r - l) * min(height[l], height[r])
    max_amount = max(max_amount, amount)
    if height[r] > height[l]:
        l += 1
    else:
        r -= 1

print(max_amount)