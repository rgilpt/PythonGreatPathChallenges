list_courses = "Mechanical", "Computer Science", "Physics"

students = [
    {
        'name': "Rodrigo",
        'surname': "Gil",
        'grade': "7",
        'firstChoice': "Mechanical",
        'secondChoice': "Computer Science"
    },
    {
        'name': "Rodrigo2",
        'surname': "Gil",
        'grade': "7",
        'firstChoice': "Mechanical",
        'secondChoice': "Computer Science"
    }
]

university = {
    'name': "IST",
    'courses': [
        {
            'name': "Mechanical",
            'minimumGrade': 18.4
        },
        {
            'name': "Computer Science",
            'minimumGrade': 16.4
        },
        {
            'name': "Physics",
            'minimumGrade': 18.4
        },
    ]
}


def print_students(my_students):

    for s in my_students:
        print("{} {}".format(s['name'], s['surname']))


def main():


    print_students(students)


if __name__ == '__main__':
    main()
