#!/usr/bin/env python

from tkinter import Tk, Frame, Label, Button, BOTH
import os
import tempfile
import win32com.client as win32

def edit():
    olook = win32.Dispatch('Outlook.Application')
    insp = olook.ActiveInspector()
    if insp is None:
        return
    item = insp.CurrentItem
    if item is None:
        return

    body = item.Body
    tmpfd, tmpfn = tempfile.mkstemp()
    f = os.fdopen(tmpfd, 'a')
    f.write(body.replace('\r\n', '\n'
    ))
    f.close()

    ed = r"c:\progra~2\vim\vim80\gvim.exe"
    print(ed)
    os.spawnv(os.P_WAIT, ed, [ed, tmpfn])

    f = open(tmpfn, 'r')
    body = f.read().replace('\n', '\r\n')
    f.close()
    os.unlink(tmpfn)
    item.Body = body

if __name__ == '__main__':
    tk = Tk()
    f = Frame(tk, borderwidth=2)
    f.pack(fill=BOTH)
    Label(f,
          text="Outlook Edit Launcher v0.3").pack()
    Button(f, text="Edit",
           fg='blue', command=edit).pack(fill=BOTH)
    Button(f, text="Quit",
           fg='red', command=tk.quit).pack(fill=BOTH)
    tk.mainloop()