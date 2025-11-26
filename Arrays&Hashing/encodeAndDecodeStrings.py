# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]

def encode (strs: list[str]) -> str:
    
    def encoder (strs: list[str]) -> str:
        return_string = ""
        
        for string in strs:
            return_string += string
            return_string += " "
        return return_string
    
    def decoder (combined_strings: str) -> list[str]:
        return_array = []
        current_string = ""
        
        for char in combined_strings:
            if char == " ":
                return_array.append(current_string)
                current_string = ""
                continue
                
            else: 
                current_string += char
        
        return return_array
    
    
    encoded_strs = encoder(strs)
    
    return decoder(encoded_strs)
    
    
    

print(encode(["neet", "code", "love", "you"]))
print(encode(["we", "say", ":", "yes"]))
