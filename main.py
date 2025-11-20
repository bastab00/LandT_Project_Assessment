#!/usr/bin/env python3
"""
Quiz Score Manager — mid-sized version (JSON storage)
Features:
- JSON storage with automatic ID management
- Add new student (auto ID)
- Update student scores (by ID)
- Delete student
- Delete subject score for a student
- Search student by name (partial)
- Average score per subject
- Student performance report
- Highest scorer per subject
- Ranking / Leaderboard
- Robust input validation and safe file handling
"""

import json
import os
import sys
from typing import Dict, Tuple, Optional

DATA_FILE = "quiz_data.json"
ID_START = 101


# ----------------------- Data helpers -----------------------
def load_data() -> Dict:
    """Load JSON data; if missing or corrupted, create base structure."""
    base = {"next_id": ID_START, "students": {}}
    if not os.path.exists(DATA_FILE):
        return base
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Basic validation
        if not isinstance(data, dict):
            raise ValueError("Bad format")
        if "next_id" not in data or "students" not in data:
            raise ValueError("Missing keys")
        if not isinstance(data["students"], dict):
            raise ValueError("Bad students")
        # Ensure next_id is int
        if not isinstance(data.get("next_id", None), int):
            data["next_id"] = ID_START
        return data
    except Exception as e:
        print("Warning: data file missing/corrupted. Creating a new dataset.")
        return base


