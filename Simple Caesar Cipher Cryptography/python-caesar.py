import string

def caesar_cipher(message, key):
    shift = key % 26
    lower_cipher = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    upper_cipher = string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]
    cipher = str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                           lower_cipher + upper_cipher)
    return message.translate(cipher)


def caesar_decrypt(encrypted_message, key):
    shift = 26 - key % 26
    lower_cipher = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    upper_cipher = string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]
    cipher = str.maketrans(string.ascii_lowercase + string.ascii_uppercase,
                           lower_cipher + upper_cipher)
    return encrypted_message.translate(cipher)


message = 'COMPUTERSCIENCE'
key = 3

encrypted_message = caesar_cipher(message, key)
print(f'Encrypted Message: {encrypted_message}')

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f'Decrypted Message: {decrypted_message}')