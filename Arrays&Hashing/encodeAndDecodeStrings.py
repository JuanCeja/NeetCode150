# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]

def encode (strs: list[str]) -> str:
    """Encode array of strings into one string"""
    encoded_string = ""
    
    for s in strs:
        len_of_string = 0
        
        for char in s:
            encoded_string += char
            len_of_string += 1

        encoded_string += f"{len_of_string}"
        encoded_string += "#"
        len_of_string = 0
        
    print (encoded_string)
        
    return decode(encoded_string)


def decode (s: str) -> list[str]:
    
    current_string = ""
    counter = 0
    arr = []
    
    for char in s:
        counter += 1
        
        # num = int(char)
        
        if counter == num:
            arr.append(current_string)
            counter = 0
        else:
            current_string += char
        
    return arr
    

print(encode(["neet", "code", "love", "you"]))
print(encode(["we", "say", ":", "yes"]))
