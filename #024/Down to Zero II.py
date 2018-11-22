def populate(n):
    nums = [0, 1, 2, 3, 3] + [None] * (n-4)
    
    for i in range(2, n + 1):
        if (nums[i] is None) or  (nums[i] > nums[i-1] + 1):
            nums[i] = nums[i-1] + 1
        for j in range(1, i + 1):
            if i * j > n:
                break
            if (nums[i * j] is None) or  (nums[i] + 1 < nums[i * j]):
                nums[j * i] = nums[i] + 1
    return nums
Q = int(input().strip())

N = [int(input().strip()) for _ in range(Q)]
max_ = max(N)
p = populate(max_)
for i in N:
    print(p[i])