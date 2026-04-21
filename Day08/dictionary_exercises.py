# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'axel'
dog['color'] = 'brown'
dog['breed'] = 'labrador'
dog['legs'] = 'long'
dog['age'] = 1
print(dog)

# 3. Create a student dictionary and add first_name, last_name, 
# gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name':'lily',
    'last_name':'lily',
    'gender':'male',
    'age':18,
    'is_married':True,
    'skills':['sleeping','eating','gaming'],
    'country':'Underwhere',
    'city':'overwhere',
    'address':{
        'street':'45 Lane',
        'zip_code':'1011'
    }
}
print(student)

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

# 6. Modify the skills values by adding one or two skills
student['skills'].append('showering')
student['skills'].append('singing')
print(student['skills'])

# 7. Get the dictionary keys as a list
student_keys = student.keys()
print(student_keys)

# 8. Get the dictionary values as a list
student_values = student.values()
print(student_values)

# 9. Change the dictionary to a list of tuples using items() method
student_tuples = student.items()
print(student_tuples)

# 10. Delete one of the items in the dictionary
del student['age']
print(student)

# 11. Delete one of the dictionaries
del student