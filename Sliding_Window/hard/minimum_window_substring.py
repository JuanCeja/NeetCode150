# 
# 
# 
# 
# 
# 
# 
# 

def min_window_substring(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""
    
    t_count, window = {}, {}
    have, need = 0, len(t_count)
    res, res_len = "", float("inf")
    left = 0
        
    for c in t:
        t_count[c] = t_count.get(c, 0) + 1
        
    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1
        
        if window[char] in t_count and window[char] == t_count[char]:
            have =+ 1
            
        while have == need:
            window[left] -= 1
            left += 1
            
            if window[char] < t_count[char]:
                have -= 1
                
            if (right - left + 1) < res_len:
                res = s[left:right]
                res_len = right - left + 1
                
    return res if res_len < float("inf") else ""

print(min_window_substring("OUZODYXAZV", "XYZ")) # "YXAZ"
print(min_window_substring("xyz","xyz")) # "xyz"
print(min_window_substring("x", "xy")) # "xy"