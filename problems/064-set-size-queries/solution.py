import heapq
s = list()
heapq.heapify(s)
c = int(input())
for i in range(c):
    q = input()
    if q == "?":
        print(len(s))
    else:
        num = int(q.split()[1])
        if num not in s:
            heapq.heappush(s, num)
