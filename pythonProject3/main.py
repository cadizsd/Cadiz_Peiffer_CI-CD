class main(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        return self.a + self.b + self.c


if __name__ == '__main__':
    obj = main(1, 2, 3)
    print(obj.add())
