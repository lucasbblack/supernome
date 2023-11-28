# Author: lb
# date: 11.28.23 | 11:55 am-pst |
# purpose: a super-utility tool for practicing shred guitar

# basic DB | todo: import sqlite3 [for storing practice logs]

import tkinter as tk

# super long function in the making cause I'm lazy


def supernome(bpm=None, tempo=None) -> [tk.Tk]:
    if bpm is None:
        bpm = 60.0
    if tempo is None:
        tempo = 1.0

    window = tk.Tk()

    # two upper frames, one lower frame. [1/2: main program, 3: practice logs]
    frames = [
        tk.Frame(master=window, width=200, height=100, bg='red'),
        tk.Frame(master=window, width=100, height=100, bg='yellow'),
        tk.Frame(master=window, width=300, height=100, bg='blue'),
    ]

    for frame in frames[:2]:
        frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)

    frames[2].pack(fill=None, side=tk.TOP, expand=False)

    messages = {
        'secondary': 'Ladies and gentlemen, start your metronomes'
    }

    labels = []

    for key in messages:
        # create tk label, using pre-defined messages
        l = tk.Label(text=messages[key])
        # append label to label array
        labels.append(l)
        # pack label into window
        l.pack()

    window_title = 'Mphm 23 | Supernome 3000 | LB special'
    window.title(window_title)
    window.mainloop()

    return window

if __name__ == "__main__":
    try:
        window = supernome()
    except WindowsError:
        print("WIN ERR |%s| couldn't run Tk/Python3" % WindowsError)

