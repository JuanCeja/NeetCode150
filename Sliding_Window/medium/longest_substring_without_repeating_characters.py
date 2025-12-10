# 
# 
# 
# 
# 

def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    res = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[r])
        res = max(res, r - left + 1)

    return res

print(length_of_longest_substring("zxyzxyz")) # 3
print(length_of_longest_substring("xxxx")) # 1