# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false

def is_anagram(s: str, t: str) -> bool:
    """"Check if two strings are anagrams."""
    
    if len(s) != len(t):
        return False
    
    counter = {}

    for char in s:
        counter[char] = counter.get(char, 0) + 1

    for char in t:
        counter[char] = counter.get(char, 0) - 1
        if counter[char] < 0:
            return False
        
    return True

    



print(is_anagram("racecar", "carrace"))
print(is_anagram("jar", "jam"))