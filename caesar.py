import string
from helpers import alphabet_position, rotate_character

alphabet_list = list(string.ascii_lowercase) ###makes list of lowercase alphabet 
        
def encrypt(text, rot):
    encrypted_list = []                 ###initialize empty list to add encrypted values to
    for char in text:                   ###iterates through text and runs through encrpytion codes
        encrypted_value = rotate_character(char, rot) ###uses rotate character function to get new encrpyted character 
        encrypted_list.append(encrypted_value)
    encrpyted_return = "".join(encrypted_list)         ###turns encrypted list back into string
    return encrpyted_return

def main():
    # your main code (input and print statements)
    text = input("What message are we encrypting?")
    rot = input("How many letters should we rotate?")

if __name__ == "__main__":
    main()