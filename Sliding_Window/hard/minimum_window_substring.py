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
    
    count = {}
    window = {}

    for i in range(len(t)):
        count[t[i]] = count.get(t[i], 0) + 1

    need = len(count)
    have = 0
    res = ""
    res_len = float("inf")
    l = 0

    for r in range(len(s)):
        window[s[r]] = window.get(s[r], 0) + 1
        if s[r] in count and window[s[r]] == count[s[r]]:
            have += 1

        while have == need:
            if r - l + 1 < res_len:
                res = s[l:r + 1]
                res_len = r - l + 1

            window[s[l]] -= 1

            if s[l] in count and window[s[l]] < count[s[l]]:
                have -= 1
            
            l += 1

    return res

print(min_window_substring("OUZODYXAZV", "XYZ")) # "YXAZ"
print(min_window_substring("xyz","xyz")) # "xyz"
print(min_window_substring("x", "xy")) # ""