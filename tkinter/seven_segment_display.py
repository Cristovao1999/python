from tkinter import *
from tkinter import ttk
from threading import Thread
from time import sleep

def seven_segment():
    root = Tk()
    root.title('7-Segment Display')

    display = ttk.Frame(root)
    display.grid()

    segs = Canvas(display, width=220, height=440)
    segs.grid()

    # Define segments as rectangles
    segments = {}
    segments['a'] = segs.create_rectangle(50, 20, 160, 40, fill='white')
    segments['b'] = segs.create_rectangle(160, 50, 180, 150, fill='white')
    segments['c'] = segs.create_rectangle(160, 170, 180, 270, fill='white')
    segments['d'] = segs.create_rectangle(50, 280, 150, 300, fill='white')
    segments['e'] = segs.create_rectangle(30, 170, 50, 270, fill='white')
    segments['f'] = segs.create_rectangle(30, 50, 50, 150, fill='white')
    segments['g'] = segs.create_rectangle(50, 150, 160, 170, fill='white')
    dp = segs.create_oval(170, 310, 190, 330, fill='black')  # Decimal point

    def display_numbers():
        bit_patterns = [
            '1111110', # 0
            '0110000', # 1
            '1101101', # 2 
            '1111001', # 3
            '0110011', # 4
            '1011011', # 5
            '1011111', # 6 
            '1110000', # 7
            '1111111', # 8
            '1111011', # 9
        ]
        count = 0
        while count < 100:
            for bits in bit_patterns:
                for i, bit in enumerate('abcdefg'):
                    segs.itemconfig(segments[bit], fill='red' if bits[i] == '1' else 'white')
                sleep(1)  # wait for 1 second
                root.update()  # update the GUI

            count +=1
    start = ttk.Button(display, text='Start', command=lambda: Thread(target=display_numbers).start())
    start.grid()

    root.mainloop()

seven_segment()
