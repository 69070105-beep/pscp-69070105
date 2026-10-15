"""Shorten"""

nums = []
while True:
    num = int(input())
    if num == -1:
        break
    nums.append(num)

if nums:
    result = []
    start = nums[0]
    prev = nums[0]

    for num in nums[1:]:
        if num == prev + 1:
            prev = num
        else:
            if start == prev:
                result.append(str(start))
            else:
                result.append(f"{start}-{prev}")
            start = num
            prev = num

    if start == prev:
        result.append(str(start))
    else:
        result.append(f"{start}-{prev}")

    print(", ".join(result))
