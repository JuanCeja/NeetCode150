# 
# 
# 
# 
# 
# 
# 
# 


def permutation_in_string(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    
    frequency_counter_s1 = {}
    frequency_counter_s2 = {}
    s1_len = len(s1)
    window_size = len(s1)
    
    for i in range(s1_len):
        frequency_counter_s1[s1[i]] = frequency_counter_s1.get(s1[i], 0) + 1
        frequency_counter_s2[s2[i]] = frequency_counter_s2.get(s2[i], 0) + 1

    if frequency_counter_s1 == frequency_counter_s2:
        return True

    for j in range(window_size, len(s2)):
        if s2[j - window_size] in frequency_counter_s2:
            frequency_counter_s2[s2[j - window_size]] -= 1
            if frequency_counter_s2[s2[j - window_size]] == 0:
                del frequency_counter_s2[s2[j - window_size]]
                
        frequency_counter_s2[s2[j]] = frequency_counter_s2.get(s2[j], 0) + 1

        if frequency_counter_s1 == frequency_counter_s2:
            return True

    return False

print(permutation_in_string("abc", "lecabee")) # True
print(permutation_in_string("abc", "lecaabee")) # False