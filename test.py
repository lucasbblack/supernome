# this is like a pre-processor macro in C
# we import a GUI (general user interface) library called
# tkinter and set the alias/variable to tk as a shorthand [saves time typing]
import tkinter as tk

# instantiate singleton of a window Object
window = tk.Tk()

# go over 3 values
for i in range(3):
    # for each i value, iterate 3 more times (0...0/1/2, 1...0/1/2)
    for j in range(3):
        # create a new window frame using the tk variable we declared above
        frame = tk.Frame(
            # set the frame to the declared window object
            master=window,
            # raise each button (bevel design)
            relief=tk.RAISED,
            # self-explanatory
            borderwidth=1
        )

        # with each new frame, set its grid position
        frame.grid(row=i, column=j)
        # add a label to each frame (9 in total, 3 * 3)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        # let tk handle the rest
        label.pack()

# eli5: while True until user quits
window.mainloop()
