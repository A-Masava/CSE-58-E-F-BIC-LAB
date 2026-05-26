nums = input().split()

if len(nums) == 0:
    print(-1)
else:
    nums = list(map(int, nums))
    nums = list(set(nums))

    if len(nums) < 2:
        print(-1)
    else:
        nums.sort()
        print(nums[-2])
