def lexiographic_smaller_string_comaprision(s1, s2):
  
    if s1 < s2:
        return s1
    else:
        return s2

s1 = "apple"
s2 = "banana"
print(lexiographic_smaller_string_comaprision(s1, s2))  # Output: "apple"