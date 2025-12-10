# 
# 
# 
# 
# 

def length_of_longest_substring(s: str) -> int:
    left, right = 0, 1    
    counter = 0
    substring_set = set()
    substring_set.add(s[left])

    while right < len(s):
        if s[right] not in substring_set:
            counter += 1
            right += 1
        else:
            left = right + 1
            right += 1
            counter = 1
            substring_set = set()
            
    return counter

print(length_of_longest_substring("zxyzxyz")) # 3
print(length_of_longest_substring("xxxx")) # 1