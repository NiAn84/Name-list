import random
from time import sleep

def input_names():
    global names_list
    names_list = []
    while True:
        name = input("Type in the names you want in the list, 0 when done: ")
        if len(name) == 0:
            print("Insufficient characters. Please try again.")
        elif name == "0":
            return names_list
        else:
            names_list.append(name)
            global total_names
            total_names = len(names_list)
            global sorted_names_tuple
            sorted_names_list = sorted(names_list)
            sorted_names_tuple = tuple(sorted_names_list)

def the_winner():
    global winner
    winner_number = random.randrange(total_names) - 1
    winner = sorted_names_tuple[winner_number]


def main():
    input_names()
    print("-" * 40, "\nThe names in the list are:")
    for n in sorted_names_tuple:
        print(n)
    print("-" * 40, "\n\nIt is", total_names, "names in the list\n")
    print("And the winner is:")
    sleep(1)
    print("Drumroll...")
    sleep(2)
    print("#" * 50)
    sleep(3)
    the_winner()
    print(f"\nCongratulations {winner}!!!\n")
    print("#" * 50)



if __name__ == '__main__':
    main()