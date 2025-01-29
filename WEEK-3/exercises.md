### Problem: **Grade Calculator**  

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



### **🎯 Number Guessing Game 🎯**  

Write a Python script that generates a random number between **1 and 20** and asks the user to guess it. The user has **5 attempts** to guess correctly.  

- If the user guesses the number within **5 attempts**, print:  
  **"🎉🎉 Congratulations! You did it! 🎉🎉"**  
  **"You guessed the number in [X] attempts! You're a champion! 🏆"**  
- If the user fails to guess correctly after 5 attempts, print:  
  **"Good effort! The correct number was [X]. Keep practicing, and you'll get it next time! 🚀"**  

---

### **Example Runs**  

✅ **Winning Scenario:**  
```
Guess the number (1-20): 8  
Wrong! Try again.  

Guess the number (1-20): 15  
Wrong! Try again.  

Guess the number (1-20): 12  
🎉🎉 Congratulations! You did it! 🎉🎉  
You guessed the number in 3 attempts! You're a champion! 🏆
```

❌ **Losing Scenario:**  
```
Guess the number (1-20): 7  
Wrong! Try again.  

Guess the number (1-20): 14  
Wrong! Try again.  

Guess the number (1-20): 19  
Wrong! Try again.  

Guess the number (1-20): 2  
Wrong! Try again.  

Guess the number (1-20): 10  
Good effort! The correct number was 6. Keep practicing, and you'll get it next time! 🚀
```

---

### **Bonus Challenge** 🌟  
- If the user enters a **non-numeric** value, display an error message:  
  **"🚨 Invalid input! Please enter a number between 1 and 20."**  
- Give hints if the guess is **too high or too low**:  
  **"Too high! Try a smaller number."**  
  **"Too low! Try a bigger number."**  



