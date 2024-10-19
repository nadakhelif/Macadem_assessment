import string


def transformation_time(char,s):
    vowels = set('AEIOU')
    time = 0
    is_char_vowel = char in vowels
    for c in s:
        is_c_vowel = c in vowels
        if char == c :
            time += 0  
        elif is_c_vowel and not is_char_vowel:
            time += 1  
        elif not is_c_vowel and is_char_vowel :
            time += 1
        elif is_c_vowel and is_char_vowel:
            time += 2  
        elif not is_c_vowel and not is_char_vowel:
            time += 2
    return time


def transform_string(s: str):
    min_transformation_time = float('inf')
    char = 'A'
    for c in string.ascii_uppercase:
        t = transformation_time(c,s)
        if t < min_transformation_time:
            min_transformation_time = t
            char = c
    return f"{s} -> {char * len(s)}: {min_transformation_time}s"
            

s = input()        
print(transform_string(s))
        
        
    