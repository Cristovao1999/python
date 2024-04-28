from tkinter import *
from tkinter import ttk
from threading import Thread
import time

def display_lights():

    root = Tk()
    root.title('Semaforo')

    f = ttk.Frame(root)
    f.grid()

    def start_lights():
        blueprint.itemconfig(lights['red'], fill='red')
        blueprint.itemconfig(lights['yellow'], fill='white')
        blueprint.itemconfig(lights['green'], fill='white')
        time.sleep(5)
        blueprint.itemconfig(lights['red'], fill='white')
        blueprint.itemconfig(lights['yellow'], fill='yellow')
        time.sleep(1)
        blueprint.itemconfig(lights['yellow'], fill='white')
        blueprint.itemconfig(lights['green'], fill='light green')
        time.sleep(5)
        blueprint.itemconfig(lights['green'], fill='white')
        blueprint.itemconfig(lights['yellow'], fill='yellow')
        time.sleep(1)
        start_lights()
        
    blueprint = Canvas(f, width=300, height=250)
    #semaforo = blueprint.create_rectangle()
    lights = {}
    lights['red'] = blueprint.create_oval(100, 30, 160, 90, fill='red', outline='black')
    lights['yellow'] = blueprint.create_oval(100, 100, 160, 160, fill='yellow', outline='black')
    lights['green'] = blueprint.create_oval(100, 170, 160, 230, fill='light green', outline='black')
    blueprint.grid()

    start = ttk.Button(f, text='start traffic', command=Thread(target=start_lights).start)
    start.grid(sticky='sw')

    root.mainloop()

display_lights()
