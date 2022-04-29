import json


def load_data_doctors(filename="doctors.json"):
    data = None
    with open(filename) as f:
        data = json.load(f)

    return data


def load_data_patients(filename="patients.json"):
    data = None
    with open(filename) as f:
        data = json.load(f)

    return data


def load_data():

    data = {
        'doctors': load_data_doctors(),
        'patients': load_data_patients()
    }
    return data


def main():
    my_data = load_data()
    # print(my_data)
    my_doctors = my_data['doctors']
    for d in my_doctors:
        print(d)
    print("Done!")


if __name__ == '__main__':
    main()