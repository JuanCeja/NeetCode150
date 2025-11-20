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
    # if len < 2 return strs

    # array we will be returning

    # create an array with 26 0's

    # outer for loop

        # inner for loop

        # create unique array and set it as a value

        # check if unique array exists in hashmap

            # if so push current word to it

        # if not, create unique array as key and current word being the value

    # return array


print(group_anagrams(["act","pots","tops","cat","stop","hat"]))
print(group_anagrams(["x"]))
print(group_anagrams([""]))