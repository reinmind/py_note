# read file as text or binary

def f1():
    textFile = open('f1.txt', 'rt')
    text = textFile.readline()
    print(text)

    binFile = open('f1.txt', 'rb')
    bin = binFile.readline()
    print(bin)
