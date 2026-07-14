# 
# 
# 
# 

def max_profit (prices: list[int]) -> int:
    l, r = 0, 1
    max_profit = 0

    while r < len(prices):
        profit = prices[r] - prices[l]
        max_profit = max(max_profit, profit)
        
        if prices[l] > prices[r]:
            l = r
        
        r += 1

    return max_profit

print(max_profit([10,1,5,6,7,1])) # 6
print(max_profit([10,8,7,5,2])) # 0