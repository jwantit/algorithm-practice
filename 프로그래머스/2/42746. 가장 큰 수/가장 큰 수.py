def solution(numbers):
    arr = list(map(str, numbers))
    arr = sorted(arr, key=lambda x: x*3, reverse=True)
    
    return str(int(''.join(arr)))
    
