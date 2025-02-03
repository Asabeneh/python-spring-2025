'''
## **Grade Calculator**  

Write a Python script that asks the user to enter their exam score (a number between 0 and 100). Based on the score, the program should print the corresponding grade using the following grading system:

- **90 - 100** → Grade **A**  
- **80 - 89** → Grade **B**  
- **70 - 79** → Grade **C**  
- **60 - 69** → Grade **D**  
- **0 - 59** → Grade **F**  
- If the score is outside the range 0-100, print an error message: `"Invalid score! Please enter a number between 0 and 100."`

#### **Example Runs**  
✅ **Valid Input:**  
```
Enter your score: 85  
Your grade is: B  
```
✅ **Valid Input:**  
```
Enter your score: 72  
Your grade is: C  
```
❌ **Invalid Input:**  
```
Enter your score: 105  
Invalid score! Please enter a number between 0 and 100.  
```

---

### **Bonus Challenge** 🌟  
Modify your program to handle cases where the user enters a non-numeric value, displaying an appropriate error message like:  
`"Invalid input! Please enter a valid number."`  



'''

score = float(input("Enter your score (0 - 100): "))
print(score)

if score > 100 or score < 0:
    print('The score must be less than or equal to 100 and greater zero')
else:
    if score >= 90:
        print(f'Your score is {score} and your grade is A.')
    elif score >= 80:
        print(f'Your score is {score} and your grade is B.')
    elif score >= 70:
        print(f'Your score is {score} and your grade is C')
    elif score >= 60:
        print(f'Your score is {score} and your grade is D')
    else :
        print(f'Your score is {score} and your grade is F')
