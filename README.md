# Password Strength Checker

A simple Python command-line tool that checks the strength of a password based on common security rules.

## Features

- Checks password length
- Detects uppercase letters
- Detects numbers
- Detects special characters
- Classifies passwords as **Weak**, **Medium**, or **Strong**

## Technologies Used

- Python
- Regular Expressions (`re` module)

## How It Works

The program evaluates a password using the following rules:

- Password length should be **at least 8 characters**
- Contains **uppercase letters (A-Z)**
- Contains **numbers (0-9)**
- Contains **special characters (!@#$%^&*)**

Based on how many conditions are satisfied, the password is classified as:

| Score | Result |
|------|------|
| 0–1 | Weak Password |
| 2 | Medium Password |
| 3–4 | Strong Password |

## How to Run

1. Clone the repository
