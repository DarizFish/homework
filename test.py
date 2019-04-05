

def changea(a):
    a.append(1)

def b(a):
    changea(a)
    print(a)

b([])