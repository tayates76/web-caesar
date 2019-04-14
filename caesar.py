from helpers import alphabet_position, rotate_character, isupper, ALPHA_STRING

def rotate_string(text, rot):
    """receives as input a string and an integer rot which specifies the rotation amount. Your function should return the result of rotating each letter in the text by rot places to the right"""
    new_text = ""
    alpha = ALPHA_STRING()
    
    for letter in text:
        if (letter.upper() in alpha.upper()) or (letter in alpha):
            new_letter = rotate_character(letter, rot)
            new_text += new_letter
        else:
            new_text += letter     
    return new_text

def main ():
    string = input("Type a message: \n")
    # print()
    # print(string)
    rotate = int(input("Rotate by: \n"))
    # print(rotate)
    print(rotate_string(string, rotate))

if __name__ == "__main__":
    main()