# Python Variables – Study Notes

## 🐍 Python Notes: Variables

### 📌 What is a Variable?

A **variable** is like a container in Python. It stores data that you can use and change later in your code. Variables help you keep track of information as your program runs.

---

### ✅ How to Create a Variable

You just give it a name and assign it a value using `=`:

```python
name = "Alice"        # string
age = 25              # integer
height = 5.6          # float
is_student = True     # boolean
```

---

### 🧠 Variable Naming Rules

- Must start with a letter or underscore (`_`)
- Can contain letters, numbers, and underscores
- **Cannot** start with a number
- Variable names are case-sensitive (`Name` and `name` are different)
- Avoid using Python reserved keywords (like `for`, `if`, `class`)

**Valid names:**
```python
my_var = 10
_name = "Sam"
age2 = 20
```

**Invalid names:**
```python
2name = "Bob"   # starts with a number
my-var = 10     # hyphens are not allowed
```

---

### 🔁 Changing Variable Values

You can reassign a variable any time:

```python
score = 100
score = 120  # new value
```

---

### 🧪 Type Checking

You can check the data type using `type()`:

```python
x = 10
print(type(x))   # <class 'int'>
```

---

### ✨ Python is Dynamically Typed

You don’t need to declare variable types ahead of time — Python figures it out for you:

```python
x = 10      # x is an int
x = "ten"   # now x is a str
```

---

### 📚 Types of Variables in Python

| Type      | Example                        | Description                        |
|-----------|-------------------------------|------------------------------------|
| int       | `x = 10`                      | Integer (whole number)             |
| float     | `y = 3.14`                    | Floating-point (decimal) number    |
| str       | `name = "Alice"`              | String (text)                      |
| bool      | `is_valid = True`             | Boolean (True or False)            |
| list      | `nums = [1, 2, 3]`            | Ordered, mutable collection        |
| tuple     | `point = (2, 3)`              | Ordered, immutable collection      |
| dict      | `student = {"name": "Bob", "age": 20}` | Key-value pairs      |
| set       | `unique = {1, 2, 3}`          | Unordered, unique items            |
| NoneType  | `result = None`               | Represents no value                |
| complex   | `z = 2 + 3j`                  | Complex number                     |

---

### 📝 Multiple Assignment

You can assign values to multiple variables at once:

```python
a, b, c = 1, 2, 3
```

---

### 🔄 Swapping Variables

Python allows easy swapping of variable values:

```python
x, y = 5, 10
x, y = y, x  # Now x is 10 and y is 5
```

---

### 💡 Best Practices

- Use descriptive variable names (`total_price` instead of `tp`)
- Stick to lowercase letters and underscores for variable names (snake_case)
- Initialize variables before using them

---

## 📖 More Resources for Learning Python Variables

- [Python Official Documentation: Variables](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
- [W3Schools Python Variables](https://www.w3schools.com/python/python_variables.asp)
- [Programiz: Python Variables and Data Types](https://www.programiz.com/python-programming/variables-datatypes)
- [Real Python: Variables in Python](https://realpython.com/python-variables/)
- [GeeksforGeeks: Python Variables](https://www.geeksforgeeks.org/python-variables/)

---

**Summary:**  
Variables are fundamental in Python for storing and manipulating data. Understanding variable types and naming rules is essential for writing clear and effective Python code.