# Quiz Score Manager — README

A clean, professional **Quiz Score Manager** application built using Python for backend logic, JSON for data storage, and a simple GUI.

---

## 1. Overview

This project allows you to manage student quiz scores efficiently. It supports adding, updating, deleting, and searching for students and their subject scores, along with generating rankings and subject-wise statistics.

---

## 2. Features

* Add new students (auto-generated ID)
* Update existing scores
* Delete students or specific subject entries
* Search by student name (partial match supported)
* Generate leaderboard (ranked by total score)
* Find highest scorer per subject
* Calculate average score per subject
* Simple dark-themed frontend interface
* JSON-based persistent storage

---

## 3. Project Structure

```
quiz_manager/
│
├── main.py                     # Entry point (runs the menu)
├── gui.py                      # GUI
│
├── data/
│   └── quiz_data.json          # JSON database file
│
├── utils/
│   ├── validators.py           # Input validation helpers
│   └── file_ops.py             # File checks, safe creation
│
├── core/
│   ├── student_ops.py          # Add / delete / search students
│   ├── score_ops.py            # Add / update / delete scores
│   ├── report_ops.py           # Stats: averages, highest scorer
│   └── ranking_ops.py          # Leaderboard, ranking logic
│
└── menu/
    └── menu.py                 # CLI menu handling
```

---


## 4. Example JSON Structure

```
{
  "students": {
    "1": {
      "name": "Bastab Gogoi",
      "scores": {
        "Math": 10,
        "English": 9
      }
    }
  }
}
```

---

## 5. Possible Future Enhancements

* Database integration (SQLite / PostgreSQL)
* CSV export for reports
* Login system for authentication
* Light/dark theme toggle
* Student dashboard view

---


## 6. License

This project is licensed under the **MIT License**.

---

A clean, modular, and minimal project to practice structured development using Python and web technologies.
