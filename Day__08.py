#Day 8





dog = {}

print(dog)





dog = {'color', 'breed', 'legs', 'age'}

print (dog)





student = {

    'first_name': 'Abdulrazak',

    'last_name': 'Auwal',

    'gender': 'Male',

    'age': 24,

    'marital_status': 'single',

    'skills': ['Python', 'Data Science', 'Web development'],

    'country': 'Nigeria',

    'city': 'Zaria',

    'address': '7 Tudun yola'

}

print(student)





students_length = len(student)

print(students_length)





skills = student['skills']

print(skills)

print(type(skills))





student['skills'] = 'Data Visualization', 'SQL'

print(student['skills'])





student_keys = list(student.keys())

print(student_keys)





student_values = list(student.values())

print(student_values)





student_list = list(student.items())

print(student_list)





del student['address']

print(student)





del dog
