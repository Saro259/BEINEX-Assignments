# Write a Python program to calculate the length of a string
str = input("Enter a string")
print(len(str))

'''Print even length words in a string.
Sample String : ''I love coding"
Expected Result : “love, coding”'''

str = "I love python"
s = str.split(" ")
l = list(filter(lambda x: (len(x)%2==0),s))
print(" ".join(l))

'''Write a Python code to remove all characters except a           
Sample String : 'exercises'
Expected Result : 'eee' (Removed all characters except special character : e)'''

def remove_char(str,c):
    str_new = "".join([i for i in str if i==c])
    return str_new
str = 'exercises'
c = 'e'
print(remove_char(str,c))



