import random
import matplotlib.pyplot as plt

list_numbers = []
list_count_numbers = []


def create_random_numbers():
    for i in range(0, 1000):
        new_number = random.randrange(0, 100)
        if new_number in list_numbers:
            n_index = list_numbers.index(new_number)
            list_count_numbers[n_index] += 1
        else:
            list_numbers.append(new_number)
            list_count_numbers.append(1)

def print_numbers_count():
    c = 0
    for i in list_numbers:
        print("{} -> {}".format(i, list_count_numbers[c]))
        c += 1

def main():

    create_random_numbers()
    print_numbers_count()
    print(average(list_count_numbers))
    analysis(list_count_numbers)


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


if __name__ == '__main__':
    main()

