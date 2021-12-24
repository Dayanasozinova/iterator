import datetime
from typing import Any

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


# class DateRange:                             #итератор по клссам
#     def __init__(self, start: datetime.date, end: datetime.date):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         self.interval = datetime.timedelta(days=1)
#         self.cursor = self.start - self.interval
#         return self
#
#     def __next__(self):
#         self.cursor += self.interval
#         if self.cursor == self.end:
#             raise StopIteration
#         return self.cursor
#
#
# for date in DateRange(datetime.date(2021, 9, 1), datetime.date(2021, 9, 12)):
#     print(date)

# class StackItem:
#
#     def __init__(self, value: Any, prev_stack_item: "StackItem" = None):
#         self.value = value
#         self.prev_stack_item = prev_stack_item
# class Stack:
#
#     def __init__(self):
#         self.tail: StackItem = None
#
#     def append(self, value: Any):
#         new_stack_item = StackItem(value, self.tail)
#         self.tail = new_stack_item
#
#     def pop(self) -> Any:
#         value = self.tail.value
#         self.tail = self.tail.prev_stack_item
#         return value
#
#
#     def __iter__(self):
#         self.cursor = StackItem(None, self.tail)
#         return self
#
#     def __next__(self):
#         if self.cursor.prev_stack_item is None:
#             raise StopIteration
#         value = self.cursor.prev_stack_item.value
#         self.cursor = self.cursor.prev_stack_item
#         return value
# my_stack = Stack()
# my_stack.append(2)
# my_stack.append(4)
# my_stack.append(8)
# my_stack.append(False)
# print(my_stack.pop())
# print(my_stack.pop())
#
#
# for item in my_stack:
#     print(item)
#

def my_range(start, end):
    cursor = start
    while cursor != end:
        yield cursor
        cursor += 1

for item in my_range(1, 10):
    print(item) 