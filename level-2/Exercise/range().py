# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

import sys

sequence = [i for i in range(1, 1001)]
print(sys.getsizeof(sequence))

range_sequence = range(1, 1001)
print(sys.getsizeof(range_sequence))

numbers= []

for i in list(range(1,5)):
    numbers.append(i)
print(numbers)

for i in range(3, 0, -1):
    print(i)

word = "automation"
for i in range(0,len(word), 2):

    print(word[i], i)

word = "radar"
for i in range(len(word)):
    similar = word[0]==word[-1]
print(similar)
