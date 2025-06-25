# Python Built-in Data Types

In programming, a **data type** is an important concept.  
Variables can store data of different types, and different types can do different things.

Python has the following built-in data types, grouped into categories:

---

| Category         | Data Type      | Example                              | Description                                 |
|------------------|---------------|--------------------------------------|---------------------------------------------|
| Text Type        | `str`         | `name = "Alice"`                     | String (text)                               |
| Numeric Types    | `int`         | `age = 25`                           | Integer number                              |
|                  | `float`       | `price = 19.99`                      | Floating point number                       |
|                  | `complex`     | `z = 2 + 3j`                         | Complex number                              |
| Sequence Types   | `list`        | `fruits = ["apple", "banana"]`       | Ordered, mutable collection                 |
|                  | `tuple`       | `coordinates = (10.0, 20.0)`         | Ordered, immutable collection               |
|                  | `range`       | `numbers = range(5)`                 | Sequence of numbers                         |
| Mapping Type     | `dict`        | `student = {"name": "Bob"}`          | Key-value pairs                             |
| Set Types        | `set`         | `unique = {1, 2, 3}`                 | Unordered, unique items                     |
|                  | `frozenset`   | `frozen = frozenset([1, 2, 3])`      | Immutable set                               |
| Boolean Type     | `bool`        | `is_active = True`                   | Boolean value (`True` or `False`)           |
| Binary Types     | `bytes`       | `data = b"hello"`                    | Immutable sequence of bytes                 |
|                  | `bytearray`   | `arr = bytearray(5)`                 | Mutable sequence of bytes                   |
|                  | `memoryview`  | `mem = memoryview(bytes(5))`         | Memory view object                          |
| None Type        | `NoneType`    | `result = None`                      | Represents the absence of a value           |

---

## Example Problems

1. **String Example**  
   Store your name in a variable and print it.
   ```python
   name = "Alice"
   print(name)
   ```

2. **Integer and Float Example**  
   Store your age and height in variables and print them.
   ```python
   age = 25
   height = 5.7
   print(age, height)
   ```

3. **List Example**  
   Create a list of three favorite colors and print the second color.
   ```python
   colors = ["red", "green", "blue"]
   print(colors[1])
   ```

4. **Dictionary Example**  
   Create a dictionary for a book with keys: title, author, and year. Print the author.
   ```python
   book = {"title": "Python 101", "author": "John Doe", "year": 2023}
   print(book["author"])
   ```

5. **Set Example**  
   Create a set of unique numbers and print it.
   ```python
   numbers = {1, 2, 3, 2, 1}
   print(numbers)
   ```

6. **Boolean Example**  
   Store whether you are a student in a variable and print its type.
   ```python
   is_student = True
   print(type(is_student))
   ```

7. **Range Example**  
   Create a range of numbers from 0 to 4 and print each number.
   ```python
   for i in range(5):
       print(i)
   ```

8. **Tuple Example**  
   Store coordinates (x, y) in a tuple and print them.
   ```python
   coordinates = (10, 20)
   print(coordinates)
   ```

9. **Bytes Example**  
   Create a bytes object from a string and print it.
   ```python
   data = b"hello"
   print(data)
   ```

10. **NoneType Example**  
    Create a variable with value `None` and check its type.
    ```python
    result = None
    print(type(result))
    ```

---

## 📝 Practice Problems on Data Types

Try these problems to practice and strengthen your understanding of Python data types:

1. **String Concatenation**  
   Combine two string variables and print the result.

2. **Integer Addition**  
   Add two integer variables and print the sum.

3. **Float Multiplication**  
   Multiply two float variables and print the product.

4. **Type Conversion**  
   Convert a string representing a number to an integer and print its type.

5. **List Indexing**  
   Create a list of five items and print the third item.

6. **Tuple Unpacking**  
   Assign a tuple of three values to three variables and print each variable.

7. **Dictionary Access**  
   Create a dictionary with at least two key-value pairs and print the value of one key.

8. **Set Operations**  
   Create two sets and print their union and intersection.

9. **Boolean Logic**  
   Use boolean variables to check if a number is both greater than 10 and less than 20.

10. **Range Usage**  
    Use a range to print numbers from 1 to 10.

11. **Bytes and Bytearray**  
    Create a bytes object and a bytearray object, then print both.

12. **Memoryview Example**  
    Create a memoryview from a bytes object and print its first element.

13. **Frozenset Example**  
    Create a frozenset from a list and print it.

14. **Complex Number Operations**  
    Create two complex numbers, add them, and print the result.

15. **NoneType Check**  
    Assign `None` to a variable and check if it is `None` using an if statement.

---