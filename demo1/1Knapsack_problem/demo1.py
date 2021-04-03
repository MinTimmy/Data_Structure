import tkinter as tk
from tkinter.constants import BOTH, LEFT, RIGHT, VERTICAL, Y
from typing import Counter, Sized
from tkinter.tix import *


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.master = master
        self.pack()
        self.SIZE = [153, 260, 67, 93, 152, 50, 58, 13, 166, 77, 151, 60]
        self.size = []
        self.VALUE = [253, 530, 153, 196, 250, 87, 191, 33,431, 90, 180, 100]
        self.value = []
        self.COST = []
        self.cost = []
        self.best = []
        self.ITEMS = ["Salmon", "Tuna",  "Istiophoridae" ,"Fenneropenaeus", "Borealis", "Adductor", "Haliotis", "Gratilla", "Kuroge", "Chionoecetes", "Eriocheir", "Palinuridae", "?"]
        self.items = []
        self.N = 0#number of item
        self.M = 17 #capacity
        self.cost_upper_bound = 0
        self.newLine = 0
        self.create_scrollingbar()
        self.create_entry_and_button()

    def create_entry_and_button(self):
        self.label1 = tk.Label(self.master, text="胃容量").place(x = 5, y=10)
        self.label2 = tk.Label(self.master, text="食材名稱").place(x = 5, y = 30)

        self.entry1 = tk.Entry(self.master)
        self.entry1.place(x = 80, y = 10)
        self.entry2 = tk.Entry(self.master)
        self.entry2.place(x = 80, y = 30)

        tk.Button(self.master, text='Submit', command=self.saveData).place(x = 250, y = 10)
        
    def knapsackProblem(self):
        self.newLine = 0
        for j in range(1, self.N+1):
            for i in range(1, self.M+1):
                if i - self.size[j-1] >= 0:
                    t = i-self.size[j-1]-1
                    if t < 0:
                        t = 0
                    if self.cost[i-1] < self.cost[t] + self.value[j-1]:
                        self.cost[i-1] = self.cost[t] + self.value[j-1]
                        self.best[i-1] = j-1
            
            self.printAnswer(j-1)
 
    def printAnswer(self, j):
        pivot = self.M - 1
        string = ""
        string += self.items[self.best[pivot]]
        pivot -= self.size[self.best[pivot]]
        y_gap = 18
        label3 = tk.Label(text="僅考慮：").place(x = 10, y = 50 + self.newLine * y_gap)
        str = ""
        for i in range(j+1):
            str += "," + self.items[i]
        label2 = tk.Label(text=str, fg='red').place(x = 50, y = 50 + self.newLine * y_gap)
        self.newLine += 1

        while pivot >= 0:
            if self.best[pivot] == -1:
                break
            string += " + " + self.items[self.best[pivot]]
            if len(string) > 200:
                label1 = tk.Label(text=string).place(x = 10, y = 50 + self.newLine * y_gap)
                string = ""
                self.newLine += 1
            pivot -= self.size[self.best[pivot]]
        label = tk.Label(text=string).place(x = 10, y = 50 + self.newLine * y_gap)
        self.newLine += 1
        str = "-----------"
        for i in range(5):
            str += str
        labe4 = tk.Label(text=str).place(x = 0, y = 50 + self.newLine * y_gap)
        self.newLine += 1
    def create_scrollingbar(self):
        self.main_frame = tk.Frame(self)

        self.main_frame.pack(fill=BOTH, expand=1)

        self.my_canvas = tk.Canvas(self.master)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.my_scrollbar = tk.Scrollbar(self.master, orient=VERTICAL)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)
        self.my_scrollbar.configure(command = self.master.yview)
        
        # self.master.configure(yscrollcommand=self.my_scrollbar.set)
        # self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))

    # def create_scrollingbar(self):
    #     self.main_frame = tk.Frame(self)

    #     self.main_frame.pack(fill=BOTH, expand=1)

    #     self.my_canvas = tk.Canvas(self.master)
    #     self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    #     self.my_scrollbar = tk.Scrollbar(self.master, orient=VERTICAL, command=self.my_canvas.yview)
    #     self.my_scrollbar.pack(side=RIGHT, fill=Y)

    #     self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
    #     self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))
    def saveData(self): 
        tmp = []
        tmp.append(self.entry1.get())
        tmp.append(self.entry2.get())

        if tmp[0] == "" or tmp[1] == "":
            tmp[0] = "670"
            tmp[1] = "Salmon,Tuna,Fenneropenaeus,Gratilla,Kuroge"
        tmp[0] = "2000"
        tmp[1] = "Salmon,Tuna,Istiophoridae,Fenneropenaeus,Borealis,Adductor,Haliotis,Gratilla,Kuroge,Chionoecetes,Eriocheir,Palinuridae"
        str = ""
        for i in tmp[1]:
            if i != ',':
                str += i
            else:
                n = 0
                while str != self.ITEMS[n]:
                    n+=1
                self.items.append(self.ITEMS[n])
                self.size.append(self.SIZE[n])
                self.value.append(self.VALUE[n])
                str = ""
        n = 0
        while str != self.ITEMS[n]:
            n+=1
        self.items.append(self.ITEMS[n])
        self.size.append(self.SIZE[n])
        self.value.append(self.VALUE[n])
        self.N = len(self.items)
        self.M = int(tmp[0])
        self.cost_upper_bound = int(tmp[0])
        for i in range(self.M):
            self.cost.append(0)
            self.best.append(-1)
        self.knapsackProblem()

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