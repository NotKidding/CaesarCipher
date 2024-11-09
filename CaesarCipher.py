import string
import random

chars =''

def encryptCC():
    global chars
    plaintext = input("Enter plaintext: ")
    shift = input("Enter shift value(1-93): ")
    if shift == '':
        shift = random.randint(1, 93)
        print("haha.. Yov've lost the key")
    else:
        shift = int(shift)
    if shift < 1 or shift > 93:
        print("Invalid key. It should be between 1 and 93.")
        return
    shiftedChars = chars[shift:] + chars[:shift]
    cipherText = []
    for char in plaintext:
        if char in chars:
            index = chars.index(char)
            cipherText.append(shiftedChars[index])
        else:
            cipherText.append(char)
    cipherText = ''.join(cipherText)
    print(f"Ciphertext: {cipherText}")
    

def decryptCC():
    global chars
    ciphertext = input("Enetr ciphertext: ")
    shift = input("Enter shift value(1-93): ")
    if shift == '':
        shift = random.randint(1, 93)
        print("it's a random key")
    else:
        shift = int(shift)
    if shift < 1 or shift > 93:
        print("Invalid key. It should be between 1 and 93.")
        return
    shift = -shift
    shiftedChars = chars[shift:] + chars[:shift]
    plainText = []
    for char in ciphertext:
        if char in chars:
            index = chars.index(char)
            plainText.append(shiftedChars[index])
        else:
            plainText.append(char)
    plainText = ''.join(plainText)
    print(f"Plaintext: {plainText}")


def main():
    global plaintext, chars
    chars = list(string.ascii_letters + string.digits + string.punctuation)
    while True:
        print("\nCaesar Cipher")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        choice = input("Enter your choice(1/2/3): ")
        if choice == '1':
            encryptCC()
        elif choice == '2':
            decryptCC()
        elif choice == '3':
            print("Bye..")
            break
        else:
            print("Invalid choice.")
 
 
if __name__ == "__main__":
    main()
