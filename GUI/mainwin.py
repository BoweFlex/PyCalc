import tkinter as tk

window = tk.Tk()
window.title("JB Calculator")
entry = tk.Entry(window)
entry.pack()

firstRow = tk.Frame(window)
firstRow.pack()
secondRow = tk.Frame(window)
secondRow.pack()
thirdRow = tk.Frame(window)
thirdRow.pack()
fourthRow = tk.Frame(window)
fourthRow.pack()

tk.Button(firstRow, text="7", fg="black").pack(side=tk.LEFT)
tk.Button(firstRow, text="8", fg="black").pack(side=tk.LEFT)
tk.Button(firstRow, text="9", fg="black").pack(side=tk.LEFT)

tk.Button(secondRow, text="4", fg="black").pack(side=tk.LEFT)
tk.Button(secondRow, text="5", fg="black").pack(side=tk.LEFT)
tk.Button(secondRow, text="6", fg="black").pack(side=tk.LEFT)

tk.Button(thirdRow, text="1", fg="black").pack(side=tk.LEFT)
tk.Button(thirdRow, text="2", fg="black").pack(side=tk.LEFT)
tk.Button(thirdRow, text="3", fg="black").pack(side=tk.LEFT)

tk.Button(fourthRow, text="0", fg="black").pack(side=tk.LEFT)

window.mainloop()
