#!/usr/bin/env python

import tkinter

top = tkinter.Tk()

label = tkinter.Label(top, text='Hello World!')
label.pack()

quit = tkinter.Button(top, text='QUIT',
                      command=top.quit)
quit.pack()
tkinter.mainloop()