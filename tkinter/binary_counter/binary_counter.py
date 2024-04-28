from tkinter import *
from tkinter import ttk
import time
from threading import Thread
def binary_counter():
    
    root = Tk()
    root.title('Binary counter')
    f = ttk.Frame(root)
    f.grid()

    def count_bits():
        bits = [
            '0000', # -- 0
            '0001', # -- 1
            '0010', # -- 2
            '0011', # -- 3
            '0100', # -- 4
            '0101', # -- 5
            '0110', # -- 6
            '0111', # -- 7
            '1000', # -- 8
            '1001', # -- 9
            '1010', # -- 10
            '1011', # -- 11
            '1100', # -- 12
            '1101', # -- 13
            '1110', # -- 14
            '1111', # -- 15
        ]
        x = 0
        while x < 100:
            for bit in bits:
                for i, square in enumerate('abcd'):
                    squares.itemconfig(my_bits[square], fill='dark cyan' if bit[i] == '1' else 'white')
                time.sleep(0.5)
                root.update()
            x+=1



    squares = Canvas(f, width=500,  height=200)
    my_bits = {}
    my_bits['a'] = squares.create_rectangle(20,  20, 100, 100, fill='white', outline='dark blue')
    my_bits['b'] = squares.create_rectangle(120,  20, 200, 100, fill='white', outline='dark blue')
    my_bits['c'] = squares.create_rectangle(220,  20, 300, 100, fill='white', outline='dark blue')
    my_bits['d'] = squares.create_rectangle(320,  20, 400, 100, fill='white', outline='dark blue')
    squares.grid()
    
    count = ttk.Button(f, text='Start counting', command=Thread(target=count_bits).start)
    count.grid()
    root.mainloop()

binary_counter()
