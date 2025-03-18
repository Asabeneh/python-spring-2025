
# Projects: Web Application Using Python

Choose one of the project and implement a simple web application using Python and Flask

## 1. Random Cat Display with Flask

- **Objective**: Build a simple Flask web application to display random cat data.
- **Example**: https://cats-paradise-f994f218e0ee.herokuapp.com
- **Task**:
  1. Use the **Cats' API** (<https://api.thecatapi.com/v1/breeds>) to fetch random cat data.
  2. Create a Flask app with a homepage that displays:
     - A random cat's name.
     - An image of the cat.
     - A short description of the cat.
  3. Use HTML templates to render the data dynamically.

---

## 2. Country Information Display with Flask

- **Objective**: Build a Flask app to display country information.
- **Example**: https://asabeneh.github.io/world-countries-data-api
- **Task**:
  1. Use the **Countries' API** (<https://restcountries.com/v3.1/all>) to fetch data about countries.
  2. Create a Flask app that displays the following information for each country:
     - Country name.
     - Capital.
     - Population.
     - Official languages.
  3. Use HTML templates to render the data in a clean and organized manner.

---

## 3. QR Code Generator

- **Objective**: Build a QR code generator web application.
- **Example**: https://qrcode-generator-reader-305c57e50ba6.herokuapp.com/qrcode
- **Task**:
  1. Create a Flask app that allows users to input text or a URL.
  2. Generate a QR code for the input using a Python library like `qrcode`.
  3. Display the generated QR code on the webpage.
  4. Optionally, allow users to download the QR code as an image.

---

## 4. Text Analyzer

- **Objective**: Build a text analyzer web application.
- **Example**:https://thirtydayofpython-api.herokuapp.com/post
- **Task**:
  1. Create a Flask app with a form where users can input text.
  2. Analyze the text and display the following metrics:
     - Word count.
     - Character count.
     - Most frequent words.
     - Average word length.
  3. Use HTML templates to display the results in a user-friendly format.

---

## 5. Sentiment Analyzer

- **Objective**: Build a text sentiment analyzer web application.
- **Example**:https://sentiment-app-6862d57cdb4b.herokuapp.com/sentiments
- **Task**:
  1. Create a Flask app with a form where users can input text.
  2. Analyze the sentiment and display the following metrics:
     - Sentiment of the text as Positive, Negative and Neutral.
     - Create a bar graph of the sentiment using matplotlib
     - Create a pie chart of the sentiment using matplotlib
     - Average word length.
  3. Use HTML templates to display the results in a user-friendly format.

---

## 6. Sentiment Analyzer

- **Objective**: Build a simple web application that send email.
- **Example**:https://emailer-1e7a0696eeee.herokuapp.com/contacts
- **Task**:
  1. Create a Flask app with a form where users can input text as shown in the example
  2. Attachement file is optional
  3. Use HTML templates to display the results in a user-friendly format.

---

## 7. Blog Application

- **Objective**: Build blog web application.
- **Example**:https://github.com/Asabeneh/python-spring-2025/tree/main/WEEK-9/blogs
- **Task**:
  1. Continue building the blog application and add post, edit and delete features to the blog .
  2. Use HTML templates to display the results in a user-friendly format.

---

## Additional Notes

- **APIs**:
  - Cats' API: <https://api.thecatapi.com/v1/breeds>
  - Countries' API: <https://restcountries.com/v3.1/all>
- **Tools**:
  - Use `requests` to fetch data from APIs.
  - Use `json` to handle JSON data.
  - Use `Flask` for building web applications.
  - Use `qrcode` for generating QR codes.
  - Use `TextBlob` for sentiment analysis
  - Use `Flask-Mail` for the email application
- **References**:
  - Cats Paradise API Format: <https://cats-paradise-f994f218e0ee.herokuapp.com/api/v1/cats>
  - QR Code Generator Example: <https://qrcode-generator-reader-305c57e50ba6.herokuapp.com/qrcode>
  - Text Analyzer Example: <https://thirtydayofpython-api.herokuapp.com/post>
