from pickle import NONE
import tkinter

PINK = "#e2979c"
RED = "#e7385b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

loops = 0
completed = 0

timer = NONE


window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=200, pady=200, bg = YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="100 days of code/Pomodoro/download.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 120, text = "00:00", fill="white", font = (FONT_NAME, 20, "bold"))
canvas.pack()

my_label = tkinter.Label(text = "Timer", fg = GREEN,  font = (FONT_NAME, 30, "bold"))
my_label.place(x = 38, y = 0)



def start_timer():
    if completed % 2 == 0 and loops % 4 != 0 or completed % 2 == 0 and loops == 0:
        count = (WORK_MIN * 60)
    if completed % 2 == 1 and loops % 4 != 0 or completed % 2 == 1 and loops == 0:
        count = (SHORT_BREAK_MIN * 60)
    if loops % 4 == 0 and loops != 0:
        count = (LONG_BREAK_MIN * 60)
    count_down(count)

def count_down(count):
    global timer
    global loops
    global completed
    minutes = int(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    elif count == 0 and loops % 4 != 0 or loops == 0:
        loops += 1
        completed += 1
        check_marks.config(text = "✔️" * completed)
        start_timer()
    else:
        loops = 0
        check_marks.config(text = "")
        start_timer()

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")

start_button = tkinter.Button(text = "Start", command = start_timer)
start_button.place(x = -15, y = 180)

reset_button = tkinter.Button(text = "Reset", command = reset_timer)
reset_button.place(x = 170, y = 180)

check_marks = tkinter.Label(text = "", fg=GREEN, bg=YELLOW)
check_marks.place(x = 70, y = 220)



window.mainloop()