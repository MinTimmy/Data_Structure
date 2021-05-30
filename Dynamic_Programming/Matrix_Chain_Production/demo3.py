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
        self.answer = []
        self.N = 0 #number of item
        self.create_entry_and_button()
        # self.create_scrollingbar()
        
        # self.printTable()
        # self.printAnswer()

    def create_entry_and_button(self):
        self.label1 = tk.Label(self.master, text="r")
        self.label1.place(x=10, y=10)
        self.entry1 = tk.Entry(self.master)
        self.entry1.place(x=20,y=10)
        
        tk.Button(self.master, text='Submit', command=self.saveData).place(x = 200, y = 10)
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        label1 = tk.Label(self, text="hello")
       
    def Matrix_Chain_Production(self):
        print(self.N, end='\n')
        for j in range(1, self.N):
            for i in range(1, self.N-j+1):
                for k in range(i+1, i+j+1):
                    t = self.cost[i-1][k-1-1] + self.cost[k-1][i+j-1] + self.r[i-1] * self.r[k-1] * self.r[i+j+1-1]
                    if t < self.cost[i-1][i+j-1]:
                        self.cost[i-1][i+j-1] = t
                        self.best[i-1][i+j-1] = k-1
                        
        self.printAnswer(0, self.N-1)
        string = 'Final answer: '
        for i in self.answer:
            string += i
        # print(string)
        label1 = tk.Label(self.master, text=string).place(x = 300, y = 10)
        self.printTable()
       

    def printTable(self):
        
        self.table_square = 100
        self.table_size = (self.N +1) * self.table_square
        string = ""
        for i in range(self.N):
            label1 = tk.Label(self.master, text=self.items[i]).place(x= 30 + self.table_square + self.table_square / 2 + i*self.table_square, y=30+self.table_square/2)
            label1 = tk.Label(self.master, text=self.items[i]).place(x=30 +self.table_square / 2, y=30 + self.table_square*1.5 + i*self.table_square)
            canvas1 = tk.Canvas(self.master,bg='red',width=self.table_size,height=1)
            canvas1.create_line(0,1,self.table_size,1)
            canvas1.place(x = 30, y = 30 + (i+1)*self.table_square)
            canvas2 = tk.Canvas(self.master,bg='red',width=1,height=self.table_size)
            canvas2.create_line(1,0,1,self.table_size)
            canvas2.place(x = 30+(i+1)*self.table_square, y = 30)

        for j in range(self.N):
            print(self.best[j])

        for r in range(self.N):
            for c in range(self.N):
                if self.cost[r][c] == -1:
                    string = "?"
                elif r == c:
                    string = "0"
                else:
                    string += self.items[self.best[r][c]] + str(self.cost[r][c])
                # label1 = tk.Label(self.master, text=string).grid(row=r*2+1,column=c+1)
                label1 = tk.Label(self.master, text=string).place(x=30+(c+1.5)*(self.table_square),y=30+(r+1.5)*(self.table_square))
                string = ""
            # canvas.grid(row=r*2+1)
        print('\n')

    def printAnswer(self, left, right):
        print("left: ", left, '\t', "right: ", right)

        i = 0
        while self.answer[i] != self.items[left]:
            i+=1
        self.answer.insert(i, '(')

        i = 0
        while self.answer[i] != self.items[right]:
            i+=1
        self.answer.insert(i+2, ')')

        i = 0
        while self.answer[i] != self.items[self.best[left][right]]:
            i+=1

        
        self.answer.insert(i, '(')
        
        self.answer.insert(i, ')')
    
        if left < self.best[left][right] - 2:
            self.printAnswer(left, self.best[left][right]-1)
        if right > self.best[left][right]+1:
            self.printAnswer(self.best[left][right], right)

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
        tmp = ""
        tmp = self.entry1.get()

        if tmp == "":
            tmp = "4,2,3,1,2,2,3"
        self.N = 0
        self.cost = []
        self.best = []
        self.r = []
        str = ""
        for i in tmp:
            if i != ',':
                str+= i
            else:
                self.r.append(int(str))
                str = ""
        
        
        self.r.append(int(str))
        self.N = len(self.r)
        self.N-=1
        c = []
        b = []
        # for i in range(self.N):
        #     b.append(-1)

        for i in range(self.N):
            for j in range(self.N):
                if i == j:
                    c.append(0)
                if i < j:
                    c.append(sys.maxsize)
                if i > j:
                    c.append(-1)
                b.append(-1)
            self.cost.append(c)
            c = []
            self.best.append(b)
            b=[]
        self.answer = []
        for i in range(self.N):
            self.answer.append(self.items[i])
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