# 🌍 Google Translator Desktop App

A modern desktop application built with **Python**, **Tkinter**, and **Google Translate API (`googletrans`)** that allows users to translate text between more than **100 languages** with automatic language detection.

---

## ✨ Features

- 🌐 Translate text between 100+ languages
- 🔍 Automatic language detection
- 🔄 Swap source and destination languages
- 🧹 Clear input/output with one click
- 🖥️ Simple and responsive desktop GUI
- ⚡ Built using asynchronous programming (`asyncio`)
- 📦 Modular project architecture
- 🛠️ Easy to extend with additional features

---

# Project Structure

```
translator/
│
├── main.py
│
├── services/
│   └── translator_service.py
│
├── ui/
│   ├── app.py
│   └── callbacks.py
│
├── utils/
│   └── languages.pyb
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# Technologies Used

- Python 3.13+
- Tkinter
- asyncio
- googletrans
- uv (Package Manager)

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/google-translator.git

cd google-translator
```

---

## Create Virtual Environment

Using **uv**

```bash
uv venv
```

Activate it

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
uv sync
```

or

```bash
uv add googletrans
```

---

## Run Application

```bash
uv run python main.py
```

---

# How It Works

The application follows a modular architecture.

```
User
   │
   ▼
Tkinter UI
   │
   ▼
Callbacks
   │
   ▼
Translation Service
   │
   ▼
Google Translate
```

---

# Translation Flow

### User enters text

```
Hello
```

↓

### Select language

```
Source : Auto Detect

Destination : Hindi
```

↓

### Translation Service

```python
await translator.translate(
    text,
    dest="hi",
)
```

↓

### Google detects language

```
English
```

↓

### Returns

```
नमस्ते
```

↓

Displayed inside the output text box.

---

# Auto Detect

When **Auto Detect** is selected, the application does **not** specify the source language.

```python
await translator.translate(
    text,
    dest=destination,
)
```

Google Translate automatically detects the source language and returns it in

```python
result.src
```

### Example

**Source Language:** Auto Detect  
**Destination Language:** English

**Input**

```text
Bonjour
```

⬇️ **Google automatically detects the language**

```text
French
```

⬇️ **Translation Result**

```text
Hello
```

---

# Asynchronous Translation

The latest version of **googletrans** is asynchronous.

Instead of

```python
translator.translate(...)
```

the application uses

```python
await translator.translate(...)
```

The async function is executed using

```python
asyncio.run(...)
```

This prevents blocking the GUI during translation requests.

---

# Supported Languages

The application supports every language available in

```python
googletrans.LANGUAGES
```

Examples

- English
- Hindi
- Japanese
- Korean
- Chinese
- French
- German
- Spanish
- Russian

and many more.

---

# Features Explained

## Translate

Translates the entered text into the selected destination language.

---

## Auto Detect

Automatically identifies the language before translation.

---

## Swap

Swaps

- Source language
- Destination language
- Input text
- Output text

making reverse translation easy.

---

## Clear

Clears

- Input text
- Output text
- Detected language label

---

# Error Handling

The application handles

- Empty input
- No destination language selected
- Network errors
- Translation failures
- Invalid requests

using Tkinter message boxes.


# Learning Outcomes

This project demonstrates

- Tkinter GUI development
- Async programming with asyncio
- API integration
- Modular Python architecture
- Event-driven programming
- Error handling
- Python package management using uv

---

# Contributing

Contributions are welcome.

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# License

This project is licensed under the MIT License.

---

# Author

**Raushan Bhanu**

GitHub:
https://github.com/RaushanBhanu

LinkedIn:
https://linkedin.com/in/raushan-bhanu

---

⭐ If you found this project useful, consider giving it a star on GitHub!