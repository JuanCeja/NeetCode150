# 
# 
# 
# 
# 
# 
# 

def character_replacement(s: str, k: int) -> int:
    count = {}
    left = 0
    res = 0

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        while (r - left + 1) - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1
            
        res = max(res, r - left + 1)

    return res

print(character_replacement("XYYX", 2)) # 4
print(character_replacement("AAABABB", 1)) # 5