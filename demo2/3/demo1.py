import tkinter as tk
import random

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.canvas1 = tk.Canvas(self.master, width=1000, height=1000, background='green')
        self.canvas1.place(x = 100, y=100)
        self.N = 0
        self.P = 0
        self.area = 0
        self.counter = 0
        self.create_entry_and_button()

    def create_entry_and_button(self):
        self.label1 = tk.Label(self.master, text="點的數量(N)：")
        self.label1.place(x = 10, y=10)
        self.entry1 = tk.Entry(self.master)
        self.entry1.place(x = 100, y = 10)

        self.label2 = tk.Label(self.master, text="次方(P)：")
        self.label2.place(x = 10, y=40)
        self.entry2 = tk.Entry(self.master, )
        self.entry2.place(x = 100, y = 40)
        
        tk.Button(self.master, text="Submit", command=self.save_data).place(x=300,y=10)

    def draw_F(self):
        self.init_point = [10,50]
        self.scale = 800
        self.Arrow = 10
        self.canvas1.create_line(self.init_point[0], self.init_point[1], self.init_point[0] + 1 * self.scale, self.init_point[1] + 1, width=2)
        self.canvas1.create_line(self.init_point[0], self.init_point[1], self.init_point[0] + 1, self.init_point[1] + 1 * self.scale, width=2)

        # create arrow
        self.canvas1.create_line(self.init_point[0] + 1 * self.scale - self.Arrow, self.init_point[1] - self.Arrow, self.init_point[0] + 1 * self.scale, self.init_point[1], width=2)
        self.canvas1.create_line(self.init_point[0] + 1 * self.scale - self.Arrow, self.init_point[1] + self.Arrow, self.init_point[0] + 1 * self.scale, self.init_point[1], width=2)
        self.canvas1.create_line(self.init_point[0] - self.Arrow, self.init_point[1] + 1 * self.scale - self.Arrow, self.init_point[0], self.init_point[1] + 1 * self.scale , width=2)
        self.canvas1.create_line(self.init_point[0] + self.Arrow, self.init_point[1] + 1 * self.scale - self.Arrow, self.init_point[0], self.init_point[1] + 1 * self.scale, width=2 )

        # create X Y
        center = [self.init_point[0] + 1 * self.scale + 20, self.init_point[1] ]
        self.canvas1.create_line(center[0] - 5, center[1] - 5, center[0] + 5, center[1] +5, width=2)
        self.canvas1.create_line(center[0] - 5, center[1] + 5, center[0] + 5, center[1] -5, width=2)
        center = [self.init_point[0] , self.init_point[1] + 1 * self.scale + 20]
        self.canvas1.create_line(center[0] - 5, center[1] - 5, center[0], center[1], width=2)
        self.canvas1.create_line(center[0] + 5, center[1] - 5, center[0], center[1], width=2)
        self.canvas1.create_line(center[0], center[1], center[0], center[1] + 5, width=2)

        # create F(x)
        for i in range(100000):
            x = float(i / 1000)
            y = float(pow(x,self.P))
            if y <= 1:
                self.canvas1.create_oval(self.init_point[0] + x * self.scale, self.init_point[1] + y * self.scale, self.init_point[0] + x * self.scale, self.init_point[1] + y * self.scale, width=2,outline='blue')

        for i in range(self.N):
            x = random.uniform(0,1)
            y = random.uniform(0,1)

            if y <= pow(x ,self.P):
                self.canvas1.create_oval(self.init_point[0] + x * self.scale, self.init_point[1] + y * self.scale, self.init_point[0] + x * self.scale, self.init_point[1] + y * self.scale, width=1, outline='red')
                self.counter+=1
            else:
                self.canvas1.create_oval(self.init_point[0] + x * self.scale, self.init_point[1] + y * self.scale, self.init_point[0] + x * self.scale, self.init_point[1] + y * self.scale, width=1,outline='black')
        

        self.area = 1 * self.counter / self.N
        self.label3 = tk.Label(self.canvas1, text="面積大約為： " + str(self.area),background='green')
        self.label3.place(x = 5, y = 5)
        self.counter = 0
            


    def save_data(self):
        temp = self.entry1.get()
        if temp == '':
            temp = '10000'
        self.N = int(temp)

        temp = self.entry2.get()
        if temp == '':
            temp = '2'
        self.P = int(temp)

        self.canvas1.delete('all') 
        self.draw_F()

root = tk.Tk(className="MMM")
root.geometry("600x400")
app = Application(root)

app.mainloop()
