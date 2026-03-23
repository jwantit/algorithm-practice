N = int(input())

for _ in range(N):
    S = input()
    result = 0
    count = 0
    
    for char in S:
        if char == 'O':
            count += 1
            result += count
        else:
            count = 0
    print(result)