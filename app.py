import tkinter

from pyenvmanager import PyEnvManager

class PyEnvManagerApp(tkinter.Frame):
    """GUI Application for the virtualenv Manager"""

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.env_manager = PyEnvManager()
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.create_button = tkinter.Button(self, text="create")
        self.create_button.grid(row=0, column=0)
        self.delete_button = tkinter.Button(self, text="delete")
        self.delete_button.grid(row=0, column=1)
        self.yScroll = tkinter.Scrollbar(self, orient=tkinter.VERTICAL)
        self.yScroll.grid(row=1, column=1, sticky=tkinter.N + tkinter.S)
        self.env_listbox = tkinter.Listbox(self,
                                           selectmode=tkinter.SINGLE,
                                           yscrollcommand=self.yScroll.set,
                                           height=10,
                                           width=50
        )
        for env in self.env_manager.environments():
            self.env_listbox.insert(tkinter.END, env)
        self.env_listbox.grid(row=1, column=0)


    # TODO: create event handler for 'create' button
    # TODO: create event handler for 'delete' button



app = PyEnvManagerApp()
app.master.title('VirtualEnv Manager')
app.mainloop()
