class sub(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sub(self):
        return self.a - self.b - self.c

if __name__ == '__main__':
    obj = sub(1, 2, 3)
    print(obj.sub())