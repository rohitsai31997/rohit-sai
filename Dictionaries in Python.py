"""Key-Value pairs"""

student = {"name" : "Rohit", "age" : 23, "courses": ['Math', 'Comp Sci']}

#Printing the value of a key
print(student['name'])

#Get method - Returns None when the key doesn't exist unlike above which throws in a stupid error
print(student.get("name"))

#We can give the error msg we like by giving it as the second parameter
print(student.get("names",'Not found'))

student['phone'] = '444-444'
print(student)

#Update method - Useful when we want to update multiple values at once
student.update({'name' : 'Jane', 'age' : 22, 'phone' : '676767'})
print(student)

#Deleting
del student['age']
#We can also use pop method. The adv is , it returns the popped value
age = student.pop('age')
print(student)
print(age)

#Printing the length of the dicctionary
print(len(student))
print(student.keys())
print(student.values())

print(student.items())

#Looping through the keys and values
#Only looping through keys
for key in student:
    print(key)

#To loop through keys and values together, do the following
for key, value in student.items():
    print(key, value)