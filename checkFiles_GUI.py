
import tkinter
from tkinter import *



class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(525, 225))
        self.master.title('Check files')
        self.master.config(bg='lightgray')

        self.varBro1 = StringVar()
        self.varBro2 = StringVar()

        self.lblBro1 = Button(self.master,text="Browse...",width=15,height=1,command='')
        self.lblBro1.grid(row=1,column=0,padx=(10,0),pady=(100,0))

        self.lblBro2 = Button(self.master,text="Browse...",width=15,height=1,command='')
        self.lblBro2.grid(row=2,column=0,padx=(10,0),pady=(10,0))

        self.txtBro1 = Entry(self.master,text='',font=("Helvetica",16),fg='black',bg='white')
        self.txtBro1.grid(row=1,column=1,rowspan=1,columnspan=5,padx=(10,0),pady=(100,0))

        self.txtBro2 = Entry(self.master,text='',font=("Helvetica",16),fg='black',bg='white')
        self.txtBro2.grid(row=2,column=1,rowspan=1,columnspan=5,padx=(10,0),pady=(10,0))

        self.btnCheck = Button(self.master,text="Check for files...",width=15,height=2,command='')
        self.btnCheck.grid(row=3,column=0,padx=(10,0),pady=(10,0))

        self.btnClose = Button(self.master,text="Close Program",width=15,height=2,command=self.close)
        self.btnClose.grid(row=3,column=8,padx=(10,0),pady=(10,0))

    def close(self):
        self.master.destroy()
        




if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
