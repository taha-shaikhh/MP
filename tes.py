from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from turtle import width

root = Tk()
root.title('Summarizer')
root.geometry("1000x1000")
frame = Frame(root)
frame.pack()

def getTextField(inputtext):
    res = inputtext.get("1.0","end-1c")
    print(res)

def refreshTextWindow():
    '''
        Function to call Text input screen
    '''
    for widgets in frame.winfo_children():
        widgets.destroy()
    label = Label(frame,text="Summarizer", font=('Helvetica',20)).grid(row=0,column=1,pady=5)
    text_input = StringVar()
    name_label = Label(frame, text = 'Text')
    textfield = ScrolledText(frame,width=60,height=20)
    textfield.grid(row=1,column=1)
    name_label.grid(row=1,column=0)
    sub_button = Button(frame,text='Submit',command=lambda:getTextField(textfield),width=10)
    sub_button.grid(row=4,column=1,pady=8)
    menu_button = Button(frame,text='Menu',command=startScreen,width=10)
    menu_button.grid(row=6,column=1,pady=8)

def refreshAudioWindow():
    '''
        Function to call Audio input screen
    '''
    for widgets in frame.winfo_children():
        widgets.destroy()
    l = Label(frame,text="Your audio is being recorded")
    l.grid(row=1,column=1,pady=5)
    stop_button = Button(frame,text='Stop ',command=resultScreen,width=10)
    stop_button.grid(row=2,column=1,pady=10)
    menu_button = Button(frame,text='Menu',command=startScreen,width=10)
    menu_button.grid(row=2,column=2,pady=10)

def startScreen():
    for widgets in frame.winfo_children():
        widgets.destroy()
    label = Label(frame,text="Summarizer", font=('Helvetica',20)).grid(row=0,column=2)
    
    var = StringVar()
    R1 = Radiobutton(frame, text="Text", variable=var, value="t",command=refreshTextWindow)

    R2 = Radiobutton(frame, text="Audio", variable=var, value="s",command=refreshAudioWindow)
    
    R1.grid(row=2,column=1,pady=10)
    R2.grid(row=2,column=3,pady=10)

def resultScreen():
    for widgets in frame.winfo_children():
        widgets.destroy()
    label = Label(frame,text="Results:", font=('Helvetica',20)).grid(row=0,column=1,pady=5)
    resultField = ScrolledText(frame,width=60,height=20)
    resultField.grid(row=1,column=1)
    menuButton = Button(frame,text='Menu',command=startScreen,width=10)
    menuButton.grid(row=2,column=1,pady=8)
startScreen()
root.mainloop()