import collections
import tkinter as tk
from tkinter.constants import BOTH, LEFT, N, RIGHT, VERTICAL, Y
from typing import Collection, Sized
import sys

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.r= []
        self.cost = []
        self.best = []
        self.items = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
        self.N = 0 #number of item
        self.create_entry_and_button()
        # self.create_scrollingbar()
        
        # self.printTable()
        # self.printAnswer()

    def create_entry_and_button(self):
        # self.init_frame = tk.Frame(self, width=2000, height= 400, bg='grey')
        self.init_frame = tk.Frame(self, bg='grey')
        # self.main_frame.pack(fill=BOTH, expand=1)
        self.init_frame.grid(row=0, column=0, padx=0, pady=0)

        # self.label1 = tk.Label(self, text="r").grid(row=0,column=0)
        self.label1 = tk.Label(self.init_frame, text="r")
        self.label1.grid(row=0, column=0, padx=5, pady=5)

        self.entry1 = tk.Entry(self.init_frame)
        self.entry1.grid(row=0,column=1)
        # self.entry1.pack(row=0,column=1)
        # self.entry1.place(x=10,y=15)
        
        tk.Button(self.init_frame, text='Submit', command=self.saveData).grid(row=0, column=3, sticky=tk.W, pady=4)
        # tk.Button(self, text='Submit', command=self.saveData).place(x = 10, y = 30)
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        label1 = tk.Label(self, text="hello")
        # label1.pack()
        
    def Matrix_Chain_Production(self):
        # print(self.N, end='\n')
        for j in range(1, self.N-1+1):
            for i in range(1, self.N-j):
                for k in range(i+1, i+j+1):
                    t = self.cost[i-1][k-1-1] + self.cost[k-1][i+j-1] + self.r[i-1] * self.r[k-1] * self.r[i+j+1-1]
                    # print(self.cost[i-1][k-1-1] , self.cost[k-1][i+j-1],t)
                    # print(k-1, i , j,i+j-1)
                    if t < self.cost[i-1][i+j-1]:
                        self.cost[i-1][i+j-1] = t
                        self.best[i-1][i+j-1] =k-1 
                        # print(self.cost)

        self.printTable()
        print(self.cost)
        print(self.items[i])
        # self.printAnswer()

    def printTable(self):
        self.table_frame = tk.Frame(self)
        self.table_frame.grid(row=1, column=0)

        string = ""
        for i in range(self.N-1):
            label1 = tk.Label(self.table_frame, text=self.items[i]).grid(row=0, column=i+1)
            label1 = tk.Label(self.table_frame, text=self.items[i]).grid(row=i+1, column=0)
            canvas = tk.Canvas(self.table_frame)
            canvas.create_line(0,1,10,1)
            canvas.grid(row=1,column=i)

        for r in range(self.N-1):
            for c in range(self.N-1):
                string += self.items[self.best[r][c]] + str(self.cost[r][c])
                label1 = tk.Label(self.table_frame, text=string).grid(row=r*2+1,column=c+1)
                string = ""
            # canvas.grid(row=r*2+1)
        print('\n')


    def printAnswer(self):
        i = self.M - 1
        while i >=0 and self.cost[i] != 0:
            pivot = i
            string = ""
            string += str(self.cost[pivot]) + " = " + self.items[self.best[pivot]]
            pivot -= self.size[self.best[pivot]]
            while pivot >= 0:
                if self.best[pivot] == -1:
                    break
                string += self.items[self.best[pivot]]
                pivot -= self.size[self.best[pivot]]
            label = tk.Label(text=string)
            label.place(x = 600, y = 10+i*20)
            i-=1

    def create_scrollingbar(self):
        self.main_frame = tk.Frame(self)

        self.main_frame.pack(fill=BOTH, expand=1)

        self.my_canvas = tk.Canvas(self.main_frame)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.my_scrollbar = tk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))
    def saveData(self): 
        tmp = []
        tmp.append(self.entry1.get())

        tmp = "4,2,3,1,2,2,3"

        str = ""
        for i in tmp:
            if i != ',':
                str+= i
            else:
                self.r.append(int(str))
                str = ""
        
        
        self.r.append(int(str))
        self.N = len(self.r)

        c = []
        b = []
        for i in range(self.N-1):
            b.append(-1)

        for i in range(self.N-1):
            for j in range(self.N-1):
                if i == j:
                    c.append(0)
                if i < j:
                    c.append(sys.maxsize)
                if i > j:
                    c.append(-1)
            self.cost.append(c)
            c = []
            self.best.append(b)

        # print(self.cost)
        self.Matrix_Chain_Production()

root = tk.Tk(className='Python Examples - Window Size')
# scrollbar = tk.Scrollbar(root)
# scrollbar.pack( side=RIGHT, fill=Y )
root.geometry("600x400")
# root.attributes('-fullscreen', True)
root.fullScreenState = False
# root.window.bind("<F11>", root.toggleFullScreen)
# root.window.bind("<Escape>", root.quitFullScreen)
app = Application(master=root)



# container = tk.Frame(root)
# canvas = tk.Canvas(container)
# scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
# container.pack()
# canvas.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="right", fill="y")
app.mainloop()