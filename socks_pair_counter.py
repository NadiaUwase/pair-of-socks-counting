from collections import Counter


def main():
    # asking the user to input the total number of socks and the list of numbers which are representative of the socks
    # colours

    n = int(input("enter the total number of socks:  "))
    socks = input("enter the colour of each of these socks: ")

    # putting the socks into a list
    socks_pile = []
    socks_pile = [int(item) for item in socks.split()]

    # I used the counter function to count the occurrence of each color(number) in the list which returns a dictionary
    # of
    # color and occurrence

    individual_color_count = Counter(socks_pile)

    # looped through the values in the dictionary to calculate the sum of all identified pairs

    pairs = 0
    for i in individual_color_count.values():
        pairs = pairs + (i // 2)

    print(pairs)


if __name__ == '__main__':
    main()
