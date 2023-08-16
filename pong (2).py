from tkinter import *
import random
import time

window = Tk()
window.geometry('400x500')
window.resizable(0,0)
canvas= Canvas(window,width=400,height=500)
canvas.pack()

class Racket():
    def __init__(self,canvas,color):
        self.win = canvas
        self.line = canvas.create_rectangle(230, 400, 330, 410, fill=color)
        self.x = 0
        self.win.bind_all('<KeyPress-Left>', self.left)
        self.win.bind_all('<KeyPress-Right>', self.right)

    def left(self,event):
        self.x = -2

    def right(self,event):
        self.x = 2

    def draw(self):
        self.win.move(self.line, self.x, 0)
        pos=self.win.coords(self.line)
        if pos[0] <= 0:
            self.x= 2    
        if pos[2] >= 400:
            self.x = -2

class Ball():
    def __init__ (self, canvas, racket, color):
        self.win = canvas
        self.racket = racket
        self.myball = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.ball_list = [-3, -2, -1, 1, 2, 3]
        self.x = random.choice(self.ball_list)
        self.y = -1
        self.tch_btm = False


    def touch(self,pos):
        racket_pos = self.win.coords(self.racket.line)
        if pos[2] >= racket_pos[0] and pos[0] <= racket_pos[2]:
            if pos[3] >= racket_pos[1] and pos[3] <= racket_pos[3]:
                return True
        return False
    
    def draw(self):
        self.win.move(self.myball,self.x,self.y)
        pos = self.win.coords(self.myball)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= 500:
            self.tch_btm = True
        if self.touch(pos) == True:
            self.y = -3 
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= 400:
            self.x = -3

racket = Racket(canvas,'blue')          
ball = Ball(canvas,racket,'orange')

while True:
    if ball.tch_btm == False:
        ball.draw()
        racket.draw()
    else:
        canvas.create_text(500 // 2, 400 // 2, text="You lose!", font="Verdana 42", fill='red')
        break
    window.update()
    time.sleep(0.02)

window.mainloop()
