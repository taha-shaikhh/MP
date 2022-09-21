from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title('Summarizer')
root.geometry("1000x1000")

class App:
    def _init_(self,frame):
        self.frame = frame
        self.frame.pack()
        self.startScreen()
        
    def startScreen(self):    
        for widgets in self.frame.winfo_children():
            widgets.destroy()
        label = Label(self.frame,text="Summarizer", font=('Helvetica',20))
        label.grid(row=0,column=2)
        var = StringVar()
        R1 = Radiobutton(self.frame, text="Text", variable=var, value="t",command=self.refreshTextWindow)
        R2 = Radiobutton(self.frame, text="Audio", variable=var, value="s",command=self.refreshAudioWindow)
        R1.grid(row=2,column=1)
        R2.grid(row=2,column=3)
        
    def refreshTextWindow(self):
        '''
            Function to call Text input screen
        '''
        for self.widgets in self.frame.winfo_children():
            self.widgets.destroy()
        self.label = Label(self.frame,text="Summarizer", font=('Helvetica',20)).grid(row=0,column=1)
        self.text_input = StringVar()
        self.name_label = Label(self.frame, text = 'Text')
        #self.input_data = StringVar()
        #self.name_entry = Entry(self.frame,textvariable=self.input_data).grid(row=1,column=1)
        self.textField = ScrolledText(self.frame,width=60,height=20)
        self.textField.grid(row=1,column=1)
        self.name_label.grid(row=1,column=0)
        self.sub_button = Button(self.frame,text='Submit',command=self.getTextField)
        self.sub_button.grid(row=4,column=1)
        self.menu_button = Button(self.frame,text='Menu',command=self.startScreen)
        self.menu_button.grid(row=6,column=1)
        
        
    def refreshAudioWindow(self):
        '''
            Function to call Audio input screen
        '''
        for self.widgets in self.frame.winfo_children():
            self.widgets.destroy()
        l = Label(self.frame,text="Your audio is being recorded").grid(row=0,column=0)
        stop_button = Button(self.frame,text='Stop ')
        stop_button.grid(row=1,column=0)  
        menu_button = Button(self.frame,text='Menu',command=self.startScreen)
        menu_button.grid(row=2,column=0)
            
    def getTextField(self):
        #self.textInput = self.textField.get()
        print(self.textField.get("1.0","end-1c"))
            
frame = Frame(root)           
app = App(frame)

root.mainloop()