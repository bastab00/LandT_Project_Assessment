from utils.validators import input_nonempty, input_int, validate_subject
from utils.file_ops import save_data
from core.student_ops import show_students_brief

def update_student_score(data):
    if not data["students"]:
        print("No students.")
        return
    
    show_students_brief(data)
    sid = input_nonempty("Enter student ID: ").strip()

    if sid not in data["students"]:
        print("Not found.")
        return

    subject = input_nonempty("Enter subject: ").title()
    if not validate_subject(subject):
        print("Invalid subject.")
        return

    score = input_int("Enter score (0-10): ", 0, 10)
    if score is None:
        print("Invalid score.")
        return

    data["students"][sid]["scores"][subject] = score
    save_data(data)
    print("Score updated.")
