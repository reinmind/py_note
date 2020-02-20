# print
def f1():
    print("hello", end='')
    print("world")


# variables
def f2():
    a = 6
    b = 6.3
    c = "str"
    d = 's'
    print(a, b, c, d)
    print(type(a), type(b), type(c), type(d))


# numbers
def f3():
    var = 0x3;
    var1 = 3 + 5.3j
    print(var1, type(var1))


# bool

# comment
# type1
''' 
type2 
'''


# arithmetic

def f4():
    var = 10 // 4
    var1 = 10 ** -1
    var3 = 10 == 3
    print(var3, type(var3))

# logic


def f5():
    var = True
    var1 = False
    print(var1 and var, var1 or True, not var)

# string


def f6():
    # string with paragraph
    str1 = '''
    <p1>e
    <p2>
    <p3>'''
    print(str1 + str(100))
    print(len(str1))