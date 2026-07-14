# 
# 
# 
# 
# 

def length_of_longest_substring(s: str) -> int:
    l, r = 0, 1
    seen = {}
    longest_substring = 1
    r += 1

    while r < len(s):
        if s[r] in seen:
            if seen[s[r]] <= l:
                seen[s[r]] = r
            else:
                l = r
            r += 1
        else:
            curr_count = len(s[l:r])
            longest_substring = max(longest_substring, curr_count)
            r += 1
            seen[s[r]] = r

    return longest_substring


print(length_of_longest_substring("zxyzxyz")) # 3
print(length_of_longest_substring("xxxx")) # 1