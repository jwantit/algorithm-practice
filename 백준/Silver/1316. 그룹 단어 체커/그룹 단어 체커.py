N = int(input())

groupCount = 0
for _ in range(N):
    word = input()
    seen = set()
    
    is_group = True
    prev = ''
    for ch in word:
        if ch not in seen:
            seen.add(ch)
            prev = ch
        else:
            if prev != ch:
                is_group = False
                break
                
    if is_group == True:
            groupCount +=1        

print(groupCount)                