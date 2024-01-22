nums = [3,2,3]
counter = {}
for i in nums:
    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1
    if max(counter.values()) > len(nums) / 2:
        break
for k, v in counter.items():
    if v == max(counter.values()):
        print(k)

