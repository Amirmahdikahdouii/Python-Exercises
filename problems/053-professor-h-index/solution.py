n = int(input())
nums = sorted(list(map(int, input().split())), reverse=True)
h_index = 0
for i in range(n):
    if nums[i] > i:
        h_index += 1
    else: break
print(h_index)