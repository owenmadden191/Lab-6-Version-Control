# Author: Owen Madden
# Partner: Alejandro Simon
# Lab 6, Group 102

def encoder(password):
    new_password = []
    encoded_password = ''
    for i in range(len(password)):
        new_password.append(int(password[i]))
    for i in range(len(new_password)):
        new_password[i] = new_password[i] + 3
        if new_password[i] > 9:
            new_password[i] = new_password[i] % 9 -1
    str(new_password)
    for i in range(len(new_password)):
        encoded_password += str(new_password[i])
    return encoded_password

if __name__ == '__main__':
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        user_input = int(input(f'Please enter an option: '))
        if user_input == 1:
            password = input('Please enter your password to encode: ')
        if user_input == 2:
            print(f'The encoded password is {encoder(password)}, and the original password is {password}: ')
        if user_input == 3:
            exit()

