# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Group strings that are anagrams of each other"""
    hashmap = {}

    for s in strs:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1

        key = tuple(count)

        if key in hashmap:
            hashmap[key].append(s)
        else:
            hashmap[key] = [s]

    return list(hashmap.values())


print(group_anagrams(["act","pots","tops","cat","stop","hat"]))
print(group_anagrams(["x"]))
print(group_anagrams([""]))