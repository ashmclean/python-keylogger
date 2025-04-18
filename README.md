# 🛡️ Python Keylogger with Email Reporting (Educational Only)

## 📌 Overview  
This project is a **simple keylogger built in Python** that captures user keystrokes and emails the log file to a specified address at scheduled intervals. It was created strictly for **educational and ethical** purposes to deepen understanding of how keyloggers work and how to defend against them.

> ⚠️ **Ethical Use Only:** Do **not** run this script on any machine you don’t own or without full consent. Misuse can be illegal.

---

## 🎯 Objectives
- Learn the basics of keyboard monitoring using Python
- Experiment with secure emailing and background process automation

---

## 🔧 Features
- Captures and stores keystrokes
- Emails the captured log file at scheduled intervals
- Runs silently in the background

---

## 🧰 Tech Stack
- Python 3
- `pynput` for key capture
- `smtplib` and `email` for sending emails
- `threading.Timer` for scheduled tasks

---

## 🚀 Setup & Usage

### 1. **Install dependencies**
```bash
pip install pynput
