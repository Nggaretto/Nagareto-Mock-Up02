import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

def login():
    global user_id_entry, password_entry, login_window
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("400x300")
    login_window.configure(bg="#F8F8F8")

    tk.Label(login_window, text="Kemet NMU ERP System", font=("Arial", 18, "bold"), fg="maroon", bg="#F8F8F8").pack()
    tk.Label(login_window, text="User ID", font=("Arial", 12), bg="#F8F8F8").pack()
    user_id_entry = tk.Entry(login_window)
    user_id_entry.pack()

    tk.Label(login_window, text="Password", font=("Arial", 12), bg="#F8F8F8").pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    tk.Button(login_window, text="Login", command=check_login, bg="maroon", fg="white").pack(pady=10)
    login_window.mainloop()

def check_login():
    user_id = user_id_entry.get()
    password = password_entry.get()

    if user_id == "223101022" and password == "0000":
        login_window.destroy()
        open_dashboard("Moawad El-Kholy", "President of NMU")
    else:
        messagebox.showerror("Error", "Invalid ID or Password")

def open_dashboard(username, role):
    dashboard = tk.Tk()
    dashboard.title("Dashboard")
    dashboard.geometry("1000x700")
    dashboard.configure(bg="#F8F8F8")

    tk.Label(dashboard, text="Kemet NMU", font=("Arial", 22, "bold"), fg="maroon", bg="#F8F8F8").pack()
    tk.Label(dashboard, text=username, font=("Arial", 18, "bold"), bg="#F8F8F8").pack()
    tk.Label(dashboard, text=role, font=("Arial", 14), bg="#F8F8F8").pack()

    tk.Label(dashboard, text="__________________________________", fg="black", bg="#F8F8F8").pack()

    tk.Button(dashboard, text="Student Performance Reports", width=30, height=2, command=open_student_reports, bg="maroon", fg="white").pack(pady=10)
    tk.Button(dashboard, text="Enrollment & Fees Report", width=30, height=2, command=open_fees_report, bg="gray", fg="white").pack(pady=10)
    tk.Button(dashboard, text="Professor Attendance Report", width=30, height=2, command=open_professor_attendance, bg="gray", fg="white").pack(pady=10)
    tk.Button(dashboard, text="Student Activities Report", width=30, height=2, command=open_student_activities, bg="gray", fg="white").pack(pady=10)

    tk.Button(dashboard, text="Logout", width=30, height=2, command=dashboard.destroy, bg="red", fg="white").pack(pady=10)

def open_student_reports():
    report_window = tk.Toplevel()
    report_window.title("Student Reports")
    report_window.geometry("900x600")
    report_window.configure(bg="#F8F8F8")

    tk.Label(report_window, text="Student Performance", font=("Arial", 16, "bold"), fg="maroon", bg="#F8F8F8").pack()

    faculties = ["Business", "Medicine", "Engineering", "Science", "Computer Science", "Pharmacy", "Dentistry", "Health Sciences"]

    faculty_frame = tk.Frame(report_window, bg="#F8F8F8")
    faculty_frame.pack(pady=10)

    for i in range(0, len(faculties), 2):
        row_frame = tk.Frame(faculty_frame, bg="#F8F8F8")
        row_frame.pack()
        for j in range(2):
            if i + j < len(faculties):
                tk.Button(row_frame, text=faculties[i + j], width=15, height=2, command=lambda f=faculties[i + j]: show_faculty_students(f), bg="gray", fg="white").pack(side=tk.LEFT, padx=10, pady=5)

    tk.Button(report_window, text="Back", command=report_window.destroy, bg="maroon", fg="white").pack(pady=10)

def show_faculty_students(faculty):
    students = {
        "Business": [("223101035", "Abdelrahman Allam", 2.0),
                      ("223101045", "Mohamed Ibrahim Al-Bahloul", 3.7)]
    }

    student_window = tk.Toplevel()
    student_window.title(f"{faculty} Students")
    student_window.geometry("900x600")
    student_window.configure(bg="#F8F8F8")

    tk.Label(student_window, text=f"{faculty} Student Performance", font=("Arial", 16, "bold"), fg="maroon", bg="#F8F8F8").pack()

    tk.Button(student_window, text="Back", command=student_window.destroy, bg="maroon", fg="white").pack(pady=10)

def open_fees_report():
    messagebox.showinfo("Enrollment & Fees Report", "Displaying Enrollment & Fees Report... Including payment details.")

def open_professor_attendance():
    messagebox.showinfo("Professor Attendance Report", "Displaying Professor Attendance Report...")

def open_student_activities():
    messagebox.showinfo("Student Activities Report", "Displaying Student Activities Report under the supervision of Yasmen El Tahan...")
    activity_window = tk.Toplevel()
    activity_window.title("Student Activities")
    activity_window.geometry("900x600")
    activity_window.configure(bg="#F8F8F8")

    tk.Label(activity_window, text="Activities Overview", font=("Arial", 16, "bold"), fg="maroon", bg="#F8F8F8").pack()
    tk.Button(activity_window, text="Back", command=activity_window.destroy, bg="maroon", fg="white").pack(pady=10)

login()  
