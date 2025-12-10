# 
# 
# 
# 

def max_profit (prices: list[int]) -> int:
    max_profit = 0
    left, right = 0, 1

    while right < len(prices):
        max_profit = max(prices[right] - prices[left], max_profit)

        if prices[left] < prices[right]:
            right += 1
        else:
            left = right
            right += 1

    return max_profit

print(max_profit([10,1,5,6,7,1])) # 6
print(max_profit([10,8,7,5,2])) # 0