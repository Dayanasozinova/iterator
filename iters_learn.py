#
#
# my_list = [None, 1, 16, False, 'qwerty']
#
# for item in my_list:
#     print(item)
#
# my_list_iterator = iter(my_list)
# item = next(my_list_iterator)
# print(item)
# item = next(my_list_iterator)
# print(item)
# item = next(my_list_iterator)
# print(item)
# item = next(my_list_iterator)
# print(item)
# item = next(my_list_iterator)
# print(item)
# item = next(my_list_iterator)
# print(item)


class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.cursor = self.start - 1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == self.end:
            raise StopIteration
        return self.cursor

for i in MyRange(1,10):
    print(i)