from utils.validators import input_nonempty
from core.student_ops import show_students_brief

def student_performance_report(data):
    if not data["students"]:
        print("No students.")
        return

    show_students_brief(data)
    sid = input_nonempty("ID for report: ").strip()

    if sid not in data["students"]:
        print("ID not found.")
        return

    scores = data["students"][sid]["scores"]
    if not scores:
        print("No scores.")
        return

    avg = sum(scores.values()) / len(scores)
    highest = max(scores.items(), key=lambda x: x[1])
    lowest = min(scores.items(), key=lambda x: x[1])

    print(f"\nReport for {data['students'][sid]['name']}:")
    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)
