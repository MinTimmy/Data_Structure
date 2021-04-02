import tkinter as tk
from tkinter.constants import BOTH, LEFT, RIGHT, VERTICAL, Y
from typing import Counter, Sized
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
        # self.create_widgets()
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
        # print(self.N)
        for j in range(1, self.N+1):
            for i in range(1, self.M+1):
                if i - self.size[j-1] >= 0:
                    t = i-self.size[j-1]-1
                    if t < 0:
                        t = 0
                    if self.cost[i-1] < self.cost[t] + self.value[j-1]:
                        self.cost[i-1] = self.cost[t] + self.value[j-1]
                        self.best[i-1] = j-1
            # print(j)
            # print(self.cost)
            # print(self.best)
            # self.printTable(j)
            self.printAnswer(j)
    # def knapsackProblem(self):
    #     print(self.N)
    #     for j in range(1, self.N+1):
    #         for i in range(1, self.M+1):
    #             if i - self.size[j-1] >= 0:
    #                 t = i-self.size[j-1]-1
    #                 if t < 0:
    #                     t = 0
    #                 if self.cost[i-1] < self.cost[t] + self.value[j-1]:
    #                     self.cost[i-1] = self.cost[t] + self.value[j-1]
    #                     self.best[i-1] = j-1
    #         self.printTable(j)
    #     self.printAnswer()
        
    def printTable(self, j):
        string = "cost: "
        for i in self.cost:
            print( i,end=' ')
            string += str(i) + ' , '
        print('\n')

        # label1 = tk.Label(text=str).grid(row=j+4, column=0)
        label1 = tk.Label(text=string).place(x=50,y=80+j*70)

        string = "best: "
        for i in self.best:
            print(self.items[i], end = ' ')
            string += str(self.items[i]) + ' , '
        print('\n---------------------------------------------------------\n')

        # label2 = tk.Label(text=str).grid(row=j+5, column=0)
        label1 = tk.Label(text=string).place(x=50,y=100+j*70)


 
    # def printTable(self, j):
    #     string = "cost: "
    #     for i in self.cost:
    #         print( i,end=' ')
    #         string += str(i) + ' , '
    #     print('\n')

    #     # label1 = tk.Label(text=str).grid(row=j+4, column=0)
    #     label1 = tk.Label(text=string).place(x=50,y=80+j*70)

    #     string = "best: "
    #     for i in self.best:
    #         print(self.items[i], end = ' ')
    #         string += str(self.items[i]) + ' , '
    #     print('\n---------------------------------------------------------\n')

    #     # label2 = tk.Label(text=str).grid(row=j+5, column=0)
    #     label1 = tk.Label(text=string).place(x=50,y=100+j*70)

    def printAnswer(self, j):
        pivot = self.M - 1
        string = ""
        string += self.items[self.best[pivot]]
        pivot -= self.size[self.best[pivot]]
        count = 0
        while pivot >= 0:
            if self.best[pivot] == -1:
                break
            string += " + " + self.items[self.best[pivot]]
            if len(string) - count * 200 > 200:
                count += 1
                string += '\n'
            pivot -= self.size[self.best[pivot]]
        label = tk.Label(text=string)
        str = 
        label1 = tk.Label()
        print(j+self.newLine)
        label.place(x = 10, y = 40 + (j + self.newLine) * 17)
        self.newLine += count
    
    # def printAnswer(self):
    #     i = self.M - 1
    #     while i >=0 and self.cost[i] != 0:
    #         pivot = i
    #         string = ""
    #         string += str(self.cost[pivot]) + " = " + self.items[self.best[pivot]]
    #         pivot -= self.size[self.best[pivot]]
    #         while pivot >= 0:
    #             if self.best[pivot] == -1:
    #                 break
    #             string += self.items[self.best[pivot]]
    #             pivot -= self.size[self.best[pivot]]
    #         label = tk.Label(text=string)
    #         label.place(x = 600, y = 10+i*20)
    #         i-=1
    # def create_scrollingbar(self):
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
        tmp.append(self.entry2.get())

        if tmp[0] == "" or tmp[1] == "":
            tmp[0] = "670"
            tmp[1] = "Salmon,Tuna,Fenneropenaeus,Gratilla,Kuroge"

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
        # print(self.N)
        # print(self.cost_upper_bound)
        # for i in range(self.N):
        #     print(self.items[i], self.size[i], self.value[i])

        for i in range(self.M):
            self.cost.append(0)
            self.best.append(-1)
        # print(self.size)
        # print(self.value)
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