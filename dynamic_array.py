def malloc(size):
    return [None] * size


def realloc(obj, size):
    new_memory = [None] * size
    for i in range(0, obj.get_size(), 1):
        new_memory[i] = obj.get_memory()[i]
    return new_memory


class DynamicArray:

    def __init__(self, size):
        if size <= 0: raise TypeError

        self.__size = size
        self.__memory = malloc(self.__size)
        self.__count = 0

    def add(self, item):
        if self.__size <= self.__count:
            new_size = self.__size + (self.__size // 2) + 1
            new_memory = realloc(self, new_size)

            self.__size = new_size
            del new_size
            del self.__memory
            self.__memory = new_memory
            del new_memory

        self.__memory[self.__count] = item
        self.__count += 1

    def add_front(self, item):
        self.add(item)

        tmp = self.__memory[self.__count - 1]
        for i in range(0, self.__count, 1):
            self.__memory[self.__count - i - 1] = self.__memory[self.__count - i - 2]

        self.__memory[0] = tmp

        del tmp

    def insert(self, index, item):

        if index > self.__count or index < 0: raise ValueError
        if self.__size <= self.__count:
            new_size = self.__size + (self.__size // 2) + 1
            new_memory = realloc(self, new_size)

        for i in range(index, self.__count, 1):
            self.__memory[self.__count - i] = self.__memory[self.__count - i - 1]
        self.__memory[index] = item

    def pop(self, index):
        if index > self.__count or index < 0: raise ValueError

        tmp = self.__memory[index]
        for i in range(index, self.__count, 1):
            self.__memory[i] = self.__memory[i + 1]
        return tmp

    def remove(self, item):
        indx = self.find(item)
        if indx != None:
            self.pop(indx)
        del indx

    def reverse(self):
        for i in range(0, self.__count // 2, 1):
            tmp = self.__memory[i]
            self.__memory[i] = self.__memory[self.__count - i - 1]
            self.__memory[self.__count - i - 1] = tmp

    def empty(self):
        return self.__count == 0

    def clear(self):

        del self.__memory
        self.__memory = malloc(self.__size)
        self.__count = 0
        self.__size = 1

    def find(self, item):
        for i in range(0, self.__count, 1):
            if self.__memory[i] == item:
                return i
        return None

    def count(self, item):
        count = 0

        for i in range(0, self.__count, 1):
            if self.__memory[i] == item:
                count += 1
        return count

    def get_size(self):
        return self.__size

    def get_memory(self):
        return self.__memory

    def __str__(self):
        return f'{self.__memory}'


qwe = DynamicArray(1)
qwe.add(123)
qwe.add(321)
qwe.add(1)
print('После add', qwe)
qwe.add_front(777)
print('После add_front', qwe)
qwe.add_front(555)
print('После add_front', qwe)
qwe.reverse()
print('После reverse', qwe)
qwe.pop(0)
print('После pop', qwe)
print('После find', qwe.find(777))
qwe.remove(777)
print('После remove', qwe)
qwe.insert(1, 0)
print('После insert', qwe)
print('После count ', qwe.count(123))
print('После empty', qwe.empty())
print(qwe.clear())
print('После empty', qwe.empty())
