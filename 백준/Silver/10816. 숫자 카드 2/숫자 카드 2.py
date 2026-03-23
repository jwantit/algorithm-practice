from collections import Counter

N = int(input())
cards = list(map(int, input().split()))

count = Counter(cards)

M = int(input())
query = list(map(int, input().split()))

for num in query:
    print(count[num], end=' ')