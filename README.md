# 😄 Emoji Converter

A Flask-based web application that converts text shortcuts into emojis and emojis back into text shortcuts.

This project started as a simple Python string-replacement exercise and gradually evolved into a complete interactive web application using **Python, Flask, HTML, CSS, JavaScript, and JSON**.

---

## 🌐 Overview

The Emoji Converter allows users to:

* Convert text shortcuts into emojis
* Convert emojis back into shortcuts
* Search through available emojis
* Insert shortcuts directly from the emoji cheat sheet
* Copy converted results
* Swap the message and result
* Clear the message
* Switch between light and dark mode
* Track the character count while typing

### Example

```text
Input:
Hello :love: :fire: :)

Output:
Hello 😍 🔥 😊
```

Reverse conversion is also supported:

```text
Input:
Hello 😍 🔥 😊

Output:
Hello :love: :fire: :)
```

---

## ✨ Features

### 🔄 Emoji Conversion

Converts predefined text shortcuts into their corresponding emojis.

```text
:smile: → 😊
:heart: → ❤️
:fire: → 🔥
:thumbsup: → 👍
```

### 🔁 Reverse Conversion

Converts emojis back into their text shortcuts.

```text
😊 → :smile:
❤️ → :heart:
🔥 → :fire:
```

### 🔍 Emoji Search

Search the emoji cheat sheet using either the shortcut or emoji.

### 📋 Copy Result

Copy the converted result directly to the clipboard.

### 🔄 Swap

Swap the contents of the message and result boxes.

### 🧹 Clear

Clear the message, result, and character counter.

### 🌙 Dark Mode

Switch between light and dark themes, with the selected theme remembered using browser local storage.

### 🔢 Character Counter

Displays the number of characters currently entered in the message box.

### 😀 Emoji Cheat Sheet

Browse the available emoji shortcuts and click one to insert it into the message.

### 🔔 Notifications

Displays a small notification when a shortcut is inserted from the emoji cheat sheet.

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **HTML5**
* **CSS3**
* **JavaScript**
* **JSON**

---

## 📁 Project Structure

```text
Emoji-Converter/
│
├── app.py
├── EmojiConverter.py
├── emoji_map.json
├── EmojiConverter.txt
├── requirement.txt
├── .gitignore
│
├── basic_converter/
│   └── basic_converter.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## 🐍 How It Works

The project separates the emoji data, conversion logic, Flask application, and frontend.

### 1. Emoji Data

`emoji_map.json` contains the mapping between shortcuts and emojis.

Example:

```json
{
    ":smile:": "😊",
    ":heart:": "❤️",
    ":fire:": "🔥"
}
```

### 2. Conversion Logic

`EmojiConverter.py` loads the JSON data and provides functions for conversion.

The main functions are:

```python
convert_message()
reverse_convert_message()
```

### 3. Flask Application

`app.py` connects the Python conversion logic with the web interface.

It receives the user's message, determines which action was requested, performs the conversion, and sends the result back to the HTML template.

### 4. Frontend

The interface is built using:

* HTML for structure
* CSS for styling
* JavaScript for interactive features

---

## 🚀 Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/shakunsharma890/Emoji-Converter.git
```

### 2. Enter the project directory

```bash
cd Emoji-Converter
```

### 3. Install the required package

```bash
pip install -r requirement.txt
```

### 4. Run the Flask application

```bash
python3 app.py
```

### 5. Open the application

Open the local Flask address shown in your terminal, usually:

```text
http://127.0.0.1:5000/
```

---

## 🌱 Project Evolution

This project represents the evolution of a small Python idea into a complete web application.

```text
Basic Python replace()
        ↓
Multiple emoji replacements
        ↓
Emoji dictionary
        ↓
JSON-based emoji data
        ↓
Reusable conversion functions
        ↓
Reverse conversion
        ↓
Flask backend
        ↓
HTML + CSS + JavaScript
        ↓
Interactive Emoji Converter
```

The original basic version is preserved inside the `basic_converter` folder because it represents the starting point of the project.

---

## 📚 What I Learned

While building this project, I practiced:

* Python strings
* `replace()`
* Dictionaries
* JSON
* File handling
* Python functions
* Flask
* HTML forms
* Jinja templates
* CSS layouts
* JavaScript DOM manipulation
* Browser local storage
* Clipboard API
* Git and GitHub
* Structuring a web application

---

## 🎯 Purpose of the Project

The goal of this project was not only to build an emoji converter, but also to understand how a simple Python program can gradually become a complete web application.

It started with a simple question:

> **Can I replace text shortcuts with emojis using Python?**

That small idea eventually became a Flask-based interactive application.

---

## 🔮 Future Improvements

Possible future improvements include:

* Adding more emoji categories
* Improving emoji search
* User-customized shortcuts
* Recently used emojis
* Better mobile UI
* Additional customization options
* API support

---

## 👩‍💻 Author

**Shakun Sharma**

B.Tech Computer Science & Engineering

Built while learning Python, Flask, web development, and Git/GitHub.

---

## ❤️ Final Note

This project started as a small Python practice program and grew into a complete application.

It represents the process of learning by building, improving, testing, and gradually adding new ideas.

**Built with Python + Flask ❤️**
