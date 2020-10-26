'''
Project: Expense Tracker
Desc: This is the GUI interface for the expense tracker, TEST
Date: 10/25/2020
Members: Matt, Dillion, Himani, Kavan
Packages used:
- tkinter (already included in python3)
- pySimpleGUI (creates an virtual environment)
'''

import tkinter as tk  ##this is our GUI package
HEIGHT = 400
WIDTH = 500
root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = '#80c1ff')
frame.place(relwidth = 1, relheight = 1)

Start = tk.Button(frame,text="Start", bg='gray') #places button within "root"
Start.place(relx = .05, rely = .25, relwidth = .25, relheight = .25)

info = tk.Button(frame,text="Info", bg='grey') #places button within "root"
info.place(relx = .37, rely = .35, relwidth = .25, relheight = .25)

quit = tk.Button(frame,text="Quit", bg='grey') #places button within "root"
quit.place(relx = .67, rely = .30, relwidth = .25, relheight = .25)


title = tk.Label(frame, text = "Expense Tracker Program", bg = 'white', font = "Helvetica")
title.place(relx = .27, rely = 0.02, relwidth = .5, relheight = .10)



#entry = tk.Entry(frame, bg='green')
#entry.grid(row = 2, column = 2)

root.mainloop()
















'''startLayout = [[sg.Text("Expense Tracker Program")],
                [sg.Button("Start")],  ## start - starts application
                [sg.Button("Info")],  ##info describes the application
                [sg.Button("Quit")]]  ## quit -- quits application'''

