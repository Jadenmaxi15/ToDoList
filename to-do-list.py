from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox

def entertask():
    input_text=""
    def add():
        nonlocal input_text
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Warning!",message="Please Enter some Text")
        else:
            listbox_task.insert(END,input_text)
            root1.destroy()
    root1=Tk()
    root1.title("Add task")
    entry_task=Text(root1,width=40,height=4, font=("Helvetica", 12))
    entry_task.pack(pady=10)
    button_temp=Button(root1,text="Add task", font=("Helvetica", 12), bg="green", fg="white", command=add)
    button_temp.pack(pady=10)
    root1.mainloop()

def deletetask():
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])

def markcompleted():
    marked=listbox_task.curselection()
    temp=marked[0]
    temp_marked=listbox_task.get(marked)
    temp_marked=temp_marked+" ✔"
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)

window = Tk()
window.title("To-Do App")

# Load and display the background image
background_image = ImageTk.PhotoImage(Image.open("background.jpg"))
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame_task = Frame(window, bg="white")
frame_task.place(x=50, y=50)

listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font=("Helvetica", 12))  
listbox_task.grid(row=0, column=0)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.grid(row=0, column=1, sticky="NS")
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_button = Button(window, text="Add task", font=("Helvetica", 12), bg="green", fg="white", width=50, command=entertask)
entry_button.place(x=50, y=400)

delete_button = Button(window, text="Delete selected task", font=("Helvetica", 12), bg="red", fg="white", width=50, command=deletetask)
delete_button.place(x=50, y=450)

mark_button = Button(window, text="Mark as completed", font=("Helvetica", 12), bg="blue", fg="white", width=50, command=markcompleted)
mark_button.place(x=50, y=500)

window.mainloop()
