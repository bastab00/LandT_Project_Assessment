import tkinter as tk
from tkinter import messagebox, simpledialog
from utils.file_ops import load_data, save_data
from core.student_ops import add_new_student, delete_student
from core.score_ops import update_student_score
from core.report_ops import student_performance_report
from core.ranking_ops import ranking_leaderboard


class QuizGUI:
    def __init__(self):
        self.data = load_data()

        self.win = tk.Tk()
        self.win.title("Quiz Score Manager")
        self.win.geometry("350x350")
        self.win.resizable(False, False)

        title = tk.Label(self.win, text="Quiz Score Manager", font=("Arial", 16))
        title.pack(pady=10)

        tk.Button(self.win, text="Add Student", width=25, command=self.add_student).pack(pady=5)
        tk.Button(self.win, text="Update Score", width=25, command=self.update_score).pack(pady=5)
        tk.Button(self.win, text="Delete Student", width=25, command=self.delete_student).pack(pady=5)
        tk.Button(self.win, text="Student Report", width=25, command=self.student_report).pack(pady=5)
        tk.Button(self.win, text="Leaderboard", width=25, command=self.leaderboard).pack(pady=5)
        tk.Button(self.win, text="Save & Exit", width=25, command=self.save_and_exit).pack(pady=15)

        self.win.mainloop()

    # ---- GUI Button Actions -----

    def add_student(self):
        name = simpledialog.askstring("Add Student", "Enter student name:")
        if not name:
            return
        name = name.title()

        sid = self.data["next_id"]
        self.data["students"][str(sid)] = {"name": name, "scores": {}}
        self.data["next_id"] += 1

        save_data(self.data)
        messagebox.showinfo("Success", f"Added {sid} - {name}")

    def update_score(self):
        sid = simpledialog.askstring("Update Score", "Enter student ID:")
        if not sid or sid not in self.data["students"]:
            messagebox.showerror("Error", "Student ID not found.")
            return

        sub = simpledialog.askstring("Subject", "Enter subject name:")
        if not sub:
            return
        sub = sub.title()

        try:
            score = int(simpledialog.askstring("Score", "Enter score (0-10):"))
        except:
            messagebox.showerror("Error", "Invalid score.")
            return

        if score < 0 or score > 10:
            messagebox.showerror("Error", "Score must be 0-10.")
            return

        self.data["students"][sid]["scores"][sub] = score
        save_data(self.data)
        messagebox.showinfo("Success", "Score updated successfully!")

    def delete_student(self):
        sid = simpledialog.askstring("Delete", "Enter student ID:")
        if not sid:
            return

        if sid not in self.data["students"]:
            messagebox.showerror("Error", "ID not found.")
            return

        del self.data["students"][sid]
        save_data(self.data)
        messagebox.showinfo("Deleted", "Student deleted successfully.")

    def student_report(self):
        sid = simpledialog.askstring("Report", "Enter student ID:")
        if not sid or sid not in self.data["students"]:
            messagebox.showerror("Error", "ID not found.")
            return

        info = self.data["students"][sid]
        scores = info["scores"]

        if not scores:
            messagebox.showinfo("Report", "This student has no scores.")
            return

        avg = sum(scores.values()) / len(scores)
        highest = max(scores.items(), key=lambda x: x[1])
        lowest = min(scores.items(), key=lambda x: x[1])

        msg = (
            f"Name: {info['name']}\n"
            f"Avg Score: {avg:.2f}\n"
            f"Highest: {highest[0]} ({highest[1]})\n"
            f"Lowest: {lowest[0]} ({lowest[1]})"
        )

        messagebox.showinfo("Student Report", msg)

    def leaderboard(self):
        avgs = []
        for sid, info in self.data["students"].items():
            scores = [v for v in info["scores"].values() if isinstance(v, int)]
            if scores:
                avgs.append((sid, info["name"], sum(scores) / len(scores)))

        if not avgs:
            messagebox.showinfo("Leaderboard", "No score data available.")
            return

        avgs.sort(key=lambda x: x[2], reverse=True)

        msg = ""
        for i, (sid, name, avg) in enumerate(avgs, start=1):
            msg += f"{i}. {sid} - {name}: {avg:.2f}\n"

        messagebox.showinfo("Leaderboard", msg)

    def save_and_exit(self):
        save_data(self.data)
        self.win.destroy()


if __name__ == "__main__":
    QuizGUI()
