def reverseSwitch(status):
    if status == 0:
        status = 1
    else: 
        status =0
    return status 
    
N = int(input())
switchs = list(map(int, input().split()))
students = int(input())

for _ in range(students):
    sex, num = map(int, input().split())

    if sex == 1:
        for i in range(num-1, N, num):
            switchs[i] =  reverseSwitch(switchs[i])
    elif sex == 2:
        idx = num - 1
        switchs[idx] =  reverseSwitch(switchs[idx])
        left = idx - 1
        right = idx + 1
        while(left >=0 and right < N and switchs[left] == switchs[right]):
            switchs[left] =  reverseSwitch(switchs[left])
            switchs[right] =  reverseSwitch(switchs[right])
            left -=1
            right +=1
        
for i in range(N):
    print(switchs[i], end=' ')
    if (i+1) % 20 == 0:
        print()