import collections
import tkinter as tk
from tkinter.constants import BOTH, LEFT, N, RIGHT, VERTICAL, Y
from typing import Collection, Sized
import sys

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.a = [[]]
        self.p = []
        self.items = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.INF = 1000000000
        self.N = 0

        self.create_entry_and_button()

    def create_entry_and_button(self):
        self.label1 = tk.Label(self.master, text="a")
        self.label1.place(x=10, y=10)
        self.entry1 = tk.Entry(self.master)
        self.entry1.place(x=70,y=10)
        
        self.label2 = tk.Label(self.master, text="p")
        self.label2.place(x=10, y=40)
        self.entry2 = tk.Entry(self.master)
        self.entry2.place(x=70,y=40) 
        tk.Button(self.master, text='Submit', command=self.saveData).place(x = 250, y = 10)
    def Flogd_Warshall_Algorithm(self):
        for j in range(self.N):
            for i in range(self.N):
                for k in range(self.N):
                    if (i != j) and (j != k):
                        if self.a[i][k] > self.a[i][j] + self.a[j][k]:
                            self.a[i][k] = self.a[i][j] + self.a[j][k]
                            self.p[i][k] = self.p[i][j]
            self.showTable(j)

    def showTable(self, count):
        self.table_square_width = 40
        self.table_square_height = 40
        self.table_start_x = 10 + count * (self.N * self.table_square_width + 200)
        self.table_start_y = 90

        for i in range(self.N):
            labelX = tk.Label(self.master, text = self.items[i]).place(x = self.table_start_x + self.table_square_width * (i + 1 + 0.5), y = self.table_start_y + self.table_square_height * 0.5)
            labelY = tk.Label(self.master, text = self.items[i]).place(x = self.table_start_x + self.table_square_width * 0.5, y = self.table_start_y + self.table_square_height * ( i + 1 + 0.5))
            canvasX = tk.Canvas(self.master, width= self.table_square_width * (self.N + 1), height = 1)
            canvasX.create_line(0,1,self.table_square_width * (self.N + 1), 1)
            canvasX.place(x = self.table_start_x, y = self.table_start_y + self.table_square_height * (i + 1) )
            canvasY = tk.Canvas(self.master, width = 1, height = self.table_square_height * (self.N + 1) )
            canvasY.create_line(1,0,1,self.table_square_height * (self.N + 1))
            canvasY.place(x = self.table_start_x + self.table_square_width * (i + 1), y = self.table_start_y)
            for j in range(self.N):
                string = ""
                if self.a[i][j] == self.INF:
                    string = "I"
                else:
                    string = str(self.a[i][j])
                label1 = tk.Label(self.master, text = self.items[self.p[i][j]] + string).place(x = self.table_start_x + self.table_square_width * (1 + j) + 3, y = self.table_start_y + self.table_square_height * (1 + i) + 3)

    def saveData(self):
        self.a = [
            [0,1,self.INF,self.INF,4],
            [1,0,5,1,self.INF],
            [self.INF, 5,0,2,self.INF],
            [self.INF, 1,2,0,1],
            [4,self.INF,self.INF,1,0]
        ]
        self.p = [
            [0,1,2,3,4],
            [0,1,2,3,4],
            [0,1,2,3,4],
            [0,1,2,3,4],
            [0,1,2,3,4]
        ]
        self.N = len(self.p[0])
        self.Flogd_Warshall_Algorithm()

root = tk.Tk(className='Optimal_Binary_Searching_Tree - 1')
root.geometry("600x400")
root.fullScreenState = False
app = Application(master=root)



app.mainloop()