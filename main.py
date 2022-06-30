import random
import time
import difflib
from tkinter import *

msg_list = [
    "여러분의 시간은 한정되어 있습니다.",
    "인생을 살기 위해 당신의 시간을 낭비하지 마세요.",
    "뒤를 돌아보는 일은 그만합시다.",
    "우리에겐 내일이 중요합니다.",
    "단순함을 얻기란 복잡함을 얻기보다 어렵다.",
    "무언가를 단순하게 만들기 위해서는 생각을 깔끔히 정리해야 한다.",
    "생각을 정리하는 과정은 어렵지만 이를 해내면 당신은 무엇이든 할 수 있다.",
    "위대한 일을 해내는 유일한 방법은 당신이 하는 그 일을 사랑하는 겁니다.",
    "오늘 할 수 있는 일에 전력을 다하라, 그러면 내일에는 한 걸음 더 진보한다.",
    "행복이란 타인을 행복하게 해주려는 데서 생기는 부산물이다.",
    "지혜는 듣는 데서 오고 후회는 말하는 데서 온다.",
    "말을 많이 하는 것과 말을 잘하는 것은 다르다.",
    "타인에 대한 존경은 처세법의 제일 조건이다.",
    "거짓말을 한 순간부터 뛰어난 기억력이 필요하다.",
    "내 비장의 무기는 아직 손 안에 있다. 그것은 희망이다.",
    "행동에 부주의 하지 말며, 말에 혼동되지 말며, 생각에 방황하지 말라.",
    "요구받기 전에 충고하지 말라.",
    "성공하기를 바라는 자는 자존심 까지도 포기해야 할 것이다.",
    "많이 팔려면 먼저 많이 사보라.",

]


def start():
    global Problem
    global startTime
    Problem = random.choice(msg_list)
    startTime = time.time()

    q_label.config(text=Problem)


def enter(envet):

    user = user_entry.get()

    deltaTime = time.time() - startTime

    accuracy = difflib.SequenceMatcher(None, Problem, user).ratio()
    speed = len(Problem) * accuracy * 3 / deltaTime * 60
    print(f"속도: {speed:0.2f} 정확도: {accuracy * 100:0.2f}")

    label_2.config(text=f"속도: {speed:0.2f} 정확도: {accuracy * 100:0.2f}")
    user_entry.delete(0, END)
    start()

    window.bind('<Return>', enter)




window = Tk()
window.title("타자 연습")
window.config(padx=50, pady=50)

window.bind('<Return>', enter)


canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="Icon-60@2x.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0,columnspan=2)

# q = random.choice(msg_list)
q_label=Label(text="타자연습", font=("Arial",24,"bold"))
q_label.grid(column=1, row=1,columnspan=2)

user_entry = Entry(window, width=35)

user_entry.grid(column=1, row=2, columnspan=2)

label_2=Label(text="start 버튼을 누르면 시작됩니다.", width=21)
label_2.grid(column=1, row=3)
start_btn = Button(text="START",width=13,command=start)
start_btn.grid(column=2, row=3)


mainloop()