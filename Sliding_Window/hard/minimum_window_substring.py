# 
# 
# 
# 
# 
# 
# 
# 

def min_window_substring(s: str, t: str) -> str:
    if len(s) < len(t):
            return ""

    t_count, window = {}, {}
    for i in t:
        t_count[i] = t_count.get(i, 0) + 1
        
    res, res_len = "", float("inf")
    have, need = 0, len(t_count)
    left = 0
    
    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1
        
        if char in t_count and window[char] == t_count[char]:
            have += 1
            
        while have == need:
            if right - left + 1 < res_len:
                res = s[left : right + 1]
                res_len = right - left + 1
                
            removed_char = s[left]
            window[removed_char] -= 1
            
            if removed_char in t_count and window[removed_char] < t_count[removed_char]:
                have -= 1
                
            left += 1
                    
    return res if res_len < float("inf") else ""

print(min_window_substring("OUZODYXAZV", "XYZ")) # "YXAZ"
print(min_window_substring("xyz","xyz")) # "xyz"
print(min_window_substring("x", "xy")) # ""