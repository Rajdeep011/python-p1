import tkinter as tk
from PIL import Image, ImageTk
import random



window = tk.Tk()
window.title("Dice")
window.geometry("500x500")


dice = ["D:/dice-six-faces-one.png","D:/dice-six-faces-two.png","D:/dice-six-faces-three.png","D:/dice-six-faces-four.png","D:/dice-six-faces-five.png","D:/dice-six-faces-six.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image= image1)
label2 = tk.Label(window,image= image2)

label1.place(x=0, y=100)
label2.place(x= 500, y=100)

def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image=image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image = image2



button = tk.Button(window,text = "Roll",fg = "white",bg = "dark green",font = "Times 20 bold",command = dice_roll)
button.place(x= 460, y=0)


window.mainloop()