import random
import matplotlib.pyplot as plt

list_numbers = []
list_unique_numbers = []
list_count_numbers = []


def create_random_numbers():
    for i in range(0, 1000):
        new_number = random.randrange(0, 100)
        list_numbers.append(new_number)


def create_unique_list():
    for n in list_numbers:
        if n not in list_unique_numbers:
            list_unique_numbers.append(n)


def create_count_numbers():
    for n in list_unique_numbers:
        list_count_numbers.append(list_numbers.count(n))

def print_numbers_count():
    c = 0
    for i in list_unique_numbers:
        print("{} -> {}".format(i, list_count_numbers[c]))
        c += 1


def average(list_count):

    average_count = 0

    for c in list_count:
        average_count += c

    return (average_count * 1.0)/(len(list_count)*1.0)


def analysis(list_count):
    x = []
    y = []
    for c in range(1, 20):
        count = list_count.count(c)
        print(count)
        x.append(c)
        y.append(count)

    plt.plot(x, y)
    plt.show()


def main():

    create_random_numbers()
    create_unique_list()
    # list_unique_numbers.sort()
    create_count_numbers()
    print_numbers_count()
    print(average(list_count_numbers))
    analysis(list_count_numbers)


if __name__ == '__main__':
    main()

