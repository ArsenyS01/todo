
    # ЧАСТЬ 1 PLACEHOLDER
    # self.task_input.insert(0, "Enter your todo here...")

    # self.task_input.bind("<FocusIn>", self.clear_placeholder)
    # self.task_input.bind("<FocusOut>", self.restore_placeholder)




    # ЧАСТЬ 2 PLACEHOLDER
    # def clear_placeholder(self, event):
    #     if self.task_input.get() == "Enter your todo here...":
    #         self.task_input.delete(0, tk.END)
    #         self.task_input.configure(style="TEntry")

    # def restore_placeholder(self, event):
    #     if self.task_input.get() == "":
    #         self.task_input.insert(0, "Enter your todo here...")
    #         self.task_input.configure(style="Custom.TEntry")




    # def load_tasks(self):
    #         try:
    #             with open("tasks.json", "r") as f:
    #                 data = json.load(f)
    #                 for task in data:
    #                     self.task_list.insert(tk.END, task["text"])
    #                     self.task_list.itemconfig(tk.END, fg=task["color"])
    #         except FileNotFoundError:
    #             pass