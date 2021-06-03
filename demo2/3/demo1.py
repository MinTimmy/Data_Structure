import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_entry_and_button()
        self.N = 0
        self.P = 0

    def create_entry_and_button(self):
        self.label1 = tk.Label(self.master, text="點的數量(N)：")
        self.label1.place(x = 10, y=10)
        self.entry1 = tk.Entry(self.master)
        self.entry1.place(x = 100, y = 10)

        self.label2 = tk.Label(self.master, text="次方(P)：")
        self.label1.place(x = 10, y=40)
        self.entry1 = tk.Entry(self.master)
        self.entry1.place(x = 100, y = 40)
        
        self.button1 = tk.Button(self.master, text="Submit", command=self.save_data()).place(x=300,y=10)

    def draw_F(self):
        self.canvas1 = tk.Canvas(self.master, width=1000, height=1000, background='blue')
        self.canvas1.place(x = 100, y=100)

    def save_data(self):
        self.N = int(self.entry1.get())
        self.P = int(self.entry2.get())
        self.draw_F()

root = tk.Tk(className="MMM")
root.geometry("600x400")
app = Application(root)

app.mainloop()
