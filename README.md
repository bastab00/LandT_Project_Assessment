📘 Quiz Score Manager

A Python mini-project designed to practice Functions, Dictionaries, Sets, File Handling, and JSON storage.
This program allows you to add, update, view, and analyze quiz scores for multiple students.

🔧 Features
✅ 1. Add / Update Quiz Score

Each student is automatically assigned a unique Student ID.

You can record quiz scores for any subject.

If the student already exists (matched by name), the system updates the record.

✅ 2. Show All Records

Displays a clean list of all students:

Their name

Their unique ID

All subjects with scores

✅ 3. Highest Scorer Report

Finds the highest scorer(s) across all subjects.

Supports ties (multiple toppers).

Uses set logic to remove duplicate subjects.

✅ 4. Persistent JSON Storage

All data is stored in students.json.

Automatically loads saved data when the program starts.

Automatically saves updated data when exiting.

📂 Project Structure
QuizScoreManager/
│
├── main.py
├── students.json   (auto-generated after first save)
└── README.md

🧠 Concepts Used
📌 1. Dictionaries

Used for storing student profiles in this structure:

{
  "id_101": {
    "name": "Aman",
    "scores": {"Math": 9, "English": 8}
  }
}

📌 2. Sets

Used to collect unique subjects and avoid repetition.

📌 3. Functions

Modular code with functions for:

Loading JSON

Saving JSON

Adding a student

Updating scores

Displaying all data

Generating reports

📌 4. File Handling

Safe reading and writing using:

json.load()
json.dump()

▶️ How to Run

Open terminal / PowerShell

Navigate to the project folder

Run the file:

python main.py

📝 Example Interaction
==== Quiz Score Manager ====
1. Add/Update Quiz Score
2. Show All Scores
3. Highest Scorer Report
4. Save & Exit
Enter choice: 1

Student name: Aman
Subject: Math
Score: 9
✔ Score updated successfully!

💾 JSON Storage Example (students.json)
{
  "id_101": {
    "name": "Aman",
    "scores": {
      "Math": 9,
      "English": 8
    }
  },
  "id_102": {
    "name": "Riya",
    "scores": {
      "Science": 10
    }
  }
}

🛡️ Error Handling Included

Invalid choices

Non-numeric score

Score out of range

Empty input

File not found (auto-creates new file)

Safe overwrite of existing data

🎯 Learning Outcome

By completing this project, you clearly understand:

✔ How to use sets to collect unique values
✔ How to use dictionaries for structured data
✔ How to write modular code using functions
✔ How to handle JSON files
✔ How to build small but practical backend tools
