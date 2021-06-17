import tkinter as tk
import sys
from tkinter.constants import Y

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.M = 0
        self.D = []
        self.T = []
        self.pack()
        self.create_entry_and_button()

    def create_entry_and_button(self):
        self.label1 = tk.Label(self.master, text="地圖張數(M)：")
        self.label1.place(x=10, y=10)
        self.entry1 = tk.Entry(self.master)
        self.entry1.place(x=90,y=10)

        self.label2 = tk.Label(self.master, text="測資路線長(D)：")
        self.label2.place(x=10, y=50)
        self.entry2 = tk.Entry(self.master)
        self.entry2.place(x=90,y=50)
        
        self.label3 = tk.Label(self.master, text="測資時間(T)：")
        self.label3.place(x=10, y=100)
        self.entry3 = tk.Entry(self.master)
        self.entry3.place(x=90,y=100)
        
        tk.Button(self.master, text='Submit', command=self.saveData).place(x = 270, y = 10)


    def cal(self):
        sum1 = 0.0
        for i in self.D:
            sum1 += i
        sum2 = 0.0
        for i in self.T:
            sum2 += i
        print(sum1)
        print(sum2)
        sum = float(sum1 / sum2)
        label = tk.Label(self.master, text=str(sum))
        label.place(x = 10, y = 150)

    def saveData(self): 
        input1 = self.entry1.get()
        input2 = self.entry2.get()
        input3 = self.entry3.get()

        if input1 == '':
            input1 = '3'
        if input2 == '':
            input2 = '124 88 190'
        if input3 == '':
            input3 = '3.4 2.1 4'
        self.M = int(input1)
        temp = ''
        for i in input2:
            if i != ' ':
                temp += i
            else:
                self.D.append(float(temp))
                temp = ''
        self.D.append(float(temp))
        temp = ''
        for i in input3:
            if i != ' ':
                temp += i
            else:
                self.T.append(float(temp))
                temp = ''
        self.T.append(float(temp))

        print(self.M)
        print(self.D)
        print(self.T)

        self.cal()


    
root = tk.Tk(className='Python Examples - Window Size')
root.geometry("600x400")
root.fullScreenState = False
app = Application(master=root)



app.mainloop()