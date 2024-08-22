def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char) - ord('A' if char.isupper() else 'a') + shift_amount) % 26 + ord('A' if char.isupper() else 'a'))
            result += new_char
        else:
            result += char
    
    return result

# Example usage:
name = input("Enter your name: ")
shift =int(input("Enter the shift value : "))
print(" 1: encypt")
print("2: decrypt")
choice=int(input("enter your choice"))
if choice==1:
    ciphertext = caesar_cipher(name, shift)
    print("Encrypted:", ciphertext)
elif choice ==2:
    decrypted_text = caesar_cipher(name,-shift)
    print("Decrypted:", decrypted_text)
else:
    print(" invalid chice")

