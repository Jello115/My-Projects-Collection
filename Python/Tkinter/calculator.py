from tkinter import ttk
import tkinter as tk

root = tk.Tk()

root.geometry("400x300")
root.title("test")

label = ttk.Label(root, text="Calculator")
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3)
textbox.pack(padx=10, pady=10)


buttonFrame = tk.Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

def button_click(number):
    textbox.insert(tk.INSERT, number)
    

btn1 = ttk.Button(buttonFrame, text="1", command= lambda: button_click(1))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = ttk.Button(buttonFrame, text="2", command= lambda: button_click(2))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = ttk.Button(buttonFrame, text="3", command= lambda: button_click(3))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = ttk.Button(buttonFrame, text="4", command= lambda: button_click(3))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = ttk.Button(buttonFrame, text="5", command= lambda: button_click(4))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = ttk.Button(buttonFrame, text="6", command= lambda: button_click(5))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btn7 = ttk.Button(buttonFrame, text="7", command= lambda: button_click(6))
btn7.grid(row=2, column=0, sticky=tk.W+tk.E)

btn8 = ttk.Button(buttonFrame, text="8", command= lambda: button_click(7))
btn8.grid(row=2, column=1, sticky=tk.W+tk.E)

btn9 = ttk.Button(buttonFrame, text="9", command= lambda: button_click(9))
btn9.grid(row=2, column=2, sticky=tk.W+tk.E)

btn10 = ttk.Button(buttonFrame, text="+", command= lambda: button_click('+'))
btn10.grid(row=3, column=0, sticky=tk.W+tk.E)

btn11 = ttk.Button(buttonFrame, text="0", command= lambda: button_click(0))
btn11.grid(row=3, column=1, sticky=tk.W+tk.E)

btn12 = ttk.Button(buttonFrame, text="*", command= lambda: button_click('*'))
btn12.grid(row=3, column=2, sticky=tk.W+tk.E)

btn13 = ttk.Button(buttonFrame, text="/", command= lambda: button_click('/'))
btn13.grid(row=4, column=0, sticky=tk.W+tk.E)

btn14 = ttk.Button(buttonFrame, text="-", command= lambda: button_click('-'))
btn14.grid(row=4, column=1, sticky=tk.W+tk.E)

btn15 = ttk.Button(buttonFrame, text="=")
btn15.grid(row=4, column=2, sticky=tk.W+tk.E)

buttonFrame.pack(fill='x')



root.mainloop()

