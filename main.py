
import tkinter as tk

from tkinter import PhotoImage

window = tk.Tk()

window.geometry('275x470')

window.title('Miles to Km')

window.resizable(False,False)

window.configure(bg='#112b45',padx=10,pady=10)


window.attributes('-alpha',0.9)



field_text = ""

field=tk.Text(window,height=2,width=12,font=('Poppins',25))

field.bind("<Key>", lambda disable: "break")


field.grid(row=0,column=0,columnspan=4,)

def field_input(value):
    global field_text
   
    field_text+=str(value)
   


    field.delete("1.0","end")
   
    field.insert("1.0", field_text)
  

 
def miles_to_km():
    
    global field_text
    result = (round(float(field_text) * 1.60934,5))
    field.delete("1.0","end")
    field.insert("1.0", result)



def clear():
    global field_text  

    field_text =""
    field.delete("1.0","end")
    


btn7 =tk.Button(window,text="7",command=lambda: field_input(7),width=5,font=('Poppins',15))


btn7.grid(row=1,column=1,pady=10,padx=4)


btn8 =tk.Button(window,text="8",command=lambda: field_input(8),width=5,font=('Poppins',15))
btn8.grid(row=1,column=2,pady=10,padx=4)


btn9 =tk.Button(window,text="9",command=lambda: field_input(9),width=5,font=('Poppins',15))
btn9.grid(row=1,column=3,pady=10,padx=4)


btn4 =tk.Button(window,text="4",command=lambda: field_input(4),width=5,font=('Poppins',15))
btn4.grid(row=2,column=1,pady=10,padx=4)

btn5 =tk.Button(window,text="5",command=lambda: field_input(5),width=5,font=('Poppins',15))
btn5.grid(row=2,column=2,pady=10,padx=4)

btn6 =tk.Button(window,text="6",command=lambda: field_input(6),width=5,font=('Poppins',15))
btn6.grid(row=2,column=3,pady=10,padx=4)


btn1 =tk.Button(window,text="1",command=lambda: field_input(1),width=5,font=('Poppins',15))
btn1.grid(row=3,column=1,pady=10,padx=4)


btn2 =tk.Button(window,text="2",command=lambda: field_input(2),width=5,font=('Poppins',15))
btn2.grid(row=3,column=2,pady=10,padx=4)


btn3 =tk.Button(window,text="3",command=lambda: field_input(3),width=5,font=('Poppins',15))
btn3.grid(row=3,column=3,pady=10,padx=4)

btn0 =tk.Button(window,text="0",command=lambda: field_input(0),width=5,font=('Poppins',15))
btn0.grid(row=4,column=1,pady=10,padx=4)

clear_btn =tk.Button(window,text="C",command=lambda: clear(),bg='#5e6a75',width=5,font=('Poppins',15))
clear_btn.grid(row=4,column=2,pady=10,padx=4)

equals_btn =tk.Button(window,text="=",command=lambda: miles_to_km(),width=5, font=('Poppins',15))
equals_btn.grid(row=4,column=3,pady=10,padx=4)


window.mainloop()
