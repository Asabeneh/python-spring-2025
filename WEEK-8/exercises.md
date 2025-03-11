
# Exercises

## File Handling

### 1. Create `cats.json` File

- **Objective**: Practice working with JSON files and APIs.
- **Task**:
  1. Use the **Cats' API** (<https://api.thecatapi.com/v1/breeds>) to fetch data about cat breeds.
  2. Create a `cats.json` file with the following structure:

     ```json
     {
       "country": "Egypt",
       "description": "The Abyssinian is easy to care for, and a joy to have in your home. They’re affectionate cats and love both people and other animals.",
       "image": "https://cdn2.thecatapi.com/images/0XYvRd7oD.jpg",
       "life_span": 14.5,
       "name": "Abyssinian",
       "temperament": "Active, Energetic, Independent, Intelligent, Gentle",
       "weight": 4
     }
     ```

  3. Ensure the `cats.json` file follows the format shown here: <https://cats-paradise-f994f218e0ee.herokuapp.com/api/v1/cats>.

---

## Web Application Using Python

### 1. Random Cat Display with Flask

- **Objective**: Build a simple Flask web application to display random cat data.
- **Task**:
  1. Use the **Cats' API** (<https://api.thecatapi.com/v1/breeds>) to fetch random cat data.
  2. Create a Flask app with a homepage that displays:
     - A random cat's name.
     - An image of the cat.
     - A short description of the cat.
  3. Use HTML templates to render the data dynamically.

---

### 2. Country Information Display with Flask

- **Objective**: Build a Flask app to display country information.
- **Task**:
  1. Use the **Countries' API** (<https://restcountries.com/v3.1/all>) to fetch data about countries.
  2. Create a Flask app that displays the following information for each country:
     - Country name.
     - Capital.
     - Population.
     - Official languages.
  3. Use HTML templates to render the data in a clean and organized manner.

---

### 3. QR Code Generator

- **Objective**: Build a QR code generator web application.
- **Task**:
  1. Create a Flask app that allows users to input text or a URL.
  2. Generate a QR code for the input using a Python library like `qrcode`.
  3. Display the generated QR code on the webpage.
  4. Optionally, allow users to download the QR code as an image.

---

### 4. Text Analyzer

- **Objective**: Build a text analyzer web application.
- **Task**:
  1. Create a Flask app with a form where users can input text.
  2. Analyze the text and display the following metrics:
     - Word count.
     - Character count.
     - Most frequent words.
     - Average word length.
  3. Use HTML templates to display the results in a user-friendly format.

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
- **References**:
  - Cats Paradise API Format: <https://cats-paradise-f994f218e0ee.herokuapp.com/api/v1/cats>
  - QR Code Generator Example: <https://qrcode-generator-reader-305c57e50ba6.herokuapp.com/qrcode>
  - Text Analyzer Example: <https://thirtydayofpython-api.herokuapp.com/post>
