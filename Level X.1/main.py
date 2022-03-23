import random

listlol = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0
}





def main():
    print(listlol)
    for item in listlol.keys():
        listlol[item] = random.randrange(0, 100)
    print(listlol)

numbers = []
numbers_odd = []


def _main():

    for cycle in range(0, 10):

        new_number = random.randint(0, 100)

        numbers.append(new_number)
        print(new_number % 2)
        if new_number % 2 != 0:
            numbers_odd.append(new_number)

    print(numbers)
    print(numbers_odd)


if __name__ == '__main__':
    main()