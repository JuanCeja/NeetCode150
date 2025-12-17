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
    
    left = 0
    t_count = {}
    window_count = {}
    
    for i in range(len(t)):
        t_count[t[i]] = t_count.get(t[i], 0) + 1
        window_count[s[i]] = window_count.get(s[i], 0) + 1
        
    if t_count == window_count:
        return s[0:len(t)]
        
    for i in range(len(t), len(s)):
        if s[i] in t_count:
            t_count[t[i]] = t_count.get(t[i]) - 1
            if t_count[t[i]] == 0:
                del t_count[t[i]]
                
        window_count[s[i]] = window_count.get(s[i], 0) + 1
        
        if not t_count:
            while s[left] not in t:
                left += 1
    
    return s[left:i]

print(min_window_substring("OUZODYXAZV", "XYZ")) # "YXAZ"
print(min_window_substring("xyz","xyz")) # "xyz"
print(min_window_substring("x", "xy")) # "xy"