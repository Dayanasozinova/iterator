# -------------1---------------------------------------
nested_list_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:

    def __init__(self, list: list):
        self.index = 0
        self.list = [a for b in list for a in b]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index + 1 > len(self.list):
            raise StopIteration

        self.index += 1

        return self.list[self.index - 1]


for item in FlatIterator(nested_list_1):
    print(item)
# ------------------2-----------------------------------------
nested_list_2 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(nested_list):
    index = 0
    list = [a for b in nested_list for a in b]
    while index != len(list):
        yield list[index]
        index += 1


for item in flat_generator(nested_list_2):
    print(item)
# -------------------3--------не-получилось-подскажите-плиз)))--------------------
# nested_list_3 = [[1, 4, [4, 4, 2, 6, [1, 6, 3, 5], 2, 5], 6],
#                  ['a', 'b', 'c'],
#                  ['d', 'e', [3, 2, 6, 9], 'f'],
#                  [1, 2, None]
#                  ]
#
#
# class FlatIterator_1:
#
#     def __init__(self, list: list):
#         self.index = 0
#         self.list = [sum(l, []) for l in list]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index + 1 > len(self.list):
#             raise StopIteration
#
#         self.index += 1
#
#         return self.list[self.index - 1]
#
#     def get_elements_of_nested_list(self, element):
#         count = 0
#         if isinstance(element, list):
#             for each_element in element:
#                 count += FlatIterator_1.get_elements_of_nested_list(self, each_element)
#         else:
#             count += 1
#         return count
#
#
# # print(FlatIterator_1.get_elements_of_nested_list(nested_list_3))
#
# for item in FlatIterator_1(nested_list_3):
#     print(item)
# # FlatIterator_1.get_elements_of_nested_list(nested_list_3)

