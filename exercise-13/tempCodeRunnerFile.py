# find output
# input : "the sky is blue"
# output: "blue is sky the"

s = "the sky is blue"
l = s.split() # makes list
print(l)
l = l[::-1]
print(l)
l = ' '.join(l) # makes string
print(type(l))
print(l)