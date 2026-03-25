arr = [n for n in range(1,31)]
for i in range(28):
    num = int(input())
    arr.remove(num)
    
arr.sort()

for x in arr:
    print(x)