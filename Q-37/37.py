count = int(input())
sizes = input()
sizes = list(map(lambda x: int(x), sizes.split()))
final_size = max(sizes)
sizes.remove(final_size)
full_size = sum(sizes)
mid_size = 0
for size in sizes:
    if full_size - size == final_size:
        mid_size = size
print(f"{mid_size} {final_size}")