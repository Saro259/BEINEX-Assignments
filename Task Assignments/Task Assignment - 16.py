#  Write a Python program to find the second smallest element in a list
import math

nums = [2, 14, 5, 6, 12, 15]
f = math.inf
s = math.inf

for i in nums:
    if i < f:
        f = i

for i in nums:
    if i != f and i < s:
        s = i

print(s)

# Write a Python program to merge two dictionaries and combine the values of common keys.
d1 = {'a': 10, 'b':20, 'c': 30}
d2 = {'a': 40, 'b': 20, 'c': 50}
new_d = d2
for i,j in d1.items():
    if i in d2:
        new_d[i] = j + d2[i]
    else:
        new_d[i] = j 
print("New dictionary is :", new_d)

# Write a Python program to find the top N elements with the highest values in a dictionary.
d = {'a': 30, 'b': 15, 'c': 8, 'e': 21, 'd': 4}
N = 3

print("The original dictionary is:", str(d))

res = dict(sorted(d.items(), key = lambda x:x[1], reverse = True) [:N])
print("Top values of the dictionary are:", str(res))

# Write a Python program to check if two lists have any common elements.
list1 = ['a','b', 1, 34]
list2 = ['b', 2, 13, 'e']

print(list1,list2)

common = 0
for v in list1:
    if v in list2:
        common = 1
        break
if common:
    print("There are common values present in both the lists")
else:
    print("No common values present in either lists")

# Write a Python program to find the intersection of two lists.
list1 = [10, 2, 3, 4, 34]
list2 = [11, 23, 4, 56]
print("The intersection of lists:",set(list1+list2))

# Write a Python program to remove empty dictionaries from a list.
l1 = [{'value': 4, 'is': '', 'this': []}, {'This': {}, 'is': 5, 'value': 0}]
res = []
print("The original list:",l1)

for d in l1:
    res.append({k: v for k,v in d.items() if v})
print("Dictionary after dropping empty", res)

# Write a Python program to count the number of occurrences of each word in a given sentence.
str = "She wanted a pet platypus but ended up getting a duck and a ferret instead."
count = dict()
words = str.split()
for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)

# Write a Python program to check if two dictionaries are equal (have the same key-value pairs).
d1 = {'Name': 'asif', 'Age': 5}
d2 = {'Name': 'Saro', 'Age': 23}

print(d1,d2)

if len(d1)==len(d2):
    print("Both dictionaries are equal")
else:
    print("The dictionaries are not equal")

