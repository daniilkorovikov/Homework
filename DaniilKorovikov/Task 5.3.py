def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, 'r') as file:
        list_of_students = [i.strip().split(',') for i in file.readlines()[1:]]
        for student in list_of_students:
            student[1], student[2] = int(student[1]), float(student[2])
        return [student[0] for student in sorted(list_of_students, reverse=True, key=lambda x: x[2])[:number_of_top_students]]


print(get_top_performers("data/students.csv"))


def sorted_by_age_students(file_path, number_of_top_students=5):
    with open(file_path, 'r') as file, open('data/sorted_by_age.csv', 'w') as out:
        print(file.readline(), file=out)
        list_of_students = [i.strip().split(',') for i in file.readlines()[1:]]
        for student in list_of_students:
            student[1], student[2] = int(student[1]), float(student[2])
        for student in sorted(list_of_students, reverse=True, key=lambda x: x[1]):
            print(*student, sep=',', file=out)


print(sorted_by_age_students("data/students.csv"))