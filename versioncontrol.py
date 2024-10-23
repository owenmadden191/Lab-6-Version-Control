# Author: Owen Madden (main + encoder)
# Partner: Alejandro Simon (decoder + fixes)
# Lab 6, Group 102

# Encoder function
def encode(password):
    encoded = ""
    for digit in password:
        encoded += str((int(digit) + 3) % 10)
    return encoded

# Main function
def main():
    encoded_password = ""
    while True:
        print("\nMenu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("\nPlease enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print("Invalid password. Please enter an 8-digit password containing only numbers.")
        elif option == "2":
            if encoded_password:
                original_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
            else:
                print("No encoded password found. Please encode a password first.")
        elif option == "3":
            break
        else:
            print("Invalid option. Please try again.")

# Decoder function
def decode(encoded_password):
    decoded = ""
    for digit in encoded_password:
        decoded += str((int(digit) - 3) % 10)
    return decoded

if __name__ == "__main__":
    main()
