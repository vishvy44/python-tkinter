from tkinter import *
class Application(Frame):
	def  __init__(self, master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.theLabel=Label(self, text="                                SNAPPER    CODE")
		self.theLabel.config(font=(60),fg='orange',bg='grey',height=2)
		self.theLabel1 = Label(self, text = 'First Name')
		self.theLabel1.config(font=60,fg='red',bg='grey')
		self.theLabel2 = Label(self, text = 'Last Name')
		self.theLabel2.config(font=60,fg='red',bg='grey')
		self.theLabel3 = Label(self, text = 'Email Address')
		self.theLabel3.config(font=60,fg='red',bg='grey')
		self.theLabel4 = Label(self, text = 'Password')
		self.theLabel4.config(font=60,fg='red',bg='grey')

		self.theLabel.grid(row=0, column=0, sticky='NW')
		self.theLabel1.grid(row=1, column=0, sticky='W')
		self.theLabel2.grid(row=2, column=0, sticky='W')
		self.theLabel3.grid(row=3, column=0, sticky='W')
		self.theLabel4.grid(row=4, column=0, sticky='W')



		self.entry1 = Entry(self)
		self.entry2 = Entry(self)
		self.entry3 = Entry(self)
		self.entry4 = Entry(self, show='*')

		self.entry1.grid(row=1, column=1)
		self.entry2.grid(row=2, column=1)
		self.entry3.grid(row=3, column=1)
		self.entry4.grid(row=4, column=1)


		self.theLabel5 = Label(self, text = 'Gender')
		self.theLabel5.grid(row=6, column=0, sticky='w')
		self.theLabel5.config(font=60,fg='red',bg='grey')
		self.R1 = Radiobutton(self, text="FEMALE", value=1).grid(row=7, sticky='w')

		self.R2 = Radiobutton(self, text="MALE", value=2).grid(row=7,column=1, sticky='w')

		
		self.button1 = Button(self, text = 'SIGN UP',command=self.signn)
		self.button1.grid(row=8, column= 0, sticky='N')
		self.button2 = Button(self, text = 'CANCEL',command=self.canc)
		self.button2.grid(row=8, column= 0, sticky='E')
		self.text=Text(self,width=35,height=1,wrap=WORD)
		self.text.grid(row=9,column=0,columnspan=2,sticky='w')
		self.configure(background='grey')  
	def signn(self):
		content=self.entry3.get()
		if content=="vishvy123@gmail.com":
			message="registration succesful"
		else:
			message="incorrect email"
		self.text.insert(0.0,message)
	def canc(self):
		self.text.delete(0.0,END)
		self.entry1.delete(0,END)
		self.entry2.delete(0,END)
		self.entry3.delete(0,END)
		self.entry4.delete(0,END)
root=Tk()
root.title("snappercode")


app=Application(root)
root.mainloop()
