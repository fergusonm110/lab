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
