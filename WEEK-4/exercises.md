

## **Exercise: Text Processing & Analysis**
Write a Python program that performs the following tasks:

### **Task 1: Process a List of Sentences**
1. Given a list of sentences, clean up the text by:
   - Removing any leading or trailing spaces.
   - Converting all text to lowercase.
   - Replacing punctuation (`.`, `,`, `!`, `?`) with an empty space.
   - Change it to list of words
   - Display unique words
   - Count total words 
   - Count unique words
   - Lexical variety is the measure of word diversity in a text, indicating how many unique words are used instead of repeating the same words frequently. Find the lexical variety of the list of words


---

#### **Example Input:**
```python
sentences = [
    "  Python is amazing!  ",
    "I love coding in Python.",
    "Loops, strings, and lists are powerful in Python.",
    "Python is fun!"
]
```

#### **Expected Output:**

```sh
['python', 'is', 'amazing', 'i', 'love', 'coding', 'in', 'python', 'loops', 'strings', 'and', 'lists', 'are', 'powerful', 'in', 'python', 'python', 'is', 'fun']
```
---

#### **Guidelines for Students:**
- Use **string methods** like `.strip()`, `.lower()`, and `.replace()`.
- Use **lists** to store words after splitting the sentences.
- Use a **for loop** to iterate over the list and count words.
- Use a **dictionary** to store word counts.



---

## **Task 2: List & Loop Exercises**  

### **1. Sum of Even Numbers**  
Write a Python program that takes a list of numbers and prints the sum of all even numbers using a for loop.  

```python
numbers = [12, 7, 9, 14, 22, 5, 8, 13]
```
**Expected Output:** `Sum of even numbers: 56`  

---

### **2. Remove Duplicates from a List**  
Write a program that removes duplicates from a given list and prints the unique values.  

```python
items = [2, 5, 7, 2, 8, 9, 5, 8, 10]
```
**Expected Output:** `[2, 5, 7, 8, 9, 10]`  

---

### **3. Find the Maximum & Minimum in a List**  
Write a program that finds and prints the **maximum and minimum numbers** from a list **without using** the built-in `max()` and `min()` functions.  

```python
numbers = [12, 45, 2, 67, 34, 89, 1, 23]
```
**Expected Output:**  
```
Maximum: 89  
Minimum: 1  
```

---

### **4. Reverse a List Without Using `[::-1]`**  
Write a program to reverse a given list manually using a loop.  

```python
numbers = [1, 2, 3, 4, 5]
```
**Expected Output:** `[5, 4, 3, 2, 1]`  

---

### **5. Merge Two Sorted Lists**  
Write a program that merges two sorted lists into one sorted list.  

```python
list1 = [1, 3, 5, 7]  
list2 = [2, 4, 6, 8]  
```
**Expected Output:** `[1, 2, 3, 4, 5, 6, 7, 8]`  

---

## ** String & Loop Exercises**  

### **6. Count Vowels and Consonants**  
Write a program that counts and prints the number of vowels and consonants in a given string.  

```python
text = "Python is fun!"
```
**Expected Output:**  
```
Vowels: 4  
Consonants: 7  
```

---

### **7. Check If a String is a Palindrome**  
Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).  

```python
word = "madam"
```
**Expected Output:** `True`  

```python
word = "hello"
```
**Expected Output:** `False`  

---

### **8. Remove Spaces from a String**  
Write a program that removes all spaces from a given string.  

```python
text = " Python  is  awesome! "
```
**Expected Output:** `"Pythonisawesome!"`  

---

### **9. Find the Longest Word in a Sentence**  
Write a program that finds and prints the longest word in a given sentence.  

```python
sentence = "Artificial Intelligence is transforming the world"
```
**Expected Output:** `"Intelligence"`  

---

### **10. Capitalize the First Letter of Each Word**  
Write a program that capitalizes the first letter of every word in a sentence.  

```python
text = "machine learning is the future."
```
**Expected Output:** `"Machine Learning Is The Future."`  

---
