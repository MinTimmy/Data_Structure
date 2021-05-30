import collections
import tkinter as tk
from tkinter.constants import BOTH, LEFT, N, RIGHT, VERTICAL, X, Y
from typing import Collection, Sized
import sys
import math

  
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.ITEMS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
        self.items = []
        self.create_entry_and_button()
        self.G = [] # for adjacency matrix to represent graph
        self.V = 0# number of vertices in graph
        self.answer_node = [[],[]]
        self.answer_cost = []
        self.graph = []

    def create_entry_and_button(self):
        self.label1 = tk.Label(self.master, text="店代號")
        self.label1.place(x=10, y=10)
        self.entry1 = tk.Entry(self.master)
        self.entry1.place(x=100,y=10)
        
        self.label2 = tk.Label(self.master, text="店相對位址")
        self.label2.place(x=10, y=40)
        self.entry2 = tk.Entry(self.master)
        self.entry2.place(x=100,y=40)
        tk.Button(self.master, text='Submit', command=self.saveData).place(x = 300, y = 10)
       
    def add_edge(self, u, v, w):
        self.graph.append([u, v ,w])
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    #  Applying Kruskal algorithm
    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                # result.append([u, v, w])
                self.answer_node[0].append(v)
                self.answer_node[1].append(u)
                self.answer_cost.append(w)
                # for i in range(len(self.answer_node[0])):
                #     print(self.answer_node[0][i], self.answer_node[1][i])
                self.apply_union(parent, rank, x, y)
                self.draw_graph()
        # for u, v, weight in result:
        #     print("%d - %d: %d" % (u, v, weight))
 
    def draw_graph(self):
        self.create_newWindow()
        angle = 360 / self.V
        edgeSize = 200
        A_site = [500, 300]

        node_X = []
        node_Y = []
        for i in range(self.V):
            node_X.append(A_site[0] + math.cos(math.radians(angle * i)) * edgeSize)
            node_Y.append(A_site[1] + math.sin(math.radians(angle * i)) * edgeSize)

        canvas1 = tk.Canvas(self.master,width=max(node_X)-min(node_X) + 10,height=max(node_Y) - min(node_Y) +10)
        canvas1.place(x = min(node_X) , y = min(node_Y)) 
        for i in range(self.V):
            for j in range(i, self.V):
                if self.G[i][j]:
                    next_node_X = A_site[0] + math.cos(math.radians(angle * j)) * edgeSize
                    next_node_Y = A_site[1] + math.sin(math.radians(angle * j)) * edgeSize

                    linePoint = [node_X[i] - min(node_X) , node_Y[i] - min(node_Y) , next_node_X - min(node_X) , next_node_Y - min(node_Y)]
                    is_draw = True
                    for k in range(len(self.answer_node[0])):
                        print(i,j)
                        if i == self.answer_node[0][k] and j == self.answer_node[1][k]:
                            print(i, j)
                            canvas1.create_line(linePoint[0], linePoint[1], linePoint[2], linePoint[3], fill = 'red', width = 5)
                            is_draw = False

                    if is_draw:
                        canvas1.create_line(linePoint[0], linePoint[1], linePoint[2], linePoint[3], width = 3)
                    label2 = tk.Label(self.master, text=str(self.G[i][j]))
                    label2.place(x = (abs(linePoint[0] + linePoint[2]) / 2) + min(node_X), y = (abs(linePoint[1] + linePoint[3]) / 2) + min(node_Y))
        for i in range(self.V):
            label1 = tk.Label(self.master, text=self.items[i], bg='green')
            label1.place(x = A_site[0] + math.cos(math.radians(angle * i)) * edgeSize, y = A_site[1]+ math.sin(math.radians(angle * i)) * edgeSize)                               

    def create_newWindow(self):
        self.master = tk.Tk(className="Kruskal_algorithm - " + str(len(self.answer_node[0]) + 1))
        self.master.geometry("600x400")
        
 
    def saveData(self): 
        tmp = []
        tmp.append(self.entry1.get())
        tmp.append(self.entry2.get())
        # other dataset
        # self.G = [
        #     [0, 9, 75, 0, 0,100],
        #     [9, 0, 95, 19, 42,0],
        #     [75, 95, 0, 51, 66,0],
        #     [0, 19, 51, 0, 31,0],
        #     [0, 42, 66, 31, 0,0],
        #     [100,0,0,0,0,0]]

        # self.V = 6
        # self.items = ['A', 'B', 'C', 'D', 'E', 'F']

        self.G = [
            [0,4,0,3,0,8],
            [4,0,0,0,7,9],
            [0,0,0,5,1,0],
            [3,0,5,0,2,0],
            [0,0,1,2,0,6],
            [8,9,0,0,6,0],
        ]
        self.V = len(self.G[0])
        self.items.clear()
        for i in range(len(self.G[0])):
            for j in range(len(self.G[0])):
                if i >= j and self.G[i][j]:
                    self.add_edge(i, j, self.G[i][j])
        self.items = ['A', 'B', 'C', 'D', 'E', 'F']
        
        self.draw_graph()
        self.kruskal_algo()
    def create_scrollingbar(self):
        self.main_frame = tk.Frame(self)

        self.main_frame.pack(fill=BOTH, expand=1)

        self.my_canvas = tk.Canvas(self.main_frame)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.my_scrollbar = tk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))
root = tk.Tk(className='Kruskal_algorithm - 0')
root.geometry("600x400")
root.fullScreenState = False
app = Application(master=root)



app.mainloop()