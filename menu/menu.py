from utils.file_ops import load_data
from core.student_ops import add_new_student, delete_student
from core.score_ops import update_student_score
from core.report_ops import student_performance_report
from core.ranking_ops import ranking_leaderboard

def main_menu():
    data = load_data()

    while True:
        print("\n==== Quiz Score Manager ====")
        print("1. Add Student")
        print("2. Update Score")
        print("3. Delete Student")
        print("4. Student Report")
        print("5. Leaderboard")
        print("6. Exit")

        ch = input("Enter choice: ").strip()

        if ch == "1":
            add_new_student(data)
        elif ch == "2":
            update_student_score(data)
        elif ch == "3":
            delete_student(data)
        elif ch == "4":
            student_performance_report(data)
        elif ch == "5":
            ranking_leaderboard(data)
        elif ch == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
