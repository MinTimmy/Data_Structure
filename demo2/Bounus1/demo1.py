import tkinter as tk
import sys
from tkinter.constants import Y

from numpy import array

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.items = []
        self.N = 0
        self.array = []
        self.MAX = 0
        self.cc = []
        # self.TOTAL_NUMBER = 0
        self.ITEM = "黑棕紅橙黃綠籃紫灰白"
        self.answer_number = []
        self.answer_items = []
        self.pack()
        self.create_entry_and_button()

    def create_entry_and_button(self):
        self.label1 = tk.Label(self.master, text="測資")
        self.label1.place(x=10, y=10)
        self.entry1 = tk.Entry(self.master)
        self.entry1.place(x=90,y=10)

        
        tk.Button(self.master, text='Submit', command=self.saveData).place(x = 270, y = 10)

    def Counting_Sort(self):
        print("MAX: ",self.MAX)
        self.answer_number = [0 for i in range(self.N)]
        self.answer_items = ['-1' for i in range(self.N)]
        count = [ 0 for i in range(self.MAX)]

        for i in range(self.N):
            count[self.array[i]] += 1
        for i in range(1,self.MAX):
            count[i] += count[i-1]

        print(count)
        for i in range(self.N):
            self.answer_number[count[self.array[i]] - 1] = self.array[i]
            self.answer_items[count[self.array[i]] - 1] = self.items[i]
            count[self.array[i]] -= 1

        for i in range(1,self.N):
            string = self.answer_items[i] + " " + str(self.answer_number[i])
            label1 = tk.Label(self.master, text=string)
            label1.place(x = 10, y = 50 + i*30)

    

    def saveData(self): 
        input1 = self.entry1.get() + ' '
        self.items = []
        self.array = []
        self.N = 0
        self.MAX = 0
        self.TOTAL_NUMBER = 0

        temp = ""
        c = 0
        rr = 1
        for i in input1:
            if i != ' ':
                temp += i
                for j in range(len(self.ITEM)):
                    if i == self.ITEM[j]:
                        c += j * rr
                rr = 1
            else:
                same = False
                for j in range(len(self.items)):
                    if self.items[j] == temp:
                        same = True
                        # self.array[j]+=1
                        break
                if not same :
                    self.cc.append(1)
                    self.array.append(c)
                    self.items.append(temp)
                c = 0
                temp = ''

            rr +=1
        self.N = len(self.items)
        # self.array[self.N-1]+=1
        self.MAX = max(self.array) + 1



        # print(self.MAX)
        # print(self.items)
        print(self.array)
        # print("N: ",self.N)
        self.Counting_Sort()
        



    
root = tk.Tk(className='Python Examples - Window Size')
root.geometry("600x400")
root.fullScreenState = False
app = Application(master=root)



app.mainloop()