from tkinter import *

# --------------------------- CONSTANTS -------------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
marks = ""
timer = None


# --------------------------- TIMER RESET ------------------------------------ #
def reset_timer():
    global reps
    global marks

    # Reset reps back to 0
    reps = 0
    # Cancel the window.after in count_down
    window.after_cancel(timer)
    # Reset the title to "Timer"
    title.config(text="Timer", fg=GREEN)
    # Reset clock back to "00:00"
    canvas.itemconfig(timer_text, text="00:00")
    # Reset check marks to none
    marks = ""
    check_marks.config(text=marks)


# --------------------------- TIMER MECHANISM -------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it is the 8th rep
    if reps % 8 == 0:
        title.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
    # If it is the 2nd/4th/6th rep
    elif reps % 2 == 0:
        title.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
    # If it is the 1st/3rd/5th/7th rep
    else:
        title.config(text="Work", fg=GREEN)
        count_down(work_sec)


# --------------------------- COUNTDOWN MECHANISM ---------------------------- #
def count_down(count):
    global timer
    global marks

    # Display time left
    count_min = count // 60
    count_sec = count % 60
    time_left = f"{count_min:02}:{count_sec:02}"
    canvas.itemconfig(timer_text, text=time_left)

    # Continue until the count hits 0
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    # Once at 0, add a check mark and start the timer again
    else:
        if reps % 2 == 0:
            marks += "✔"
        check_marks.config(text=marks)
        start_timer()


# --------------------------- UI SETUP --------------------------------------- #
# Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title
title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
title.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(107, 134, text="00:00", fill="white",
                                font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)


# Reset Button
restart_button = Button(text="Restart", highlightthickness=0, command=reset_timer)
restart_button.grid(column=2, row=2)

# Check Marks
check_marks = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 14))
check_marks.grid(column=1, row=3)

window.mainloop()
