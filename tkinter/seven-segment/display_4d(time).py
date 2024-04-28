from tkinter import *
from tkinter import ttk
import time



class Digit:
    
    def __init__(self, segs, x):
            self.segs = segs
            self.segments = {}
            self.segments['a'] = segs.create_rectangle(50+x, 20, 160+x, 40, fill='white')
            self.segments['b'] = segs.create_rectangle(160+x, 50, 180+x, 150, fill='white')
            self.segments['c'] = segs.create_rectangle(160+x, 170, 180+x, 270, fill='white')
            self.segments['d'] = segs.create_rectangle(50+x, 280, 150+x, 300, fill='white')
            self.segments['e'] = segs.create_rectangle(30+x, 170, 50+x, 270, fill='white')
            self.segments['f'] = segs.create_rectangle(30+x, 50, 50+x, 150, fill='white')
            self.segments['g'] = segs.create_rectangle(50+x, 150, 160+x, 170, fill='white')
            dp = segs.create_oval(170+x, 310, 190+x, 330, fill='black')  # Decimal point
    
    def __display__(self, digit, root):
        hex_segs = {
            '0x0': '1111110', # 0
            '0x1': '0110000', # 1
            '0x2': '1101101', # 2
            '0x3': '1111001', # 3
            '0x4': '0110011', # 4
            '0x5': '1011011', # 5
            '0x6': '1011111', # 6
            '0x7': '1110000', # 7
            '0x8': '1111111', # 8
            '0x9': '1111011', # 9
        }
       
        for hex_num, hex_value in hex_segs.items():
            if hex_num == digit:
                for i, bit in enumerate('abcdefg'):
                    self.segs.itemconfig(self.segments[bit], fill='red' if hex_value[i] == '1' else 'white')
                root.update()  # update the GUI


def seven_segment():
    root = Tk()
    root.title('7-Segment Display with 4d')

    f = ttk.Frame(root)
    f.grid()

    def display_digits():

          while True:
                h, m, s = time.strftime('%H:%M:%S').split(':')
                digit1.__display__(hex(int(h[0])), root)
                digit2.__display__(hex(int(h[1])), root)
                digit3.__display__(hex(int(m[0])), root)
                digit4.__display__(hex(int(m[1])), root)
                digit5.__display__(hex(int(s[0])), root)
                digit6.__display__(hex(int(s[1])), root)

    
    segs = Canvas(f, width=1400, height=440)
    digit1 = Digit(segs, 1)
    digit2 = Digit(segs, 200)
    dot1 = segs.create_oval(400, 80, 430, 110, fill='white')
    dot2 = segs.create_oval(400, 190, 430, 220, fill='white')
    digit3 = Digit(segs, 420)
    digit4 = Digit(segs, 620)
    dot3 = segs.create_oval(820, 80, 850, 110, fill='white')
    dot4 = segs.create_oval(820, 190, 850, 220, fill='white')
    digit5 = Digit(segs, 840)
    digit6 = Digit(segs, 1040)
    segs.grid()

    display = ttk.Button(f, text='display', command=display_digits)
    display.grid()

    root.mainloop()

seven_segment()
