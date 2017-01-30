import tkinter

from .pyenvmanager import PyEnvManager

class MenuFrame(tkinter.Frame):

    def __init__(self, master=None):
        self.master = master
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.createMenu()

    def createMenu(self):
        self.create_button = tkinter.Button(self, text="create", command=self.create_on_click)
        self.create_button.grid(row=0, column=0)
        self.delete_button = tkinter.Button(self, text="delete", command=self.delete_on_click)
        self.delete_button.grid(row=0, column=1)
        self.env_name = tkinter.Entry(self, width=20)
        self.env_name.grid(row=0, column=2)

    def create_on_click(self):
        self.master.env_manager.create_environment(self.env_name.get())
        self.env_name.delete(0, tkinter.END)
        self.master.list_environments()

    def delete_on_click(self):
        selected_row = self.master.env_listbox.curselection()
        if selected_row:
            name = self.master.env_listbox.get(selected_row)
            self.master.env_manager.delete_environment(name)
            self.master.list_environments()


class PyEnvManagerApp(tkinter.Frame):
    """GUI Application for the virtualenv Manager"""

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.env_manager = PyEnvManager()
        self.grid()
        self.createWidgets()

    def list_environments(self):
        self.env_listbox.delete(0, tkinter.END)
        for env in self.env_manager.environments():
            self.env_listbox.insert(tkinter.END, env)
        self.env_listbox.grid(row=1, column=0)

    def createWidgets(self):
        self.menu = MenuFrame(master=self)
        self.menu.grid(row=0, column=0)
        self.yScroll = tkinter.Scrollbar(self, orient=tkinter.VERTICAL)
        self.yScroll.grid(row=1, column=1, sticky=tkinter.N + tkinter.S)
        self.env_listbox = tkinter.Listbox(self,
                                           selectmode=tkinter.SINGLE,
                                           yscrollcommand=self.yScroll.set,
                                           height=10,
                                           width=50
        )
        self.env_listbox.bind('<Double-Button-1>', self.start_env_handler)
        self.env_listbox.grid(row=1, column=0)
        self.list_environments()

    # TODO: implement on click event for starting a cli terminal with selected environment
    def start_env_handler(self, event):
        selected_row = self.env_listbox.curselection()
        name = self.env_listbox.get(selected_row)
        self.env_manager.open_environment(name)

#app = PyEnvManagerApp()
#app.master.title('VirtualEnv Manager')
#app.mainloop()
