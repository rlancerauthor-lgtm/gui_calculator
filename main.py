
import customtkinter
from PIL import ImageTk,Image
import os
import pywinstyles


customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()

root.resizable(False, False)

root.title("Calculator")

#Function to add character to entry widget
def add_character(char):
   if char.isdigit() or char == ".":
       inp.insert("end", "" + str(char))
   else:
       inp.insert("end", " " + str(char) + " ")

#Function to clear everything in entry widget
def clearAll():
    inp.delete(0, "end")

#Function to delete last character in entry widget
def deleteLast():
        expression = inp.get()
        inp.delete(len(expression) - 1, customtkinter.END)
     
# Function to evaluate the sum/expression
def evaluate_expression():
    expression = inp.get()
    try:
        # Evaluate the mathematical string
        result = eval(expression)
        # Display the result in the entry (clearing previous text)
        inp.insert("end", " = " + str(result))
    except Exception:
        inp.delete(0, "end")
        inp.insert(0, "Error")


root.geometry("420x280")
 # load and create background image
current_path = os.path.dirname(os.path.realpath(__file__))
canvas_bg =customtkinter.CTkCanvas(root, width=420, height=400, highlightthickness=0) 

canvas_img = ImageTk.PhotoImage(Image.open(current_path + "\\back_img.jpeg"))

       
canvas_bg.create_image(0,0, image=canvas_img)
canvas_bg.pack()

def add_text_hover(widget):
    """Dynamically applies text hover colors to a CustomTkinter widget."""
    widget.bind("<Enter>", lambda e: widget.configure(text_color="#ffffff",fg_color="#707175"))
    widget.bind("<Leave>", lambda e: widget.configure(text_color="#3F3E3E",fg_color="#a8acbe"))

inp = customtkinter.CTkEntry(canvas_bg, corner_radius=5,width=400, bg_color="#5d6a7d",font=("Arial",24,"bold"))
inp.grid(row=0,column=0, columnspan=6,pady=10,padx=10,ipady=5)


#buttons
clrBtn = customtkinter.CTkButton(canvas_bg, text="C", width=60,height=40,fg_color="red", bg_color="#000001", hover_color="#b30505",text_color="white",corner_radius=5,font=("Arial",15,"bold"),command=clearAll)
clrBtn.grid(row=1, column=0,pady=5,padx=5)
pywinstyles.set_opacity(clrBtn, color="#000001") 

delBtn = customtkinter.CTkButton(canvas_bg,text="DEL",width=60,height=40,fg_color="#85642b",text_color="white",hover_color="#815507",corner_radius=5,font=("Arial",15,"bold"), bg_color="#000001",command=deleteLast)
delBtn.grid(row=1, column=1,pady=5,padx=5)
pywinstyles.set_opacity(delBtn, color="#000001") 

