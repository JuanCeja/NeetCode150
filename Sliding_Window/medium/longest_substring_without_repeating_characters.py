# 
# 
# 
# 
# 

def length_of_longest_substring(s: str) -> int:
    l,r = 0, 1
    seen = {}
    longest_substring = 1
    seen[s[l]] = 0

    while r < len(s):
        if s[r] not in seen:
            seen[s[r]] = r
            r += 1
            longest_substring = max(longest_substring, len(s[l:r]))
        else:
            if seen[s[r]] < l:
                seen[s[r]] = r
                r += 1
                longest_substring = max(longest_substring, len(s[l:r]))
            else:
                l = r
                r += 1

    return longest_substring



print(length_of_longest_substring("zxyzxyz")) # 3
print(length_of_longest_substring("xxxx")) # 1
print(length_of_longest_substring("aab")) # 2