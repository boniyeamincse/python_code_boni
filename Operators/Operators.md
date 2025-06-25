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