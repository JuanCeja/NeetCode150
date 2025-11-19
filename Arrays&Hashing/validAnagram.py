# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false

def is_anagram(s: str, t: str) -> bool:
    """"This function checks if both strings are anagrams of each other."""
    if len(s) != len(t): return False

    s_counter = {}
    t_counter = {}

    for i in range(len(s)):
        if s[i] in s_counter:
            s_counter[s[i]] = s_counter[s[i]] + 1
        else: s_counter[s[i]] = 1

    for i in range(len(t)):
        if t[i] in t_counter:
            t_counter[t[i]] = t_counter[t[i]] + 1
        else: t_counter[t[i]] = 1


    for key in s_counter:
        if key not in t_counter:
            return False
        if s_counter[key] != t_counter[key]:
            return False

    return True



print(is_anagram("racecar", "carrace"))
print(is_anagram("jar", "jam"))