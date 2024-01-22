def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    if target > max(nums):
        return len(nums)
    if target < min(nums):
        return 0
    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return guess, mid


nums_1 = [1,3,5, 6]
target_1 = 2
a, b = binary_search(nums_1, target_1)
print(a, b)
