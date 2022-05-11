
students_school = [
        {'name': 'Blake', 'surname': 'Wilson', 'grade': 6.4, 'firstChoice': 'Computer Science', 'secondChoice': 'Chemistry Engineer'},
        {'name': 'Wade', 'surname': 'Johnson', 'grade': 4.7, 'firstChoice': 'Computer Science', 'secondChoice': 'Chemistry Engineer'},
        {'name': 'Zayne', 'surname': 'Davis', 'grade': 6.8, 'firstChoice': 'Mechanical Engineer', 'secondChoice': 'Computer Science'},
        {'name': 'Hank', 'surname': 'Gonzales', 'grade': 6.8, 'firstChoice': 'Chemistry Engineer', 'secondChoice': 'Computer Science'},
        {'name': 'Thomas', 'surname': 'Clark', 'grade': 5.8, 'firstChoice': 'Electric Engineer', 'secondChoice': 'Computer Science'},
        {'name': 'Scott', 'surname': 'Harris', 'grade': 6.3, 'firstChoice': 'Electric Engineer', 'secondChoice': 'Computer Science'},
        {'name': 'Cade', 'surname': 'Nelson', 'grade': 5.8, 'firstChoice': 'Computer Science', 'secondChoice': 'Mechanical Engineer'},
    ]

university = {
    'students': students_school,
    'grade_range': 20,
    'course': [
        {'name': 'Computer Science', 'minimum grade': 16.5},
        {'name': 'Mechanical Engineer', 'minimum grade': 18},
        {'name': 'Electric Engineer', 'minimum grade': 16.5},
        {'name': 'Chemistry Engineer', 'minimum grade': 16.8},
    ]

}


def print_all_students(list_students):
    for s in list_students:
        print("{} {}".format(s["name"], s["surname"]))



def main():
    print_all_students(students_school)

if __name__ == '__main__':
    main()