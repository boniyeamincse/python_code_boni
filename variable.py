# introduction to variables in Python
# Variables are used to store data values
# This is a comment explaining the variable below

# integer variable
# An integer is a whole number, positive or negative, without decimals, of unlimited length
my_int = 10

# float variable
# A float is a number, positive or negative, containing one or more decimals
my_float = 10.5 


# string variable
# A string is a sequence of characters, used to store text
my_string = "Hello, World!"

# boolean variable
# A boolean is a data type that can only have two values: True or False
my_bool = True


# list variable
# A list is a collection which is ordered and changeable, allows duplicate members
my_list = [1, 2, 3, 4, 5, "python"]


# tuple variable
# A tuple is a collection which is ordered and unchangeable, allows duplicate members   
my_tuple = (1, 2, 3, 4, 5, "python")

# dictionary variable
# A dictionary is a collection which is unordered, changeable and indexed, no duplicate members 

my_dict = {
    "name": "John", 
    "age": 30,
    "city": "New York"
}


# set variable
# A set is a collection which is unordered, unchangeable, and unindexed, no duplicate members
my_set = {1, 2, 3, 4, 5, "python"}

# none variable
# The None type is a special type in Python that represents the absence of a value or a null value
my_none = None

# complex variable
# A complex number is a number that can be expressed in the form a + b*i,   
# where a and b are real numbers, and i is the imaginary unit
my_complex = 1 + 2j
# bytes variable
# A bytes object is an immutable sequence of integers in the range 0 <= x < 256
my_bytes = b"Hello, World!" 

# bytearray variable
# A bytearray is a mutable sequence of integers in the range 0 <= x < 256
my_bytearray = bytearray(5)  # creates a bytearray of size 5
# memoryview variable
# A memoryview is a built-in function that allows you to access the internal data of an object that supports the buffer protocol without copying it
my_memoryview = memoryview(bytes(5))  # creates a memoryview of a bytes
# object of size 5      
# frozenset variable
# A frozenset is an immutable version of a set, meaning it cannot be changed after creation
my_frozenset = frozenset([1, 2, 3,  4, 5, "python"])  # creates a frozenset from a list 
# range variable
# A range is a built-in function that generates a sequence of numbers, commonly used in for loops
my_range = range(5)  # creates a range object from 0 to 4       
# slice variable
# A slice is a built-in function that allows you to access a portion of a sequence (like a list or string) by specifying a start, stop, and step
my_slice = slice(0, 5, 1)  # creates a slice object from 0 to 4 with a step of 1            
# memoryview variable
# A memoryview is a built-in function that allows you to access the internal data of an object that supports the buffer protocol without copying it
my_memoryview = memoryview(bytes(5))  # creates a memoryview of a bytes object of size 5        

# callable variable
# A callable is an object that can be called as a function, such as a function or a class
def my_function():              

    return "This is a callable function"        
my_callable = my_function  # assigns the function to a variable
# function variable
# A function is a block of code that only runs when it is called, and can take parameters and return a value
def my_function_with_params(param1, param2):
    return f"Function called with {param1} and {param2}"            

my_function_var = my_function_with_params  # assigns the function to a variable     


# class variable
# A class is a blueprint for creating objects, providing initial values for state (attributes) and      
# implementations of behavior (methods)

class MyClass:  
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"
my_class_instance = MyClass("John")  # creates an instance of MyClass with the name "John"  

# module variable
# A module is a file containing Python code, which can define functions, classes, and variables     
import math  # imports the math module, which provides access to mathematical functions and constants
my_module = math  # assigns the math module to a variable       
# package variable
# A package is a way of organizing related modules into a single directory hierarchy, allowing for better           
# organization and reuse of code
import os  # imports the os module, which provides a way of using operating system dependent functionality
my_package = os  # assigns the os module to a variable      


# namespace variable
# A namespace is a container that holds a set of identifiers (names) and their corresponding objects    
my_namespace = globals()  # gets the global namespace, which contains all global variables and functions
# context variable          
# A context variable is a variable that is used to store context-specific information, such as the current user or request
from contextvars import ContextVar      




my_context_var = ContextVar("my_context_var")  # creates a context variable with the name "my_context_var"  
# coroutine variable
# A coroutine is a special type of function that can pause and resume its execution, allowing for asynchronous programming
import asyncio  # imports the asyncio module, which provides support for asynchronous programming

async def my_coroutine():
    await asyncio.sleep(1)  # pauses the coroutine for 1 second
    return "Coroutine completed"    



my_coroutine_var = my_coroutine  # assigns the coroutine function to a variable
# generator variable
# A generator is a special type of iterator that allows you to iterate over a sequence of values    



def my_generator():
    for i in range(5):
        yield i  # yields the next value in the sequence    


my_generator_var = my_generator  # assigns the generator function to a variable
# iterator variable
# An iterator is an object that implements the iterator protocol, which consists of the methods __iter__() and __next__()   





    # print all the variables
print("Integer:", my_int)
print("Float:", my_float)
print("String:", my_string)
print("Boolean:", my_bool)
print("List:", my_list)
print("Tuple:", my_tuple)
print("Dictionary:", my_dict)
print("Set:", my_set)
print("None:", my_none)
print("Complex:", my_complex)
print("Bytes:", my_bytes)
print("Bytearray:", my_bytearray)
print("Memoryview:", my_memoryview)
print("Frozenset:", my_frozenset)
print("Range:", list(my_range))  # convert range to list for display
print("Slice:", my_slice)
print("Callable:", my_callable())
print("Function:", my_function_var("param1", "param2"))
print("Class Instance:", my_class_instance.greet())
print("Module (math.sqrt(16)):", my_module.sqrt(16))
print("Package (os.getcwd()):", my_package.getcwd())
print("Namespace (globals keys):", list(my_namespace.keys()))
print("ContextVar:", my_context_var)
print("Coroutine (function):", my_coroutine_var)
print("Generator (function):", my_generator_var)