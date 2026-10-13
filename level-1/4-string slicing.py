my_variable = "Python"

# Start at index 1 and end at index 4 (non-inclusive).
print(my_variable[1:4])  # 'yth'

# Start at index 3 and include every character until you reach the end of the string.
print(my_variable[3:])  # 'hon'

# Start at index 0 and end at index 4 (not inclusive).
print(my_variable[:4])  # 'Pyth'

# Get a reversed copy of the string.
print(my_variable[::-1])  # 'nohtyP'

# Get a reversed copy of the string including every other character.
print(my_variable[::-2])  # 'nhy'

# Start at index 1 and end at index 4 (non-inclusive) including every other character.
print(my_variable[1:4:2])  # 'yh'

print(my_variable[:2])
print(my_variable[-2:])
print(my_variable[0:3])# print(my_variable[:3])
print(my_variable[-1::1])

text = "Automation" #"Auto"
print(text[:4])
text = "Playwright" #"wright"
print(text[:-6]) #"Play" using negative indexes
text = "Playwright" #"wright"
print(text[-6:])
text = "Selenium" #reverse the entire string.
print(text[::-1])
text = "123456789" #"13579" using a step.
print(text[::2])
text = "BugReport" #extract "Report" using negative indexes
print(text[-6:])
text = "Automation"
print(text[:-8])
text = "Automation"
print(text[-2:])

