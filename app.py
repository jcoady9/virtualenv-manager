import tkinter

from pyenvmanager import PyEnvManager

class PyEnvManagerApp(tkinter.Frame):
    """GUI Application for the virtualenv Manager"""

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.env_manager = PyEnvManager()
        self.grid()
        self.createWidgets()

    def list_environments(self):
        for env in self.env_manager.environments():
            self.env_listbox.insert(tkinter.END, env)
        self.env_listbox.grid(row=1, column=0)

    def createWidgets(self):
        self.create_button = tkinter.Button(self, text="create", command=self.create_on_click)
        self.create_button.grid(row=0, column=0)
        self.delete_button = tkinter.Button(self, text="delete", command=self.delete_on_click)
        self.delete_button.grid(row=0, column=1)
        self.env_name = tkinter.Entry(self, width=20)
        self.env_name.grid(row=0, column=2)
        self.yScroll = tkinter.Scrollbar(self, orient=tkinter.VERTICAL)
        self.yScroll.grid(row=1, column=1, sticky=tkinter.N + tkinter.S)
        self.env_listbox = tkinter.Listbox(self,
                                           selectmode=tkinter.SINGLE,
                                           yscrollcommand=self.yScroll.set,
                                           height=10,
                                           width=50
        )
        self.list_environments()

    def create_on_click(self):
        self.env_manager.create_environment(self.env_name.get())
        self.env_name.delete(0, tkinter.END)
        self.list_environments()

    def delete_on_click(self):
        self.env_manger.delete_environment()



app = PyEnvManagerApp()
app.master.title('VirtualEnv Manager')
app.mainloop()
