# Syed Jawed

# password encoder
def encoder(password):
    new = ''
    for i in password:
        data = ((int(i) + 3) % 10)
        new += data
    return new

# password decoder
def decoder(password):
    s_to_int = [(int(i) - 3) % 10 for i in passwd]
    out = [str(i) for i in s_to_int]
    out_1 = "".join(out)
    return out_1


def main():
    while True:
        # print all the menu options
        print('\nRLE Menu')
        print('-' * 13)
        print('1. Encode\n2. Decode\n3. Quit')
        # Prompt user for menu option
        option = int(input("\nPlease enter an option: "))
        # option 1, 2 ,3
        if option == 1:
            password = input('Please enter your password to encode: ')
            new = encoder(password)
            print('Your password has been encoded and stored!')
            pass
        elif option == 2:
            old = decoder(password)
            print('The encoded password is', new, 'and the original password is', old'.')
            pass
        elif option == 3:
            break

if __name__ == '__main__':
    main()
