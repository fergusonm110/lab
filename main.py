


# encodes password
def encode(password):
    encoder = []
    encoder = list(password)
    for i in range(0, len(encoder)):
        # adds three to each value
        encoder[i] = int(encoder[i])
        encoder[i] = encoder[i] + 3
    password = "".join(str(i) for i in encoder)
    return password

# displays menu
def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    
def decode(password):
    return ''.join([str(int(num)-3) for num in password])

def main():

    password = ''
    
    while True:
        menu()
        print("Please enter an option:")
        menuselect = int(input())
        if menuselect == 1:
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print(password)
            print("Your password has been encoded and stored!\n")
        elif menuselect == 2:
            encoded = password
            password = decode(password)
            print(f"The encoded password is {encoded}, and the original password is {password}.")
        elif menuselect == 3:
            break


if __name__ == '__main__': 
    main()


    """
    password = ''


# encodes password
def encode(password):
    encoder = []
    password = input()
    encoder = list(password)
    for i in range(0, len(encoder)):
        # adds three to each value
        encoder[i] = int(encoder[i])
        encoder[i] = encoder[i] + 3
    password = str(encoder)
    return password


def main():
    # displays menu
    def menu():
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")

    while True:
        menu()
        print("Please enter an option:")
        menuselect = int(input())
        if menuselect == 1:
            print("Please enter your password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!\n")
        if menuselect == 3:
            break


if __name__ == '__main__': main()
    """