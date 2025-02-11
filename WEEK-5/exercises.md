# Exercises

### **Loops**
1. Write a `for` loop that prints all the even numbers between 1 and 20.
2. Use a `while` loop to calculate the sum of numbers from 1 to 100. Print the result.

---

### **Lists**
3. Given the list `numbers = [10, 20, 30, 40, 50]`, write code to:
   - Append the number `60` to the list.
   - Remove the number `30` from the list.
   - Print the final list.
4. Write a program that takes a list of integers as input and returns a new list with only the unique elements (no duplicates).
    #### Example 
    ```
    input_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
    result = unique_elements(input_list)
    print(result)
    ```

    #### **Expected Output:**
    ```
    [1, 2, 3, 4, 5]
    ```

---

### **Dictionaries**
5. Create a dictionary called `student` with the following key-value pairs:
   - `"name"`: `"Matti"`
   - `"age"`: `19`
   - `"grade"`: `"A"`
   Then, update the `"age"` to `29` and add a new key `"city"` with the value `"Helsinki"`. Print the updated dictionary.
6. Write a function that takes a dictionary as input and returns the key with the maximum value. For example, for `{"a": 10, "b": 20, "c": 15}`, the function should return `"b"`.

---

### **Functions**
7. Write a function called `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome (reads the same backward as forward), and `False` otherwise.
8. Create a function called `calculate_area` that takes two arguments (`length` and `width`) and returns the area of a rectangle. If no arguments are provided, assume the shape is a square with a default side length of 5.

---

### **Combined Concepts**
9. Write a program that uses a loop to create a dictionary where the keys are numbers from 1 to 10, and the values are the squares of the keys. For example, the key `2` should have the value `4`.
10. Write a function called `filter_list` that takes a list of integers and a function as arguments. The function should return a new list containing only the elements for which the provided function returns `True`. For example:
    ```python
    def is_even(x):
        return x % 2 == 0

    filter_list([1, 2, 3, 4, 5], is_even)  # Should return [2, 4]
    ```







