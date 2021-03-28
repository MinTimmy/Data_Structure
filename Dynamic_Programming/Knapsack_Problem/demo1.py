import tkinter as tk
from tkinter.constants import BOTH, LEFT, RIGHT, VERTICAL, Y
from typing import Sized

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.master = master
        self.pack()
        self.size = []
        self.value = []
        self.cost = []
        self.best = []
        self.items = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
        self.N = 0#number of item
        self.M = 17 #capacity
        # self.create_widgets()
        self.create_entry_and_button()
        # self.create_scrollingbar()
        
        # self.printTable()
        # self.printAnswer()

    def create_entry_and_button(self):
        self.label1 = tk.Label(self, text="size").grid(row=0,column=0)
        self.label2 = tk.Label(self, text="value").grid(row=1,column=0)

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0,column=1)
        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1,column=1)


        tk.Button(self, text='Submit', command=self.saveData).grid(row=3, column=1, sticky=tk.W, pady=4)
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        label1 = tk.Label(self, text="hello")
        # label1.pack()
        
    def knapsackProblem(self):
        print(self.N)
        for j in range(1, self.N+1):
            for i in range(1, self.M+1):
                if i - self.size[j-1] >= 0:
                    t = i-self.size[j-1]-1
                    if t < 0:
                        t = 0
                    if self.cost[i-1] < self.cost[t] + self.value[j-1]:
                        self.cost[i-1] = self.cost[t] + self.value[j-1]
                        self.best[i-1] = j-1
            self.printTable(j)
        self.printAnswer()

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
# for(int i = M - 1; i >= 0 && cost[i] != 0; i--){
#         int pivot = i;
#         cout << cost[pivot] << " = " << item[best[pivot]];
#         pivot -= size[best[pivot]];
#         while(pivot >= 0){
#             if(best[pivot] == -1 )
#                 break;
#             cout << " + " << item[best[pivot]];
#             pivot -= size[best[pivot]];
#         }
#         cout << '\n';
#     }
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
        tmp.append(self.entry2.get())

        tmp[0] = "3,4,7,8,9"
        tmp[1] = "4,5,10,11,13"

        for j in range(2):
            str = ""
            for i in tmp[j]:
                if i != ',':
                    str+= i
                else:
                    if j == 0:
                        self.size.append(int(str))
                    else:
                        self.value.append(int(str))
                    str = ""
            if j == 0:
                self.size.append(int(str))
            else:
                self.value.append(int(str))
             
        self.N = len(self.size)

        for i in range(self.M):
            self.cost.append(0)
            self.best.append(-1)
        print(self.size)
        print(self.value)
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