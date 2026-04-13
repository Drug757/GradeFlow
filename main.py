# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox, ttk

class GradeFlowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GradeFlow - Калькулятор оценок")
        self.root.geometry("1024x768")
        self.root.resizable(False, False)
        
        self.subject_entries = []
        self.grade_entries = []
        
        title = tk.Label(root, text="Калькулятор среднего балла", 
                        font=("Arial", 16, "bold"))
        title.pack(pady=15)
        
        count_frame = tk.Frame(root)
        count_frame.pack(pady=5)
        
        tk.Label(count_frame, text="Количество предметов:", 
                font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
        
        self.count_var = tk.StringVar(value="3")
        self.count_entry = tk.Entry(count_frame, textvariable=self.count_var, 
                                   width=5, font=("Arial", 11))
        self.count_entry.pack(side=tk.LEFT)
        
        tk.Button(count_frame, text="Создать поля", 
                 command=self.create_fields, bg="#4CAF50", fg="white",
                 font=("Arial", 10)).pack(side=tk.LEFT, padx=10)
        
        ttk.Separator(root, orient='horizontal').pack(fill='x', padx=20, pady=10)
        
        self.canvas = tk.Canvas(root, height=250)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True, padx=(20, 0))
        self.scrollbar.pack(side="right", fill="y", padx=(0, 20))
        
        self.calc_btn = tk.Button(root, text="Рассчитать средний балл", 
                                  command=self.calculate, bg="#2196F3", fg="white",
                                  font=("Arial", 12, "bold"), height=2)
        self.calc_btn.pack(pady=15, padx=30, fill='x')
        
        self.result_label = tk.Label(root, text="", font=("Arial", 13), fg="#333")
        self.result_label.pack(pady=5)
        
        self.create_fields()
    
    def create_fields(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        self.subject_entries.clear()
        self.grade_entries.clear()
        
        try:
            count = int(self.count_var.get())
            if count <= 0:
                messagebox.showwarning("Предупреждение", "Количество должно быть больше 0")
                count = 3
                self.count_var.set("3")
            if count > 20:
                messagebox.showwarning("Предупреждение", "Максимум 20 предметов")
                count = 20
                self.count_var.set("20")
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целое число")
            count = 3
            self.count_var.set("3")
        
        header_frame = tk.Frame(self.scrollable_frame)
        header_frame.pack(fill='x', pady=5)
        tk.Label(header_frame, text="Предмет", font=("Arial", 10, "bold"), 
                width=25, anchor='w').pack(side=tk.LEFT, padx=5)
        tk.Label(header_frame, text="Оценка (1-5)", font=("Arial", 10, "bold"), 
                width=10, anchor='w').pack(side=tk.LEFT, padx=5)
        
        for i in range(count):
            frame = tk.Frame(self.scrollable_frame)
            frame.pack(fill='x', pady=2)
            
            tk.Label(frame, text=f"{i+1}.", width=3).pack(side=tk.LEFT)
            
            subj_entry = tk.Entry(frame, width=25, font=("Arial", 10))
            subj_entry.pack(side=tk.LEFT, padx=5)
            subj_entry.insert(0, f"Предмет {i+1}")
            self.subject_entries.append(subj_entry)
            
            grade_entry = tk.Entry(frame, width=10, font=("Arial", 10))
            grade_entry.pack(side=tk.LEFT, padx=5)
            grade_entry.insert(0, "5")
            self.grade_entries.append(grade_entry)
    
    def calculate_average(self, grades):
        if not grades:
            return 0
        return sum(grades) / len(grades)
    
    def get_letter_grade(self, avg):
        if avg >= 4.5:
            return "Отлично (A)"
        elif avg >= 3.5:
            return "Хорошо (B)"
        elif avg >= 2.5:
            return "Удовлетворительно (C)"
        else:
            return "Неудовлетворительно (D)"
    
    def calculate(self):
        grades = []
        subjects = []
        
        for i, (subj_entry, grade_entry) in enumerate(zip(self.subject_entries, self.grade_entries)):
            subject = subj_entry.get().strip()
            if not subject:
                subject = f"Предмет {i+1}"
            subjects.append(subject)
            
            try:
                grade = float(grade_entry.get().replace(',', '.'))
                if grade < 1 or grade > 5:
                    messagebox.showerror("Ошибка", f"Оценка для '{subject}' должна быть от 1 до 5")
                    return
                grades.append(grade)
            except ValueError:
                messagebox.showerror("Ошибка", f"Введите число для предмета '{subject}'")
                return
        
        if not grades:
            messagebox.showwarning("Предупреждение", "Нет данных для расчета")
            return
        
        avg = self.calculate_average(grades)
        letter = self.get_letter_grade(avg)
        
        if avg >= 4.5:
            color = "#2E7D32"
        elif avg >= 3.5:
            color = "#1976D2"
        elif avg >= 2.5:
            color = "#F57C00"
        else:
            color = "#C62828"
        
        self.result_label.config(
            text=f"Средний балл: {avg:.2f} | {letter}",
            fg=color,
            font=("Arial", 14, "bold")
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeFlowApp(root)
    root.mainloop()
