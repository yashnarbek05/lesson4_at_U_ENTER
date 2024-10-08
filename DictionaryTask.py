

students = {
    'student_name': 'Dilshod',
    'grade': 3,
    'university': "O'zmu"
}

print(students)

print("grade:", students['grade'])

students['sport'] = 'football'

print(students)

students.pop('sport')

print("modified:", students)

del students['grade']

print("modified:", students)