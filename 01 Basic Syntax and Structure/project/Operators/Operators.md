# Python Operators

Python divides operators into the following groups:

- **Arithmetic Operators**
- **Assignment Operators**
- **Comparison Operators**
- **Logical Operators**
- **Identity Operators**
- **Membership Operators**
- **Bitwise Operators**

These operators are used to perform operations on variables and values, and are categorized based on their functionality.

## 1. Arithmetic Operators

These operators perform mathematical calculations:

| Operator | Name            | Example      |
|----------|-----------------|-------------|
| +        | Addition        | x + y       |
| -        | Subtraction     | x - y       |
| *        | Multiplication  | x * y       |
| /        | Division        | x / y       |
| //       | Floor Division  | x // y      |
| %        | Modulo          | x % y       |
| **       | Exponentiation  | x ** y      |

## 2. Comparison (Relational) Operators

These operators compare two values and return a Boolean result (`True` or `False`):

| Operator | Description                  | Example    |
|----------|------------------------------|------------|
| ==       | Equal to                     | x == y     |
| !=       | Not equal to                 | x != y     |
| >        | Greater than                 | x > y      |
| <        | Less than                    | x < y      |
| >=       | Greater than or equal to     | x >= y     |
| <=       | Less than or equal to        | x <= y     |

## 3. Logical Operators

These operators combine or manipulate Boolean expressions:

| Operator | Description                                 | Example             |
|----------|---------------------------------------------|---------------------|
| and      | Returns True if both operands are True      | x > 5 and y < 10    |
| or       | Returns True if at least one is True        | x > 5 or y < 10     |
| not      | Reverses the Boolean value of the operand   | not (x > 5)         |

## 4. Assignment Operators

These operators assign values to variables:

| Operator | Example   | Equivalent to   |
|----------|-----------|----------------|
| =        | x = 5     | x = 5          |
| +=       | x += 5    | x = x + 5      |
| -=       | x -= 5    | x = x - 5      |
| *=       | x *= 5    | x = x * 5      |
| /=       | x /= 5    | x = x / 5      |
| %=       | x %= 5    | x = x % 5      |
| //=      | x //= 5   | x = x // 5     |
| **=      | x **= 5   | x = x ** 5     |

## 5. Identity Operators

These operators compare the memory locations of two objects:

| Operator | Description                                         | Example    |
|----------|-----------------------------------------------------|------------|
| is       | True if both variables point to the same object     | x is y     |
| is not   | True if they do not point to the same object        | x is not y |

## 6. Membership Operators

These operators check if an item exists within a sequence (e.g., string, list, tuple):

| Operator | Description                                 | Example             |
|----------|---------------------------------------------|---------------------|
| in       | True if value is found in the sequence      | 'a' in 'banana'     |
| not in   | True if value is not found in the sequence  | 'z' not in 'banana' |

## 7. Bitwise Operators

These operators perform bit-level operations on integers:

| Operator | Name        | Example   |
|----------|-------------|-----------|
| &        | AND         | x & y     |
| \|       | OR          | x \| y    |
| ^        | XOR         | x ^ y     |
| ~        | NOT         | ~x        |
| <<       | Left Shift  | x << 2    |
| >>       | Right Shift | x >> 2    |

## Practice Problems

### Beginner Level

1. **Addition Calculator**  
   Write a program that asks the user for two numbers and prints their sum.

2. **Even or Odd Checker**  
   Ask the user for a number and print whether it is even or odd using the modulo operator.

3. **Simple Comparison**  
   Input two numbers and print which one is greater, or if they are equal.

4. **Membership Test**  
   Ask the user for a letter and check if it is present in the word "python".

5. **Swap Two Variables**  
   Take two numbers as input and swap their values using assignment operators.

---

### Intermediate Level

6. **Grade Calculator**  
   Input marks for three subjects, calculate the average, and print the grade using comparison operators.

7. **Logical Operations**  
   Take two Boolean values as input and print the result of `and`, `or`, and `not` operations.

8. **Identity Check**  
   Create two lists with the same values and check if they are the same object using identity operators.

9. **Bitwise Operations**  
   Input two integers and print the result of their bitwise AND, OR, and XOR operations.

10. **Compound Assignment Practice**  
    Start with `x = 20`. Use compound assignment operators to add 10, subtract 5, multiply by 2, and divide by 5. Print the result after each operation.

---

### Advanced Level

11. **Password Strength Checker**  
    Ask the user for a password and check if it contains at least one uppercase letter, one lowercase letter, one digit, and is at least 8 characters long (use membership and comparison operators).

12. **Set Operations**  
    Input two lists from the user, convert them to sets, and print their union, intersection, and difference using set and bitwise operators.

13. **Custom Calculator**  
    Write a calculator that takes two numbers and an operator (+, -, *, /, //, %, **) as input and prints the result.

14. **Prime Number Finder**  
    Ask the user for a number and print whether it is a prime number using logical and comparison operators.

15. **List Filter with Lambda**  
    Given a list of numbers, use a lambda function and the `filter()` function to print all even numbers from the list.

---