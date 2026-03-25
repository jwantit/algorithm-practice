N, M = map(int, input().split())

nums = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    nums[i-1:j] = nums[i-1:j][::-1]
print(*nums)