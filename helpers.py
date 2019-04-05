import string

alphabet_list = list(string.ascii_lowercase)

def alphabet_position(letter):
    alphaletter = letter.lower()
    alphabet_pos = alphabet_list.index(alphaletter)
    return alphabet_pos
    
def rotate_character(char, rot):
    new_char = ""
    char_value = 0
    if char.lower() not in alphabet_list:       ####Checks if character is alphabetical character
        new_char = char                         ####If not - return original value and do not run through encryption
    else: 
        char_value = alphabet_position(char)            ###Gets alpha position value -- integer
        new_char_value = (char_value + rot) % 26        ###finds encrpyted character value
        if char in alphabet_list:                       ###Checks if character was originally lowercase or uppercase
            new_char = alphabet_list[new_char_value]    ###If originally lowercase - will return lowercase encryption
        else:                                           ###If originally uppercase - will return uppercase encrpytion
            new_char = alphabet_list[new_char_value].upper()
    
    return new_char