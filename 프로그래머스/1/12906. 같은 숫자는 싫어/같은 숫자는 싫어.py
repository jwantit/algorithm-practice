def solution(arr):
    answer = []
    
    seen = set()
    prev = None
    for num in arr:
        if num not in seen:
            seen.add(num)
            answer.append(num)
        else: 
            if prev != num:
                answer.append(num)
        prev = num
            
    return answer