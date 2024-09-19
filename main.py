from tkinter import *
from pathlib import Path

DARK = "#222831"
MID = "#393E46"
BLUE = "#00ADB5"
WHITE = "#EEEEEE"


def delete_entry(num):
    item = new_todo.items[num]
    new_todo.items.remove(item)
    delete_button = new_todo.buttons[num]
    label_title = new_todo.labels[num]
    label_title.grid_forget()
    delete_button.grid_forget()
    new_todo.update_list()


class ToDo:
    def __init__(self):
        try:
            with open(file="to_do.txt", mode="r") as file:
                content = file.readlines()
                if "\n" in content:
                    content.remove("\n")
        except FileNotFoundError:
            if not Path("to_do.txt").exists():
                open(file="to_do.txt", mode="w")
                content = None
        self.items = content
        self.labels = []
        self.buttons = []
        if content:
            self.num_items = len(content)

    def update_list(self):
        if self.items:
            for each in self.items:
                with open(file="to_do.txt", mode="w") as file:
                    file.write(f"{each}\n")
        else:
            with open(file="to_do.txt", mode="w") as file:
                file.write("")
        new_todo.display()

    def save(self):
        if todo.get != "":
            with open(file="to_do.txt", mode="a") as file:
                file.write(f"{todo.get()}\n")
        self.items.append(todo.get())
        todo.delete(first=0, last=len(todo.get()))
        self.display()

    def display(self):
        save_button.grid_forget()
        todo.grid_forget()
        if self.labels:
            for each in self.labels:
                each.grid_forget()
        if self.buttons:
            for each in self.buttons:
                each.grid_forget()
        order = 1
        for each in self.items:
            num = self.items.index(each)
            item_number = num+1
            label_title = Label(
                text=f"{item_number} : {each}", justify="center", height=1,
                fg=BLUE, bg=MID, font=("georgia", 12, "normal"), padx=10, anchor="n",)
            label_title.grid(column=0, row=order, pady=3, sticky="w")
            label_title.grid_columnconfigure(0, weight=3)
            label_title.grid_rowconfigure(0, weight=1)
            title = Button(
                text="Delete", fg=BLUE, bg=MID, font=("georgia", 10, "normal"),
                command=lambda num=num : delete_entry(num)
            )
            title.grid(column=2, row=order, pady=3,)

            self.labels.append(label_title)
            self.buttons.append(title)
            order += 1
        row = len(new_todo.items) + 2
        save_button.grid(column=2, row=row, padx=20, pady=30)
        todo.grid(column=0, row=row, columnspan=2)


new_todo = ToDo()
# Window--------------------
window = Tk()
window.minsize(400, 400)
window.config(pady=20, padx=20, background=DARK)
# Entry and Labels-------------------
todo = Entry(width=80, bg=MID, fg=BLUE, font=("georgia", 10, "bold"),)
header = Label(text="To-Do List", fg=WHITE, bg=DARK, font=("georgia", 20, "bold"), pady=20)
header.grid(column=0, row=0, columnspan=3)
# Buttons ------------------
save_button = Button(text="Save", fg=BLUE, bg=MID, font=("georgia", 10, "normal"), command=new_todo.save)

new_todo.display()
window.mainloop()
