# Python Loops and Looping Techniques: Beginner to Advanced.
# By: Estefania Cassingena Navone.

word = "hannah"
print(len(word))
is_palindrome = True

for i in range(len(word) // 2):
    left_char = word[i]

    right_char = word[len(word)-1-i]
    # -1 extract indexes, because len=6, but indexes 5. The length counts how many letters there are. The index tells you where a letter is, starting from zero.
    # that line of code right_char = word[len(word)] "see" [6]
    # -i make loop backward, from the end

    if left_char.lower() != right_char.lower():
        is_palindrome = False

print(is_palindrome)

# len(word) = 6
#       -----------------------
#         i   |  len(word)-i-1
#       -----------------------
# 1st:    0   |  6 - 0 - 1 = 5
# 2nd:    1   |  6 - 1 - 1 = 4
# 3rd:    2   |  6 - 2 - 1 = 3

#  h a n n a h
#  0 1 2 3 4 5

# Tests:
# Other palindromes: noon, level.
# Not palindromes: python, javascript.
word = "madam"
for i in range(len(word)//2):
    left = word[i]
    right = word[(len(word)-i-1)]
    print(left,right, [i])
