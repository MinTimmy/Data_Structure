import tkinter as tk
from tkinter.constants import BOTH, LEFT, N, RIGHT, VERTICAL, Y
from typing import Sized
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
        self.label1 = tk.Label(self, text="r").grid(row=0,column=0)

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0,column=1)
        # self.entry1.pack(row=0,column=1)
        


        tk.Button(self, text='Submit', command=self.saveData).grid(row=3, column=1, sticky=tk.W, pady=4)
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
            self.printTable(j)
        print(self.cost)
        print(self.items[i])
        # self.printAnswer()

    def printTable(self, j):
        canvas = tk.Canvas(self)
        canvas.create_line(0, 25, 10, 25)
        # canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        # canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        canvas.grid()
        # canvas.place()
        # string = "cost: "
        # for i in self.cost:
        #     print( i,end=' ')
        #     string += str(i) + ' , '
        # print('\n')

        # # label1 = tk.Label(text=str).grid(row=j+4, column=0)
        # label1 = tk.Label(text=string).place(x=50,y=80+j*70)

        # string = "best: "
        # for i in self.best:
        #     print(self.items[i], end = ' ')
        #     string += str(self.items[i]) + ' , '
        # print('\n---------------------------------------------------------\n')

        # # label2 = tk.Label(text=str).grid(row=j+5, column=0)
        # label1 = tk.Label(text=string).place(x=50,y=100+j*70)


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