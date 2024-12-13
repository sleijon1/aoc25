import re
import math
_input = open("input.txt").read().split("\n\n")
games = []
for section in _input:
    nums = list(map(int, re.findall(r"(\d+)", section)))
    games.append(((nums[0], nums[1]), (nums[2], nums[3]), (nums[4], nums[5])))




def calculate_tokens(A, B, price):
    #rice = (price[0] + 10000000000000, price[1] + 10000000000000)
    max_A_x, max_A_y = math.ceil(price[0] / A[0]), math.ceil(price[1] / A[1])
    max_B_x, max_B_y = math.ceil(price[0] / B[0]), math.ceil(price[1] / B[1])
    max_hits_A = min(max_A_x, max_A_y)
    max_hits_B = min(max_B_x, max_B_y)
    
    tokens = math.inf
    for hits_A in range(1, max_hits_A):
        for hits_B in range(1, max_hits_B):
            x, y = hits_A * A[0] + hits_B * B[0], hits_A * A[1] + hits_B * B[1]
            if price[0] % x == 0 and price[1] % y == 0:
                tokens = min(tokens, (price[0]/x)*(hits_A*3) + (price[1]/y)*(hits_B))
    if tokens != math.inf:
        return tokens

min_tokens = []
for game in games:
    A, B, price = game
    tokens = calculate_tokens(A, B, price)
    if tokens:
        min_tokens.append(tokens)
    #rint(len(min_tokens))

print(sum(min_tokens))