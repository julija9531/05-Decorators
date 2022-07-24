from logger import log_decorator


class SampleIterator:

    @log_decorator('logs/SampleIterator.txt')
    def __init__(self, list1):
        self.list1 = list1

    @log_decorator('logs/SampleIterator.txt')
    def __iter__(self):
        self.x1 = 0
        self.x2 = 0
        return self

    @log_decorator('logs/SampleIterator.txt')
    def __next__(self):
        if type(self.list1[self.x1]) != list:
            self.x1 += 1
            if self.x1 >= len(self.list1):
                raise StopIteration
            return self.list1[self.x1 - 1]
        elif self.x2 < len(self.list1[self.x1]):
            self.x2 += 1
            return self.list1[self.x1][self.x2 - 1]
        else:
            self.x1 += 1
            self.x2 = 0
            if self.x1 >= len(self.list1):
                raise StopIteration
            elif (type(self.list1[self.x1]) == list) and (self.x2 <= len(self.list1[self.x1])):
                self.x2 += 1
                return self.list1[self.x1][self.x2 - 1]
            else:
                self.x1 += 1
                if self.x1 >= len(self.list1):
                    raise StopIteration
                return self.list1[self.x1 - 1]

@log_decorator('logs/gen.txt')
def type_list(list_1):
    for item in list_1:
        yield type(item)

@log_decorator('logs/gen.txt')
def gen(list_1):
    while list in type_list(list_1):
        list_2 = []
        for x_1 in list_1:
            if type(x_1) != list:
                list_2.append(x_1)
            else:
                for x_2 in x_1:
                    list_2.append(x_2)
        list_1 = list_2
    for item in list_1:
        yield item


if __name__ == '__main__':

    my_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
    ]

    for i_1 in SampleIterator(my_list):
        print(i_1)

    print('_' * 50)

    my_list2 = [
        ['a', 'b', 'c'],
        ['d', [1, 'D', [34, 'gafds']],'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for i_2 in gen(my_list2):
        print(i_2)

