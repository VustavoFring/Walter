from tkinter import*
import random

window = Tk()
w = 600
h = 600
window.geometry(str(h)+'x'+str(w))
canvas = Canvas(window,width= w,height=h)
canvas.place(in_=window, x=0 , y=0)
bg_photo = PhotoImage(file='bg_2.png')

class Knight:
    def __init__(self):
        self.photo = PhotoImage(file='knight.png')
        self.x = 70
        self.y = h//2
        self.v = 0
    def up(self,event):
        self.v = -3
    def down(self,event):
        self.v = 3
    def stop(self,event):
        self.v = 0

class Dragon:
    def __init__(self):
        self.photo = PhotoImage(file='dragon.png')
        self.x = 550
        self.y = random.randint(100,500)
        self.v = 1
knight = Knight()
dragons = []
for i in range(3):
    dragons.append(Dragon())


def game():
    canvas.delete('all')
    canvas.create_image(300,300,image=bg_photo)
    canvas.create_image(knight.x,knight.y,image=knight.photo)
    knight.v += knight.v
    dragon_to_kill = -1
    current_dragon = 0
    for dragon in dragons:
        dragon.x -= dragon.v
        canvas.create_image(dragon.x,dragon.y,image=dragon.photo)
        if (dragon.x - knight.x)**2 + (dragon.y - knight.y)**2 <= 96**2:
            dragon_to_kill = current_dragon
        current_dragon += 1
        if dragon.x <=0:
            canvas.delete('all')
            canvas.create_text(w//2,h//2, text= ' you lose',font= 'Verdana42',fill= 'red')
            break
    if dragon_to_kill>=0:
        del dragons[dragon_to_kill]
    if len(dragons) == 0:
        canvas.delete('all')
        canvas.create_text(w//2,h//2, text= ' you win',font= 'Verdana42',fill= 'red')
    else:
        window.after(10,game)
game()
window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)

window.mainloop()