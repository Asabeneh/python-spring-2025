# Python Operators, Variables, and Data Types

- [Section Introduction](#section-introduction)
- [Python Operators](#python-operators)
  - [Arithmetic Operators](#arithmetic-operators)
  - [Assignment Operators](#assignment-operators)
  - [Comparison (Relational) Operators](#comparison-relational-operators)
  - [Logical Operators](#logical-operators)
  - [Bitwise Operators](#bitwise-operators)
  - [Membership Operators](#membership-operators)
  - [Identity Operators](#identity-operators)
  - [Ternary Operator (Conditional Expression)](#ternary-operator-conditional-expression)
  - [Special Operators](#special-operators)
    - [`del` Operator](#del-operator)
    - [`pass` Operator](#pass-operator)
- [Variables](#variables)
  - [Understanding Variables and Basic Operations](#understanding-variables-and-basic-operations)
  - [What is a Variable?](#what-is-a-variable)
  - [Conclusion](#conclusion)
- [Python Data Types](#python-data-types)
  - [Numbers](#numbers)
  - [Booleans](#booleans)
  - [Strings](#strings)
  - [Lists](#lists)
  - [Tuples](#tuples)
  - [Sets](#sets)
  - [Dictionaries](#dictionaries)

---

[<< WEEK 1](../readme.md) | [WEEK 3 >>](../WEEK-3/week-3.md)
[WEEK 2 >>](./WEEK-2/week-2.md)

[WEEK 1](./readme.md) | [WEEK 2](./WEEK-2/week-2.md) | [WEEK 3](./WEEK-3/week-3.md) | [WEEK 4](./WEEK-4/week-4.md.md) | [WEEK 5](./WEEK-5/week-5.md) | [WEEK 6](./WEEK-6/week-6.md)

---

## Section Introduction

This section introduces essential Python concepts through practical examples. It covers **operators**, **variables**, **data types**, and **built-in functions**, making it a great resource for both beginners and intermediate learners. Each example is accompanied by clear explanations to ensure easy understanding and application.

---

## Python Operators

Operators are special symbols or keywords used to perform operations on values and variables. Python provides a wide range of operators, including arithmetic, assignment, comparison, logical, bitwise, membership, and identity operators. Let’s explore each type with examples.

---

### Arithmetic Operators

Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication, etc.

| Operator | Description                | Example     | Output  |
|----------|----------------------------|-------------|---------|
| `+`      | Addition                   | `3 + 2`     | `5`     |
| `-`      | Subtraction                | `5 - 2`     | `3`     |
| `*`      | Multiplication             | `4 * 3`     | `12`    |
| `/`      | Division (float)           | `10 / 4`    | `2.5`   |
| `%`      | Modulus (remainder)        | `10 % 3`    | `1`     |
| `**`     | Exponentiation (power)     | `2 ** 3`    | `8`     |
| `//`     | Floor division (integer)   | `10 // 3`   | `3`     |

**Examples:**

```python
# Addition
print(3 + 4)  # Output: 7

# Exponentiation
print(2 ** 3)  # Output: 8

# Floor division
print(10 // 4)  # Output: 2
```

---

### Assignment Operators

Assignment operators are used to assign values to variables. Python provides shorthand operators to simplify variable manipulations.

| Operator  | Description                    | Example    | Equivalent |
|-----------|--------------------------------|------------|------------|
| `=`       | Assign value                   | `a = 5`    | -          |
| `+=`      | Add and assign                 | `a += 3`   | `a = a + 3`|
| `-=`      | Subtract and assign            | `a -= 3`   | `a = a - 3`|
| `*=`      | Multiply and assign            | `a *= 2`   | `a = a * 2`|
| `/=`      | Divide and assign (float)      | `a /= 2`   | `a = a / 2`|
| `%=`      | Modulus and assign             | `a %= 3`   | `a = a % 3`|
| `**=`     | Exponentiation and assign      | `a **= 2`  | `a = a ** 2`|
| `//=`     | Floor divide and assign        | `a //= 2`  | `a = a // 2`|

**Examples:**

```python
a = 10
a += 5  # a = a + 5
print(a)  # Output: 15

b = 20
b //= 3  # b = b // 3
print(b)  # Output: 6
```

---

### Comparison (Relational) Operators

Comparison operators are used to compare two values or variables, returning a boolean (`True` or `False`).

| Operator | Description             | Example     | Output   |
|----------|-------------------------|-------------|----------|
| `==`     | Equal to                 | `5 == 5`    | `True`   |
| `!=`     | Not equal to             | `5 != 4`    | `True`   |
| `>`      | Greater than             | `7 > 5`     | `True`   |
| `<`      | Less than                | `5 < 10`    | `True`   |
| `>=`     | Greater than or equal to | `7 >= 7`    | `True`   |
| `<=`     | Less than or equal to    | `4 <= 5`    | `True`   |

**Examples:**

```python
print(5 == 5)  # Output: True
print(3 != 2)  # Output: True
print(7 < 6)   # Output: False
```

---

### Logical Operators

Logical operators are used to combine conditional statements and return boolean results.

| Operator | Description                  | Example            | Output  |
|----------|------------------------------|--------------------|---------|
| `and`    | Returns `True` if both conditions are true | `True and True`  | `True`  |
| `or`     | Returns `True` if at least one condition is true | `True or False` | `True`  |
| `not`    | Reverses the result (returns `False` if the result is `True`) | `not True` | `False` |

**Examples:**

```python
print(5 > 3 and 8 > 6)  # Output: True
print(5 > 3 or 2 > 6)   # Output: True
print(not 5 == 5)       # Output: False
```

---

### Bitwise Operators

Bitwise operators work at the binary level (i.e., on bits) and are mainly used in low-level programming or when manipulating individual bits.

| Operator | Description                          | Example  | Output |
|----------|--------------------------------------|----------|--------|
| `&`      | Bitwise AND                          | `5 & 3`  | `1`    |
| `|`      | Bitwise OR                           | `5 | 3`  | `7`    |
| `^`      | Bitwise XOR                          | `5 ^ 3`  | `6`    |
| `~`      | Bitwise NOT                          | `~5`     | `-6`   |
| `<<`     | Bitwise left shift                   | `5 << 1` | `10`   |
| `>>`     | Bitwise right shift                  | `5 >> 1` | `2`    |

**Examples:**

```python
# Bitwise AND
print(5 & 3)  # Output: 1

# Bitwise left shift
print(5 << 1)  # Output: 10
```

---

### Membership Operators

Membership operators are used to test if a value is present in a sequence (e.g., a string, list, tuple, or set).

| Operator | Description                   | Example          | Output |
|----------|-------------------------------|------------------|--------|
| `in`     | Returns `True` if the value is present | `'a' in 'apple'` | `True`  |
| `not in` | Returns `True` if the value is not present | `'b' not in 'apple'` | `True`  |

**Examples:**

```python
print('p' in 'apple')  # Output: True
print(2 not in [1, 3, 5])  # Output: True
```

---

### Identity Operators

Identity operators check if two variables refer to the same object in memory.

| Operator | Description                       | Example         | Output |
|----------|-----------------------------------|-----------------|--------|
| `is`     | Returns `True` if two variables point to the same object | `a is b` | `True`  |
| `is not` | Returns `True` if two variables point to different objects | `a is not b` | `True`  |

**Examples:**

```python
a = [1, 2, 3]
b = a
print(a is b)  # Output: True (b refers to the same object as a)

c = [1, 2, 3]
print(a is not c)  # Output: True (c is a different object even though it contains the same values)
```

---

### Ternary Operator (Conditional Expression)

The ternary operator is used to evaluate a condition in a single line of code and return one of two values based on the condition.

**Syntax:**  
`[on_true] if [condition] else [on_false]`

**Example:**

```python
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
```

---

### Special Operators

#### `del` Operator

The `del` operator is used to delete objects or variables.

```python
a = 5
del a  # a is deleted and no longer accessible
```

#### `pass` Operator

The `pass` operator is a null operation; it is used as a placeholder for future code.

```python
def func():
    pass  # No code yet
```

---

## Variables

Variables are containers that store data values. They can hold various data types, including numbers, strings, lists, tuples, and sets.

---

### Understanding Variables and Basic Operations

Variables are fundamental components of programming that allow you to store and manipulate data. In Python, you can assign a value to a variable using the assignment operator (`=`). Here's an example:

```python
# Arithmetic Operations
a = 3
b = 4
c = a + b
```

**Output:**

```python
print('Value of a:', a)                   # Output: Value of a: 3
print('Sum of a and b:', c)               # Output: Sum of a and b: 7
print('Sum of a and b is', a + b)         # Output: Sum of a and b is 7
print('Difference of a and b is', a - b)  # Output: Difference of a and b is -1
print('Product of a and b is', a * b)     # Output: Product of a and b is 12
print('Division of a and b is', a / b)    # Output: Division of a and b is 0.75
```

---

### What is a Variable?

A variable is a named location in memory used to store data. Descriptive variable names enhance code readability and maintainability.

**Examples:**

```python
# Personal Information
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
```

---

### Conclusion

This section covered Python operators, variables, and data types. Understanding these concepts is essential for writing efficient and readable code. With this knowledge, you can start building more complex programs and data management solutions in Python.

---

## Python Data Types

Python supports several fundamental data types:

- **Numbers**: `int`, `float`, `complex`
- **Booleans**: `True`, `False`
- **Strings**: Text enclosed in single, double, or triple quotes
- **Lists**: Ordered collections of elements
- **Tuples**: Immutable collections
- **Sets**: Unordered collections of unique elements
- **Dictionaries**: Key-value pairs

---

### Numbers

```python
print(type(10))  # Output: <class 'int'>
print(type(9.81))  # Output: <class 'float'>
print(type(1 + 2j))  # Output: <class 'complex'>
```

---

### Booleans

```python
print(type(True))  # Output: <class 'bool'>
print(0 < 1)  # Output: True
```

---

### Strings

```python
print('I love Python'.upper())  # Output: I LOVE PYTHON
print('Python'.startswith('P'))  # Output: True
```

---

### Lists

```python
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])  # Output: apple
```

---

### Tuples

```python
colors = ('red', 'green', 'blue')
print(colors[1])  # Output: green
```

---

### Sets

```python
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # Output: {1, 2, 3, 4}
```

---

### Dictionaries

```python
person = {'name': 'Alice', 'age': 25}
print(person['name'])  # Output: Alice
```

---

[<< WEEK 1](../readme.md) | [WEEK 3 >>](../WEEK-3/week-3.md)

[WEEK 1](./readme.md) | [WEEK 2](./WEEK-2/week-2.md) | [WEEK 3](./WEEK-3/week-3.md) | [WEEK 4](./WEEK-4/week-4.md.md) | [WEEK 5](./WEEK-5/week-5.md) | [WEEK 6](./WEEK-6/week-6.md)