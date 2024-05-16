import string
import random

def generate_password(length, include_digits=True, include_punctuation=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter the desired length of the password: "))
    
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'
    
    password = generate_password(length, include_digits, include_punctuation)
    print("Generated password:", password)

if __name__ == "__main__":
    main()