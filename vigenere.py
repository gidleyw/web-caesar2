from helpers import alphabet_position, rotate_character
import string

alphabet_list = list(string.ascii_lowercase)

def encrypt(text, key):
    encrpytion_key_list = []
    encrypted_list = []
    e_counter = 0
    for i in key: ### take each letter in encrpytion key and assign alpha value
        encrpytion_key_list.append(alphabet_position(i))

    for char in text: 
        lower_char = char.lower()    
        if lower_char in alphabet_list:
            rot = encrpytion_key_list[e_counter % len(encrpytion_key_list)]
            encrypted_char = rotate_character(char, rot)
            encrypted_list.append(encrypted_char)
            e_counter +=1
        else: 
            encrypted_list.append(char)
    
    encrpyted_return = "".join(encrypted_list)
    return encrpyted_return

def main():
    # your main code (input and print statements)
    text = input("Type a message")
    key = input("Encryption Key:")

if __name__ == "__main__":
    main()