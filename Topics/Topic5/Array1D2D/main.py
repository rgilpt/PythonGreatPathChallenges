
matrix = [[0, 1, 2, 3],
          [4, 5, 6, 7]]

height = 2
width = 4


def transform1d(array_2d):
    new_array = []
    for h in array_2d:
        for w in h:
            new_array.append(w)

    return new_array


def value_2d_coord(array_1d, y, x, my_width):
    index = y * my_width + x
    print(index)
    return array_1d[index]


def main():
    print(matrix)

    print(matrix[1][3])

    new_array = transform1d(matrix)

    print(new_array)

    print(value_2d_coord(new_array, 1, 3, width))

    



if __name__ == '__main__':
    main()