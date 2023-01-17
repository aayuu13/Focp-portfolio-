print('\n')
import sys
import string

# function to decrypt the ciphertext using the key
def decrypt(ciphertext, key):
    original_text = ""
    
    for char in ciphertext:
        if char.isalpha():
            char_code = ord(char)
            char_code -= key
           
            if char.isupper():
                if char_code < ord('A'):
                    char_code += 26
            else:
                if char_code < ord('a'):
                    char_code += 26
            original_text += chr(char_code)
        else:
            original_text += char
    return original_text

# function to perform frequency analysis and find the key
def frequency_analysis(ciphertext):
    letter_count = {}
    
    for letter in string.ascii_lowercase:
        letter_count[letter] = ciphertext.lower().count(letter)
    max_count = max(letter_count.values())
    likely_letter = [letter for letter, count in letter_count.items() if count == max_count]
    key = ord(likely_letter[0]) - ord('e')
    if key < 0:
        key += 26
    return key

#To get the file name from the command line
file_name = sys.argv[1]
try:
    # open the file and read the contents
    with open(file_name, "r") as file:
        ciphertext = file.read()
       
        key = frequency_analysis(ciphertext)
       
        original_text = decrypt(ciphertext, key)
        print(original_text)
except:
    
    print(f"Cannot open {file_name}. Sorry about that.")