def save_data(data: Dict) -> None:
    """Save data to JSON file safely."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("Error: could not save data:", e)


def subjects_set(data: Dict) -> set:
    """Return set of all subjects present in dataset."""
    s = set()
    for stud in data["students"].values():
        for sub in stud.get("scores", {}).keys():
            s.add(sub)
    return s


# ----------------------- Input validation -----------------------
def input_nonempty(prompt: str) -> str:
    while True:
        v = input(prompt).strip()
        if v == "":
            print("Input cannot be empty. Try again.")
        else:
            return v


def input_choice(prompt: str, choices: Tuple[str, ...]) -> str:
    v = input(prompt).strip()
    return v if v in choices else ""


def input_int(prompt: str, min_val: Optional[int] = None, max_val: Optional[int] = None) -> Optional[int]:
    v = input(prompt).strip()
    if v == "":
        return None
    if not v.lstrip("-").isdigit():
        return None
    n = int(v)
    if min_val is not None and n < min_val:
        return None
    if max_val is not None and n > max_val:
        return None
    return n


def validate_subject(sub: str) -> bool:
    """Allow letters and spaces only for subject names."""
    if sub == "":
        return False
    return sub.replace(" ", "").isalpha()


# ----------------------- Core features -----------------------
def add_new_student(data: Dict) -> None:
    name = input_nonempty("Enter new student name: ").title()
    sid = data["next_id"]
    data["students"][str(sid)] = {"name": name, "scores": {}}
    data["next_id"] = sid + 1
    save_data(data)
    print(f"Added student: {sid} - {name}")


def update_student_score(data: Dict) -> None:
    if not data["students"]:
        print("No students available. Add a student first.")
        return
    show_students_brief(data)
    sid = input_nonempty("Enter student ID to update: ").strip()
    if sid not in data["students"]:
        print("Student ID not found.")
        return
    student = data["students"][sid]
    print(f"Selected: {sid} - {student['name']}")
    # enter subject
    while True:
        subject = input_nonempty("Enter subject name (letters & spaces): ").title()
        if not validate_subject(subject):
            print("Invalid subject name. Use letters and spaces only.")
            continue
        break
    # enter score
    score = input_int("Enter score (0 - 10): ", 0, 10)
    if score is None:
        print("Invalid score. Must be an integer between 0 and 10.")
        return
    student["scores"][subject] = score
    save_data(data)
    print(f"Updated {student['name']} → {subject}: {score}")


def quick_update_by_id(data: Dict) -> None:
    """Prompt ID, subject, score and update (used for quick scripts)."""
    if not data["students"]:
        print("No students available.")
        return
    sid = input_nonempty("Enter student ID: ").strip()
    if sid not in data["students"]:
        print("ID not found.")
        return
    subject = input_nonempty("Enter subject name: ").title()
    if not validate_subject(subject):
        print("Invalid subject.")
        return
    score = input_int("Enter score (0 - 10): ", 0, 10)
    if score is None:
        print("Invalid score.")
        return
    data["students"][sid]["scores"][subject] = score
    save_data(data)
    print("Score saved.")


def delete_student(data: Dict) -> None:
    if not data["students"]:
        print("No students to delete.")
        return
    show_students_brief(data)
    sid = input_nonempty("Enter student ID to delete (or 'c' to cancel): ").strip()
    if sid.lower() == "c":
        print("Cancelled.")
        return
    if sid not in data["students"]:
        print("Student ID not found.")
        return
    confirm = input_choice(f"Confirm delete {sid} - {data['students'][sid]['name']}? (y/n): ", ("y", "n"))
    if confirm == "y":
        del data["students"][sid]
        save_data(data)
        print("Student deleted.")
    else:
        print("Cancelled.")


def delete_subject_for_student(data: Dict) -> None:
    if not data["students"]:
        print("No students available.")
        return
    show_students_brief(data)
    sid = input_nonempty("Enter student ID: ").strip()
    if sid not in data["students"]:
        print("Student ID not found.")
        return
    stud = data["students"][sid]
    if not stud["scores"]:
        print("This student has no scores.")
        return
    print(f"Subjects for {sid} - {stud['name']}:")
    for s in stud["scores"].keys():
        print(" -", s)
    subject = input_nonempty("Enter subject to remove: ").title()
    if subject not in stud["scores"]:
        print("Subject not found for this student.")
        return
    confirm = input_choice(f"Confirm delete {subject} for {stud['name']}? (y/n): ", ("y", "n"))
    if confirm == "y":
        del stud["scores"][subject]
        save_data(data)
        print("Subject removed.")
    else:
        print("Cancelled.")


def show_all_details(data: Dict) -> None:
    if not data["students"]:
        print("No records.")
        return
    print("\nAll students and scores:")
    for sid in sorted(data["students"].keys(), key=lambda x: int(x)):
        info = data["students"][sid]
        print(f"{sid} | {info['name']}")
        if not info["scores"]:
            print("   (no scores)")
        else:
            for sub, sc in info["scores"].items():
                print(f"   {sub}: {sc}")
    print()


def show_students_brief(data: Dict) -> None:
    if not data["students"]:
        print("No students.")
        return
    print("\nStudents:")
    for sid in sorted(data["students"].keys(), key=lambda x: int(x)):
        print(f"{sid} - {data['students'][sid]['name']}")
    print()


def average_per_subject(data: Dict) -> None:
    subs = {}
    for info in data["students"].values():
        for sub, sc in info.get("scores", {}).items():
            subs.setdefault(sub, []).append(sc)
    if not subs:
        print("No subjects recorded yet.")
        return
    print("\nAverage score per subject:")
    for sub in sorted(subs.keys()):
        scores = subs[sub]
        avg = sum(scores) / len(scores)
        print(f"{sub} → {avg:.2f}  (n={len(scores)})")
    print()


def student_performance_report(data: Dict) -> None:
    if not data["students"]:
        print("No students.")
        return
    show_students_brief(data)
    sid = input_nonempty("Enter student ID for report: ").strip()
    if sid not in data["students"]:
        print("Student ID not found.")
        return
    info = data["students"][sid]
    scores = info.get("scores", {})
    if not scores:
        print("This student has no scores.")
        return
    total = sum(scores.values())
    count = len(scores)
    avg = total / count
    highest = max(scores.items(), key=lambda x: x[1])
    lowest = min(scores.items(), key=lambda x: x[1])
    print(f"\nReport for {sid} - {info['name']}:")
    print(f"Total subjects: {count}")
    print(f"Average score: {avg:.2f}")
    print(f"Highest: {highest[0]} ({highest[1]})")
    print(f"Lowest: {lowest[0]} ({lowest[1]})")
    print()


def search_student_by_name(data: Dict) -> None:
    q = input_nonempty("Enter name to search (partial allowed): ").lower()
    found = []
    for sid, info in data["students"].items():
        if q in info["name"].lower():
            found.append((sid, info["name"]))
    if not found:
        print("No matches found.")
        return
    print("\nMatches:")
    for sid, name in found:
        print(f"{sid} - {name}")
    print()


def highest_scorer_per_subject(data: Dict) -> None:
    subjects = sorted(subjects_set(data))
    if not subjects:
        print("No subjects recorded.")
        return
    print("\nHighest scorers per subject:")
    for sub in subjects:
        best = None
        best_score = -1
        for info in data["students"].values():
            sc = info.get("scores", {}).get(sub)
            if sc is not None and sc > best_score:
                best_score = sc
                best = info["name"]
        if best is not None:
            print(f"{sub}: {best} ({best_score})")
        else:
            print(f"{sub}: No entries")
    print()


def ranking_leaderboard(data: Dict, top_n: int = 10) -> None:
    averages = []
    for sid, info in data["students"].items():
        scores = list(info.get("scores", {}).values())
        if scores:
            averages.append((sid, info["name"], sum(scores) / len(scores)))
    if not averages:
        print("No score data to rank.")
        return
    averages.sort(key=lambda x: x[2], reverse=True)
    print("\nLeaderboard (by average score):")
    for i, (sid, name, avg) in enumerate(averages[:top_n], start=1):
        print(f"{i}. {sid} - {name}: {avg:.2f}")
    print()


# ----------------------- CLI Menu -----------------------
def main_menu():
    data = load_data()
    # if load created new base structure, immediately save to create file
    if not os.path.exists(DATA_FILE):
        save_data(data)

    while True:
        print("\n==== Quiz Score Manager ====")
        print("1. Add New Student")
        print("2. Add / Update Student Score")
        print("3. Quick Update by ID (subject & score)")
        print("4. Delete a Student")
        print("5. Delete a Subject Score (for a student)")
        print("6. Show All Scores")
        print("7. Highest Scorer Per Subject")
        print("8. Average Score Per Subject")
        print("9. Student Performance Report")
        print("10. Search Student By Name")
        print("11. Ranking / Leaderboard")
        print("12. Save & Exit")
        print("13. Exit without saving")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_new_student(data)
        elif choice == "2":
            update_student_score(data)
        elif choice == "3":
            quick_update_by_id(data)
        elif choice == "4":
            delete_student(data)
        elif choice == "5":
            delete_subject_for_student(data)
        elif choice == "6":
            show_all_details(data)
        elif choice == "7":
            highest_scorer_per_subject(data)
        elif choice == "8":
            average_per_subject(data)
        elif choice == "9":
            student_performance_report(data)
        elif choice == "10":
            search_student_by_name(data)
        elif choice == "11":
            ranking_leaderboard(data)
        elif choice == "12":
            save_data(data)
            print("Saved. Goodbye!")
            break
        elif choice == "13":
            print("Exiting without saving changes (if any). Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 13.")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        try:
            sys.exit(0)
        except SystemExit:
            pass
