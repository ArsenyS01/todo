import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json

class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()


        self.title("Todo List App")
        self.geometry("1200x800")
        style = Style(theme="flatly")
        style.configure("Custom.TEntry", foreground="gray")


        self.task_input = ttk.Entry(self, font=("TkDefaultFont", 16), width=30, style="Custom.TEntry")
        self.task_input.pack(pady=10)

        self.task_list = tk.Listbox(self, font=("TkDefaultFont", 16), height=10, selectmode=tk.NONE)
        self.task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.load_tasks()




        ttk.Button(self, text="Add", command=self.add_task, style="info.TButton", width=30).pack(pady=10, ipadx=20, ipady=10)
        ttk.Style().configure("info.TButton", font=("TkDefaultFont", 14))

        ttk.Button(self, text="Done", style="success.TButton", command=self.mark_done, width=15, padding=(80, 34)).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Style().configure("success.TButton", font=("TkDefaultFont", 14))

        ttk.Button(self, text="Delete", style="danger.TButton", command=self.delete_task, width=15, padding=(80, 34)).pack(side=tk.RIGHT, padx=10, pady=10, ipadx=20, ipady=10)
        ttk.Style().configure("danger.TButton", font=("TkDefaultFont", 14))


    def add_task(self):
        task = self.task_input.get()
        if task != "":
            self.task_list.insert(tk.END, task)
            self.task_list.itemconfig(tk.END, fg="orange")
            self.task_input.delete(0, tk.END)
            self.save_tasks()

    
    def mark_done(self):
        task_index = self.task_list.curselection()
        if task_index:
            current_color = self.task_list.itemcget(task_index, "fg")
            new_color = "orange" if current_color == "green" else "green"
            self.task_list.itemconfig(task_index, fg=new_color)
            self.task_list.selection_clear(0, tk.END)
            self.save_tasks()

    
    def delete_task(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.delete(task_index)
            self.save_tasks()
    

    def load_tasks(self):
        with open("tasks.json", "r") as f:
            data = json.load(f)
            for task in data:
                self.task_list.insert(tk.END, task["text"])
                self.task_list.itemconfig(tk.END, fg=task["color"])
    
    def save_tasks(self):
        data = []
        for i in range(self.task_list.size()):
            text = self.task_list.get(i)
            color = self.task_list.itemcget(i, "fg")
            data.append({"text": text, "color": color})
        with open("tasks.json", "w") as f:
            json.dump(data, f)

if __name__ == '__main__':
    app = TodoListApp()
    app.mainloop()
