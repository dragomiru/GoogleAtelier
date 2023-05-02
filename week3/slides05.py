"""Example 1"""
# def my_initial_function(msg):
#     print(msg)
#
# def another_function(function_param):
#     function_param("Hello World!")
#
# another_function(my_initial_function)

"""Example 2"""
# def my_initial_function(msg):
#     print(msg)
#
# def another_function():
#     return my_initial_function
#
# another_function()("Hello World!")

"""Example 3"""
# def my_initial_function(msg):
#     print(msg)
#
# my_var = my_initial_function
#
# my_var("Hello World!")

"""Example 4"""
# def sum_decorator(custom_function):
#     def wrapper(a, b):
#         result = custom_function(a, b)
#         return result ** 2
#     return wrapper
#
# def sum_function(a, b):
#     return a + b
#
# decorated_function = sum_decorator(sum_function)
# print(decorated_function(2, 3))

"""Example 5"""
# def sum_decorator(custom_function):
#     def wrapper(a, b):
#         result = custom_function(a, b)
#         return result ** 2
#
#     return wrapper
#
# @sum_decorator
# def sum_function(a, b):
#     return a + b
#
# print(sum_function(2, 3))

"""Example 6"""
# def sum_decorator_with_param(param_number):
#     def sum_decorator(custom_function):
#         def wrapper(a, b):
#             result = custom_function(a, b)
#             return result ** param_number
#
#         return wrapper
#
#     return sum_decorator
#
# def sum_function(a, b):
#     return a + b
#
# decorated_function = sum_decorator_with_param(3)(sum_function)
# print(decorated_function(2, 3))

"""Example 7"""
# def sum_decorator_with_param(param_number):
#     def sum_decorator(custom_function):
#         def wrapper(a, b):
#             result = custom_function(a, b)
#             return result ** param_number
#
#         return wrapper
#
#     return sum_decorator
#
# @sum_decorator_with_param(param_number=3)
# def sum_function(a, b):
#     return a + b
#
# print(sum_function(2, 3))

"""Example 8"""
# class Dog:
#     legs_no = 4
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return '%s %s' % (type(self), self.name)
#
#     def change_name(self, name):
#         self.name = name
#
#     @staticmethod
#     def speak():
#         print('Bark! Bark!')
#
# print(Dog.legs_no)
# my_dog = Dog('Rex')
# print(my_dog)
# print(my_dog.name)
# print(my_dog.legs_no)
#
# my_dog.change_name("Ben")
# print(my_dog)
# print(my_dog.name)
# my_dog.speak()
# Dog.speak()

"""Example 9"""
# class FibonacciIterator:
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         self.count = 0
#         self.value = 1
#         self.prev = 0
#         return self
#
#     def __next__(self):
#         if self.count < self.n:
#             value = self.value
#             self.value += self.prev
#             self.prev = value
#             self.count += 1
#
#             return value
#         else:
#             raise StopIteration
#
# fibonacci_instance = FibonacciIterator(10)
# fibonacci_iterator = iter(fibonacci_instance)
#
# for number in fibonacci_iterator:
#     print(number)