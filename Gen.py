import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    """Generate a random password based on user preferences."""
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    # Base character set
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password, filename="passwords.txt"):
    """Save the password to a file."""
    with open(filename, "a") as file:
        file.write(password + "\n")
    print(f"Password saved to {filename}.")

def main():
    print("Welcome to the Password Generator!")
    try:
        # Get user preferences
        length = int(input("Enter password length (default 12): ") or 12)
        use_uppercase = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
        use_numbers = input("Include numbers? (y/n, default y): ").lower() != 'n'
        use_symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'

        # Generate password
        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"\nGenerated Password: {password}")

        # Save password
        save = input("Save this password to a file? (y/n): ").lower()
        if save == 'y':
            save_password(password)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
