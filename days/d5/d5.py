from collections import defaultdict
from colored import Fore, Style
order, orders = open("input.txt").read().split("\n\n")
order = order.split("\n")
orders = orders.split("\n")
behind_page = defaultdict(list)
for pair in order:
    n1, n2 = map(int, pair.split("|"))
    behind_page[n1].append(n2)
    
p1, wrong_order = 0, []
for order in orders:
    nums = list(map(int, order.split(',')))
    if all(nums[i+1] in behind_page[nums[i]] for i in range(len(nums)-1)):
        p1 += nums[len(nums)//2]
        continue
    wrong_order.append(nums)
p2 = 0

for nums in wrong_order:
    print("\nSorting", ','.join(map(str, nums)))
    while not all(nums[i+1] in behind_page[nums[i]] for i in range(len(nums)-1)):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] in behind_page[nums[j]]:
                    print(f"Swapping {nums[i]} and {nums[j]}")
                    nums.insert(j, nums.pop(i))
                    print(f"New order: {','.join(map(str, nums[:j]))},{Fore.red}{nums[j]}{Style.reset}{',' if nums[j+1:] else ''}{','.join(map(str, nums[j+1:]))}")
    p2 += nums[len(nums)//2]

print(f"\n{Fore.green}Part 1: {p1}, part 2: {p2}")
