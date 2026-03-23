from collections import Counter

def solution(participant, completion):
    count = Counter(participant)
    
    for name in completion:
        count[name] -= 1
        
    for name in participant:
        if count[name] > 0:
            answer = name
    return answer