# Write a Python program to merge two Python dictionaries.
student = {'Name':'Asha', 'Age': '22', 'Grade':'A'}
student1 = {'Name1': 'sanjana', 'Age1': '23', 'Grade1': 'B'}
student.update(student1)
print(student)

# Write a Python program to get dictionary keys as a list
fruits = {'apples': 1, 'pear': 3, 'blueberry': 40}
print(fruits['apples'])
print(fruits.get('apples'))

'''Write a Python program to print a dictionary where the keys are numbers 
between 1 and 15 (both included) and the values are the square of the keys'''
diction = {}
for k in range(1,16):
    diction[k] = k**2
print(diction)

# Write a Python program to sum all the items in a dictionary.
dic = {'a': 150, 'b':250, 'c':350}
print(sum(dic.values()))

# Write a Python program to multiply all the items in a dictionary.
dic = {'a': 150, 'b':250, 'c':350}
m = 1
for i in dic:
    m = m* dic[i]
print(m)

# Write a Python program to get the maximum and minimum values of a dictionary
dic = {'a': 150, 'b':250, 'c':350}
print(max(dic.values()))
print(min(dic.values()))

# Write a Python program to Delete a list of keys from a dictionary
info = {
    'name': 'Saro',
    'rollno': '177',
    'age': '23',
    'gender': 'female',
    'city': 'chennai'
}
keys = ['gender', 'city']
for k in keys:
    info.pop(k, None)
print(info)

'''Create a function that takes a string and returns a dictionary where keys are letters, 
and values are the number of times each letter appears in the string'''
def dic_create(str):
    dic = {}
    for i in str:
        k = dic.keys()
        if i in k:
            dic[i]+=1
        else:
            dic[i]=1
    return dic
print(dic_create('doobydobap'))
