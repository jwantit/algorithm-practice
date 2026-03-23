N = int(input())
arr = list(map(int, input().split()))

max_num = max(arr)
result = 0
for num in arr :
    result += (num / max_num) * 100

print(result / N)