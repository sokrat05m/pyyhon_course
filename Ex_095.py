def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.remove(val)
        else:
            i += 1
    length = len(nums)
    return length

