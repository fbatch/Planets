from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

planets = [('Mercury', 2.646, 'img/Mercury.jpg'),
            ('Venus', 1.104, 'img/Venus.jpg'),
            ('Mars', 2.661, 'img/Mars.jpg'),
            ('Jupiter', 0.423, 'img/Jupiter.jpg'),
            ('Saturn', 1.087, 'img/Saturn.jpg'),
            ('Uran', 1.125, 'img/Uran.jpg'),
            ('Neptune', 0.889, 'img/Neptune.jpg')]

planets_names = []
for p in planets:
    planets_names.append(p[0])


def calculate_weight(_):
    global photo
    weight = earth_weight_ent.get()
    planet_name = planets_list_box.get()
    for planet in planets:
        if planet_name == planet[0]:
            planet_img = Image.open(planet[2])
            photo = ImageTk.PhotoImage(planet_img)
            planet_canvas.itemconfig(planet_canvas_img, image=photo)
            if weight == '':
                result_lb['text'] = 'Enter your Weight'
            else:
                result_lb['text'] = 'Your weight on ' + planet[0] + ' equals ' + str(round(float(weight) / planet[1], 1)) + ' kg.'


window = Tk()
window.title('Weight Calculator for different planets')
window.geometry('350x400+800+320')

earth_weight_lb = Label(window, text='Enter your Earth weight:', font='Arial 14')
earth_weight_lb.pack()

earth_weight_ent = Entry(window, font='arial 12')
earth_weight_ent.pack()

choose_planet_lb = Label(window, text='Choose planet:', font='Arial 14')
choose_planet_lb.pack()

planets_list_box = ttk.Combobox(window, state='readonly', values=planets_names, font='Arial 12')
planets_list_box.current(0)
planets_list_box.bind('<<ComboboxSelected>>', calculate_weight)
planets_list_box.pack()

planet_canvas = Canvas(window, height=200, width=200)
planet_canvas_img = planet_canvas.create_image(0, 0, anchor='nw')
planet_canvas.pack()

result_lb = Label(window, font='Arial 12')
result_lb.pack()
window.mainloop()
