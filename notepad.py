from functools import cache
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox

@cache
class notepad():
    def __init__(self):
        self.root = Tk()
        self.root.config(background='black')
        self.root.title('Sahil khan notepad')
        self.root.resizable(False,False)
        # self.root.geometry('500x500')
        self.navbar()
        self.root.mainloop()
    def navbar(self):
        self.navbar_frame = Frame(self.root)
        self.navbar_frame.grid(row=0,column=0,sticky='nsew')
        self.menubar = Menu(self.navbar_frame,background='white',
                        foreground='black',activebackground='black',
                        activeforeground='white')
        # self.menubar.grid(row=0,column=0)
        self.file = Menu(self.menubar,tearoff=0,background='white',foreground='black')
        self.file.add_command(label='New',command=self.new)
        self.file.add_command(label='Open',command=self.Open)
        self.file.add_command(label='Save',command=self.save)
        self.file.add_command(label='Save as',command=self.save_as)
        self.file.add_separator()
        self.file.add_command(label='Exit',command=self.root.quit)
        self.menubar.add_cascade(label='File',menu=self.file)
        self.edit = Menu(self.menubar,tearoff=0)
        self.edit.add_command(label='undo',command=self.undo)
        self.edit.add_command(label='redo',command=self.redo)
        self.edit.add_separator()
        self.edit.add_command(label='Cut',command=self.cut)
        self.edit.add_command(label='Copy',command=self.copy)
        self.edit.add_command(label='Paste',command=self.paste)
        self.menubar.add_cascade(label='Edit',menu=self.edit)
        self.help = Menu(self.menubar,tearoff=0)
        self.help.add_command(label='About',command=self.about)
        self.menubar.add_cascade(label='Help',menu=self.help)
        self.root.config(menu=self.menubar)
        self.root.bind('<Control-s>',lambda event: self.save())
        self.root.bind('<Control-z>',lambda event: self.undo())
        self.root.bind('<Control-y>',lambda event: self.redo())
        self.root.bind('<Control-p>',lambda event: self.paste())
        self.root.bind('<Control-c>',lambda event: self.copy())
        self.root.bind('<Control-x>',lambda event: self.cut())
        self.root.bind('<Control-a>',lambda event: self.select_all())
        self.root.bind('<Alt-F4>',lambda event: self.quit())
        self.root.bind('<Control-o>',lambda event: self.Open())
        self.body()
    def body(self):
        self.body_frame = Frame(self.root)
        self.body_frame.grid(row=1,column=0,sticky='nsew')
        self.entry = scrolledtext.ScrolledText(self.body_frame,relief='flat',selectbackground='white',foreground='black',xscrollcommand=HORIZONTAL,highlightcolor='black',cursor='arrow')
        self.entry.grid(row=0,column=0,sticky='nesw')
        # self.entry.pack(expand=True,fill=BOTH)
    def Open(self):
        self.root.filename = filedialog.askopenfilename(
                initialdir = '/',
                title="Select file",
                filetypes=(("text file","*.txt"),("all files","*.*")))
        file = open(self.root.filename)
        self.entry.insert('end',file.read())
    def save(self):
        self.save_as()
    def save_as(self):
        self.root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt',filetypes=(("text file","*.txt"),("all files","*.*")))
        if self.root.filename is None:
                return
        file_save =  str(self.entry.get(1.0,END))
        self.root.filename.write(file_save)
        self.root.filename.close()
    def cut(self):
        self.entry.event_generate("<<Cut>>")
    def copy(self):
        self.entry.event_generate('<<Copy>>')
    def paste(self):
        self.entry.event_generate("<<Paste>>")
    def new(self):
        self.message = messagebox.askquestion('Notepad',"Do you want to Delete all")
        if self.message == "yes":
                self.entry.delete('1.0','end')
        else:
               return "break"
    def about(self):
        messagebox.showinfo("Notepad","Sahil khan")
    def undo(self):
        self.entry.edit_undo()
    def redo(self):
        self.entry.edit_redo()
    def select_all(self):
        self.entry.tag_add(SEL, "1.0", END)
        self.entry.mark_set(INSERT, "1.0")
        self.entry.see(INSERT)
        self.entry.tag_configure(SEL,background="black", foreground= "white")
        return 'break'
if __name__ == '__main__':
    note = notepad()