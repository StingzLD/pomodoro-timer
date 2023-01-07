from tkinter import *

# --------------------------- CONSTANTS -------------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# --------------------------- TIMER RESET ------------------------------------ #

# --------------------------- TIMER MECHANISM -------------------------------- #

# --------------------------- COUNTDOWN MECHANISM ---------------------------- #

# --------------------------- UI SETUP --------------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title
title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
# title.config(pady=40)
title.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(107, 134, text="00:00", font=(FONT_NAME, 30, "bold"),
                   fill="white")
canvas.grid(column=1, row=1)

# Start Button
start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

# Stop Button
stop_button = Button(text="Stop", highlightthickness=0)
stop_button.grid(column=2, row=2)

# Check Mark
check_marks = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 14))
check_marks.grid(column=1, row=3)

window.mainloop()
