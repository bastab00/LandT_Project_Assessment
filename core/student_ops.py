from utils.validators import input_nonempty
from utils.file_ops import save_data

def show_students_brief(data):
    print("\nStudents:")
    for sid, info in sorted(data["students"].items()):
        print(f"{sid} - {info['name']}")
    print()

def add_new_student(data):
    name = input_nonempty("Enter name: ").title()
    sid = data["next_id"]
    data["students"][str(sid)] = {"name": name, "scores": {}}
    data["next_id"] += 1
    save_data(data)
    print(f"Added {sid}: {name}")

def delete_student(data):
    if not data["students"]:
        print("No students.")
        return

    show_students_brief(data)
    sid = input_nonempty("Enter ID to delete: ").strip()

    if sid not in data["students"]:
        print("ID not found.")
        return

    del data["students"][sid]
    save_data(data)
    print("Student deleted.")
