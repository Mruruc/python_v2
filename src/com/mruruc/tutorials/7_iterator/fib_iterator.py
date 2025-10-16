class Fib:
    def __init__(self, num):
        self.__num = num
        self.__a, self.__b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__a > self.__num:
            raise StopIteration
        else:
            self.__a, self.__b = self.__b, self.__a + self.__b
            return self.__a
