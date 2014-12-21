import Tkinter

class SimpleAppTK(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()
		self.entryVariable = Tkinter.StringVar()
		self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)              # create the Entry widget
		self.entry.grid(column=0,row=0,sticky='EW')   # add it to the grid 
		#EW means east west.. means Have the text entry expand when the window is resized.
		self.entry.bind("<Return>",self.OnPressEnter)
		self.entry.bind("<a>",self.OnPressEnter)

		self.entryVariable.set("Enter text here!")

		button = Tkinter.Button(self,text = "Click me!",command=self.OnButtonClick)
		button.grid(column=1,row=0)

		self.labelVariable = Tkinter.StringVar()
		label = Tkinter.Label(self,anchor="w",fg="white",bg="blue",textvariable=self.labelVariable) 
		# w means left align
		label.grid(column=0,row=1,columnspan=2,sticky="EW")
		self.labelVariable.set("Hello")

		self.grid_columnconfigure(0,weight=1) #col 0 responsive
		self.grid_columnconfigure(1,weight=1) #similarly we can do grid_rowconfigure

		self.resizable(True,False)  # allow only horizontal Resize (Horizontally,Vertically)
		self.update()
		self.geometry(self.geometry())
		self.entry.focus_set()
		self.entry.selection_range(0,Tkinter.END)

	def OnButtonClick(self):
		self.labelVariable.set(self.entryVariable.get()+" (button clicked)")
		self.entry.focus_set()
		self.entry.selection_range(0,Tkinter.END)

	def OnPressEnter(self,event):
		self.labelVariable.set(self.entryVariable.get()+" (pressed)")
		self.entry.focus_set()
		self.entry.selection_range(0,Tkinter.END)


if __name__ == "__main__":
	app = SimpleAppTK(None)
	app.title("My application")
	app.mainloop()
