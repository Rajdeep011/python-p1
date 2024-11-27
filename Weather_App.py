from tkinter import *
from tkinter import ttk
import requests
import_requests

def data_get():
     city = city_name.get()
     data = requests.get('https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=94b588a08e10fa5bb07314c6fb5e604d').json()
     w_label1.config(text = data["weather"][0]["main"])
     wb_label1.config(text = data["weather"][0]["description"])
     wt_label1.config(text = str(data["main"]["temp"]-273.15))
     per_label1.config(text= data["main"]["pressure"])
win = Tk()

win.title("Weather App")
win.geometry("500x570")
win.config(bg='skyblue')

label = Label(win, text="Weather app", font=("Time New Roman",38,"bold"))
label.place(x=13,y=50,height=50,width=500)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win, text="Weather app", value= list_name, font=("Time New Roman",20,"bold"), textvariable = city_name)
com.place(x=25,y=120,height=50,width=450)

button = Button(win, text= "Done",font= ("Time New Roman",20,"bold"))
button.place(x=200,y=190,height=50, width=100)

w_label = Label(win, text="Weather Climate", font=("Time New Roman",20))
w_label.place(x=25,y=260,height=50,width=210)
w_label1 = Label(win, text="", font=("Time New Roman",20))
w_label1.place(x=250,y=260,height=50,width=210)

wb_label = Label(win, text="Weather Discription", font=("Time New Roman",17))
wb_label.place(x=25,y=320,height=50,width=210)
wb_label1 = Label(win, text="", font=("Time New Roman",17))
wb_label1.place(x=250,y=320,height=50,width=210)

wt_label = Label(win, text="Temperature", font=("Time New Roman",20))
wt_label.place(x=25,y=380,height=50,width=210)
wt_label1 = Label(win, text="", font=("Time New Roman",20))
wt_label1.place(x=250,y=380,height=50,width=210)

per_label = Label(win, text="Pressure", font=("Time New Roman",20))
per_label.place(x=25,y=440,height=50,width=210)
per_label1 = Label(win, text="", font=("Time New Roman",20))
per_label1.place(x=250,y=440,height=50,width=210)


win.mainloop()