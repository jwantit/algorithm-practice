N, M = map(int, input().split())
mp1 = {}
mp2 = {}

for i in range(1, N+1):
    s = input()
    mp1[i] = s
    mp2[s] = i

for _ in range(M):
    cmd = input()
    
    if cmd.isdigit():
        print(mp1[int(cmd)])
    else: 
        print(mp2[cmd])