minusBtn = customtkinter.CTkButton(canvas_bg,text="-",width=60,height=40,fg_color="#ed962c",text_color="white",hover_color="#e9850b",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",command=lambda:add_character("-"))
minusBtn.grid(row=1, column=2,pady=5,padx=5)
pywinstyles.set_opacity(minusBtn, color="#000001") 

plusBtn = customtkinter.CTkButton(canvas_bg,text="+",width=60,height=40,fg_color="#0593a1",text_color="white",hover_color="#025b63",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",command=lambda:add_character("+"))
plusBtn.grid(row=1, column=3,pady=5,padx=5)
pywinstyles.set_opacity(plusBtn, color="#000001") 

multiBtn = customtkinter.CTkButton(canvas_bg,text="x",width=60,height=40,fg_color="#7a40e0",text_color="white",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",hover_color="#37058d",command=lambda:add_character("*"))
multiBtn.grid(row=1, column=4,pady=5,padx=5)
pywinstyles.set_opacity(multiBtn, color="#000001")

divBtn = customtkinter.CTkButton(canvas_bg,text="÷",width=60,height=40,fg_color="#bc41bd",text_color="white",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",hover_color="#8d078d",command=lambda:add_character("/"))
divBtn.grid(row=1, column=5,pady=5,padx=5)
pywinstyles.set_opacity(divBtn, color="#000001") 
#second row
nineBtn = customtkinter.CTkButton(canvas_bg, text="9", width=60,height=40,fg_color="#a8acbe",text_color="#3F3E3E",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",hover_color="#707175",command=lambda:add_character("9"))
nineBtn.grid(row=2, column=0,pady=5,padx=5)
pywinstyles.set_opacity(nineBtn, color="#000001") 
add_text_hover(nineBtn)

eigBtn = customtkinter.CTkButton(canvas_bg, text="8", width=60,height=40,fg_color="#a8acbe",text_color="#3F3E3E",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",hover_color="#707175",command=lambda:add_character("8"))
eigBtn.grid(row=2, column=1,pady=5,padx=5)
pywinstyles.set_opacity(eigBtn, color="#000001") 
add_text_hover(eigBtn)

sevBtn = customtkinter.CTkButton(canvas_bg, text="7", width=60,height=40,fg_color="#a8acbe",text_color="#3F3E3E",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",hover_color="#707175",command=lambda:add_character("7"))
sevBtn.grid(row=2, column=2,pady=5,padx=5)
pywinstyles.set_opacity(sevBtn, color="#000001") 
add_text_hover(sevBtn)

sixBtn = customtkinter.CTkButton(canvas_bg, text="6", width=60,height=40,fg_color="#a8acbe",text_color="#3F3E3E",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",hover_color="#707175",command=lambda:add_character("6"))
sixBtn.grid(row=2, column=3,pady=5,padx=5)
pywinstyles.set_opacity(sixBtn, color="#000001") 
add_text_hover(sixBtn)

fifBtn = customtkinter.CTkButton(canvas_bg, text="5", width=60,height=40,fg_color="#a8acbe",text_color="#3F3E3E",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",hover_color="#707175",command=lambda:add_character("5"))
fifBtn.grid(row=3, column=0,pady=5,padx=5)
pywinstyles.set_opacity(fifBtn, color="#000001") 
add_text_hover(fifBtn)

frBtn = customtkinter.CTkButton(canvas_bg, text="4", width=60,height=40,fg_color="#a8acbe",text_color="#3F3E3E",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",hover_color="#707175",command=lambda:add_character("4"))
frBtn.grid(row=3, column=1,pady=5,padx=5)
pywinstyles.set_opacity(frBtn, color="#000001") 
add_text_hover(frBtn)

thrBtn = customtkinter.CTkButton(canvas_bg, text="3", width=60,height=40,fg_color="#a8acbe",text_color="#3F3E3E",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",hover_color="#707175",command=lambda:add_character("3"))
thrBtn.grid(row=3, column=2,pady=5,padx=5)
pywinstyles.set_opacity(thrBtn, color="#000001")

twoBtn = customtkinter.CTkButton(canvas_bg, text="2", width=60,height=40,fg_color="#a8acbe",text_color="#3F3E3E",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",hover_color="#707175",command=lambda:add_character("2"))
twoBtn.grid(row=3, column=3,pady=5,padx=5)
pywinstyles.set_opacity(twoBtn, color="#000001")
add_text_hover(twoBtn)

oneBtn = customtkinter.CTkButton(canvas_bg, text="1", width=60,height=40,fg_color="#a8acbe",text_color="#3F3E3E",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",hover_color="#707175",command=lambda:add_character("1"))
oneBtn.grid(row=4, column=0,pady=5,padx=5)
pywinstyles.set_opacity(oneBtn, color="#000001") 
add_text_hover(oneBtn)

zeroBtn = customtkinter.CTkButton(canvas_bg, text="0", width=60,height=40,fg_color="#a8acbe",text_color="#3F3E3E",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",hover_color="#707175",command=lambda:add_character("0"))
zeroBtn.grid(row=4, column=1,pady=5,padx=5)
pywinstyles.set_opacity(zeroBtn, color="#000001") 

decBtn = customtkinter.CTkButton(canvas_bg, text=".", width=120,height=40,fg_color="#a8acbe",text_color="#3F3E3E",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",hover_color="#707175",command=lambda:add_character("."))
decBtn.grid(row=4, column=2,pady=5,padx=5,columnspan=2)
pywinstyles.set_opacity(decBtn, color="#000001") 
add_text_hover(decBtn)


eqBtn = customtkinter.CTkButton(canvas_bg, text="=", width=130,height=140,fg_color="#09916d",text_color="#ffffff",corner_radius=5,font=("Arial",22,"bold"), bg_color="#000001",hover_color="#045b44",command=evaluate_expression)
eqBtn.grid(row=2, column=4,pady=5,padx=5,rowspan=3,columnspan=2)
pywinstyles.set_opacity(eqBtn, color="#000001") 

label = customtkinter.CTkLabel(canvas_bg, text="", fg_color="transparent")
label.grid(row=5, column=0,pady=5,padx=5,columnspan=6)
root.mainloop()