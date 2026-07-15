# 
# 
# 
# 
# 
# 
# 

def character_replacement(s: str, k: int) -> int:
    count = {}
    res = 0

    l = 0
    max_f = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        max_f = max(max_f, count[s[r]])

        while (r - l + 1) - max_f > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)

    return res

print(character_replacement("XYYX", 2)) # 4
print(character_replacement("AAABABB", 1)) # 5