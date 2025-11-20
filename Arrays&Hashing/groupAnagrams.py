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

    # array we will be returning
    grouped_anagrams = []
    hashmap = {}

    # create an array with 26 0's
    


    # outer for loop
    for current_str in strs:
        arr = [0] * 26
        # inner for loop
        for char in current_str:
        # create unique array and set it as a value
            letter_index = ord(char) - ord('a')
            arr[letter_index] += 1


        # check if unique array exists in hashmap
        my_tuple = tuple(arr)
        
        if my_tuple in hashmap:
            # if so push current word to it
            hashmap[my_tuple].append(current_str)
        else:
            # if not, create unique array as key and current word being the value
            hashmap[my_tuple] = [current_str]


    for value in hashmap.values():
        grouped_anagrams.append(value)

    # return array
    return grouped_anagrams


print(group_anagrams(["act","pots","tops","cat","stop","hat"]))
print(group_anagrams(["x"]))
print(group_anagrams([""]))