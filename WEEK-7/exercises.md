
# **Exercises**

```python
blogs = [
    {
        "id": 1,
        "title": "Introduction to Python",
        "author": "John Doe",
        "tags": ["python", "programming", "beginners"],
        "content": "Python is a versatile programming language...",
        "likes": 120,
        "comments": 25
    },
    {
        "id": 2,
        "title": "Advanced Python Techniques",
        "author": "Jane Smith",
        "tags": ["python", "advanced", "optimization"],
        "content": "Learn advanced Python techniques...",
        "likes": 85,
        "comments": 15
    },
    {
        "id": 3,
        "title": "Data Analysis with Pandas",
        "author": "John Doe",
        "tags": ["python", "data analysis", "pandas"],
        "content": "Pandas is a powerful library for data analysis...",
        "likes": 200,
        "comments": 50
    },
    {
        "id": 4,
        "title": "Machine Learning Basics",
        "author": "Alice Johnson",
        "tags": ["python", "machine learning", "AI"],
        "content": "Machine learning is transforming industries...",
        "likes": 300,
        "comments": 75
    }
]
```

---

## **Questions for Students**

### **1. List Comprehensions**

1. **Extract Titles**: Use a list comprehension to extract all blog titles.
2. **Filter by Author**: Use a list comprehension to filter blogs written by "John Doe".
3. **Popular Blogs**: Use a list comprehension to extract blogs with more than 100 likes.
4. **Tag Search**: Use a list comprehension to find all blogs that have the tag "python".
5. **Count Comments**: Use a list comprehension to create a list of tuples containing the blog title and its number of comments.

---

### **2. Map Function**

1. **Author Names**: Use `map` to extract the names of all authors.
2. **Uppercase Titles**: Use `map` to convert all blog titles to uppercase.
3. **Likes Count**: Use `map` to create a list of the number of likes for each blog.
4. **Tag Count**: Use `map` to create a list of the number of tags for each blog.

---

### **3. Reduce Function**

1. **Total Likes**: Use `reduce` to calculate the total number of likes across all blogs.
2. **Most Comments**: Use `reduce` to find the blog with the highest number of comments.
3. **Concatenate Titles**: Use `reduce` to concatenate all blog titles into a single string, separated by commas.

---

### **4. Filter Function**

1. **High Engagement**: Use `filter` to find blogs with more than 50 comments.
2. **Specific Tag**: Use `filter` to find blogs that contain the tag "machine learning".
3. **Author Filter**: Use `filter` to find blogs written by "Jane Smith".

---

### **5. Lambda Functions**

1. **Sort by Likes**: Use `sorted` with a lambda function to sort the blogs by the number of likes in descending order.
2. **Sort by Comments**: Use `sorted` with a lambda function to sort the blogs by the number of comments in ascending order.
3. **Filter by Tag**: Use `filter` with a lambda function to find blogs that contain the tag "data analysis".

---

### **6. Advanced Questions**

1. **Unique Authors**: Use a set comprehension to extract the names of all unique authors.
2. **Tag Frequency**: Use a dictionary to count how many blogs contain each tag.
3. **Average Likes**: Calculate the average number of likes per blog.
4. **Blog Summary**: Create a new list of dictionaries where each dictionary contains only the `title`, `author`, and `likes` of the blog.
5. **Merge Tags**: Use `reduce` to merge all tags from all blogs into a single list (ensure no duplicates).

---
