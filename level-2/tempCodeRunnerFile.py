from itertools import cycle
word = "radar"
for i in range(len(word)):
    similar = word[0]==word[-1]
print(similar)

s = "Hello"
func_cycle = cycle([str.upper, str.lower])
for i in range (len(s)):
    char=s[i]
    ret = next(func_cycle)
    print(ret(char), end="")


s = "Buy"
func_cycle = cycle([str.upper, str.lower])
for i in range (len(s)):
    ret = next(func_cycle)

    print(ret(s[i]), end="\n")

from itertools import cycle

food = ["apple", "banana", "cherry"]
food_cycle = cycle(food)

for i in range(len(food)):
    print(f"{i + 1}: {next(food_cycle)}")

things = ["table", "cup", "cherry"]
things_cycle = cycle(things)
for i, item in enumerate(things, start=1):
    print(f"{i}: {item}")




