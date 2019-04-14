def ALPHA_STRING():
    return "abcdefghijklmnopqrstuvwxyz"

def isupper(letter):
    alpha = ALPHA_STRING()
    if letter not in alpha:
        return True
    else:
        return False

def alphabet_position(letter):
    """receives a letter (that is, a string with only one alphabetic character) and returns the 0-based numerical position of that letter within the alphabet"""
    alpha = ALPHA_STRING()
    low_ltr = letter.lower()
    idx = alpha.index(low_ltr)
    return idx

def rotate_character(char, rot):
    """receives a character char (that is, a string of length 1), and an integer rot. Your function should return a new string of length 1, the result of rotating char by rot number of places to the right."""
    alpha = ALPHA_STRING()
    
    low_ltr = char.lower()
    length = len(alpha)
    
    new_position = (alpha.index(low_ltr) + rot) % length
    new_char = alpha[new_position]
    
    if isupper(char):
        return new_char.upper()
    else:
        return new_char