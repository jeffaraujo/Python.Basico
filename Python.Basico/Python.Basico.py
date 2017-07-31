import sys
from math import sin, cos, radians

def make_dot_string(x):
    return ' ' * int(10 * cos(radians(x)) + 10) + 'o'


for i in range(360):
    s = make_dot_string(1)
    print s


"""multiple line commenting
Example for importance of identation
"""
#Single commenting

def spam():
    eggs = 12
    return eggs

print("abc")


b=True
print(b)
type(b)

print(type(str(12)))


age = input("Entre com a sua idade") 
if age < 15:
    print "Child"
elif age < 30:
    print "Young"
elif age < 45:
    print "Senior"
else:
    print "Old"


range(0, -5, -1)


def loop1():
    sum =0
    for x in range(1, 11):
        sum += x
    print sum

def loop2():
    x = 0
    while (x < 7):

        x += 1
        if x == 3:
            continue
        print x
        if x == 5:
            break
