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
def sum_decorator(custom_function):
    def wrapper(a, b):
        result = custom_function(a, b)
        return result ** 2
    return wrapper

def sum_function(a, b):
    return a + b

decorated_function = sum_decorator(sum_function)
print(decorated_function(2, 3))