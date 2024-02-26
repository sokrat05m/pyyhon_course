nums = [0, 0, 1]
length = len(nums)
i = 0
while i < len(nums):
    if nums[i] == 0:
        nums.remove(0)
    else:
        i += 1
print(nums)
nums += [0] * (length - len(nums))
print(nums)
