# Quiz Score Manager

A Python-based mini-project designed to practice **JSON file handling**, **functions**, **dictionaries**, and **sets**.
The program allows you to record, update, and analyze quiz scores for multiple students using auto-generated Student IDs.

---

## Features

### 1. Add or Update Quiz Score

* Each student receives an automatic **Student ID**.
* If a student already exists (matched by name), their scores update.
* Supports multiple subjects per student.

### 2. View All Records

* Displays all students along with:

  * Student ID
  * Name
  * Subjects and scores

### 3. Highest Scorer Report

* Finds highest scorer(s) across all subjects.
* Supports tie conditions.
* Uses sets to track unique subjects.

### 4. Persistent JSON Storage

* Data is stored in `quiz_data.json`.
* Automatically loads previous data when the program starts.
* Automatically saves data when exiting.

---

## Project Structure

```
QuizScoreManager/
│
├── main.py
├── quiz_data.json   (generated automatically)
└── README.md
```

---

## Concepts Covered

* **Dictionaries** for structured student data
* **Sets** for unique subjects
* **Functions** for modular design
* **JSON File Handling** for persistent storage

---

## How to Run

1. Open a terminal or PowerShell
2. Navigate to the project folder
3. Run:

```
python main.py
```

---

## Sample JSON (quiz_data.json)

```json
{
  "id_101": {
    "name": "Bastab",
    "scores": {
      "Math": 9,
      "English": 8
    }
  },
  "id_102": {
    "name": "Sibga",
    "scores": {
      "Science": 10
    }
  }
}
```

---

## Example Console Output

```
==== Quiz Score Manager ====
1. Add/Update Quiz Score
2. Show All Scores
3. Highest Scorer Report
4. Save & Exit
Enter choice: 1

Student name: Bastab
Subject: Math
Score: 9
Score saved successfully!
```

---

## Error Handling

The program safely handles:

* Invalid menu choices
* Empty name/subject inputs
* Non-numeric score inputs
* Score not in 0–10 range
* Corrupted or missing JSON files
* Duplicate student names (auto-updates)

---

## Learning Outcomes

By completing this project, you learn:

* How dictionaries and nested structures work
* How sets automatically avoid duplicate entries
* How to build modular programs with functions
* How to store and load persistent data with JSON
* How to create a clean, usable Python console application

---

## License

This project is free to use for learning and practice.

---
