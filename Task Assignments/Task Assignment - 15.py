# Write a python program to read the first five characters from file text.txt.

f = open("text.txt", "r")
print(f.read(5))

# Write a python program to print the number of lines in a file

with open("text.txt", "r") as f:
    x = len(f.readlines())

print("Total lines are:", x)

"""Create a file and store the poem in the file to perform the next questions.
"POEM.txt"
	Ring-a-ring-a-rosies...
Write a python program to open a file 'poem.txt' in read mode and count the number of times the word 'tissue' occurs"""


count = 0
f = open("POEM.txt")
line = f.read()
chars = line.split()
for i in chars:
    if i == "tissue":
        count += 1
print(f"The no of occurence of 'tissue' is:", count)
f.close()

# Write a function to read lines from "poem.txt" and display all those words which has two characters in it.

def Two_words():
    f = open("POEM.txt")
    line = f.read()
    chars = line.split()
    for i in chars:
        if len(i) == 2:
            print(i, end=" ")
    f.close()

print("The words which have two characters in them are :")
Two_words()


# Write a function to read from "poem.txt" and display the lines start with A.

def count_the_starts():
    with open("POEM.txt", "r") as f:
        for line in f:
            if line[0] == "A":
                print(line)
    f.close()

print("The lines which atart with 'A' are :")
count_the_starts()
