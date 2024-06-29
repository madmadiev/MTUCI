groupmates = [
{
"name": "Радмила",
"surname": "Кунафина",
"exams": ["ТРТПО", "СОС", "УИРиИ"],
"marks": [4, 3, 5]
},
{
"name": "Константин",
"surname": "Ливчак",
"exams": ["Рад.Безоп.", "МНТ", "НЛ"],
"marks": [4, 5, 4]
},
{
"name": "Светлана",
"surname": "Лисицына",
"exams": ["НЛ", "Ино.Яз", "КНИИР"],
"marks": [4, 5, 5]
},
{
"name": "Виктория",
"surname": "Луцикова",
"exams": ["ТРТПО", "ВвБД", "Программирование"],
"marks": [5, 5, 5]
},
{
"name": "Константин",
"surname": "Маслов",
"exams": ["ИБД", "БвСС", "Нл"],
"marks": [5, 4, 5]
}
]

def filter_students_by_average_mark(students, threshold):
    filtered_students = []
    for student in students:
        average_mark = sum(student["marks"]) / len(student["marks"])
        if average_mark > threshold:
            filtered_students.append(student)
    return filtered_students

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10),u"Средний балл".ljust(30))
    for student in students:
        print(student["name"].ljust(15),student["surname"].ljust(10), str(round(sum(student['marks']) / len(student['marks']),2)).ljust(30))

# Запросить пороговое значение у пользователя
threshold = float(input("Введите пороговое значение среднего балла: "))

# Отфильтровать студентов
filtered_students = filter_students_by_average_mark(groupmates, threshold)

# Вывести отфильтрованных студентов
print("Студенты с средним баллом выше заданного порога:")
print_students(filtered_students)
