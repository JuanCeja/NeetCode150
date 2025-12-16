# 
# 
# 
# 
# 
# 
# 

def character_replacement(s: str, k: int) -> int:
    counter = {}
    longest_repeating_char = 1
    left = 0
    replacements = k

    for char in s:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    most_freq_char = max(counter, key = counter.get)
    
    for r in range(1, len(s)):

        if s[r] == most_freq_char:
            longest_repeating_char = max(r - (left + 1), longest_repeating_char)
        elif s[r] != most_freq_char and replacements > 0:
            longest_repeating_char = max(r - (left + 1), longest_repeating_char)
            replacements -= 1
        else:
            left = r
            replacements = k

    return longest_repeating_char

print(character_replacement("XYYX", 2)) # 4
print(character_replacement("AAABABB", 1)) # 5