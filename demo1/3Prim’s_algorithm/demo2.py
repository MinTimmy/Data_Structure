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
       
    def Prim_Algorithm(self):
        selected = []
        for i in range(self.V):
            selected.append(0)
        # set number of edge to 0
        no_edge = 0
        # the number of egde in minimum spanning tree will be
        # always less than(V - 1), where V is number of vertices in
        # graph
        # choose 0th vertex and make it true
        selected[0] = True
        # print for edge and weight
        print("Edge : Weight\n")
        while (no_edge < self.V - 1):
            # For every vertex in the set S, find the all adjacent vertices
            #, calculate the distance from the vertex selected at step 1.
            # if the vertex is already in the set S, discard it otherwise
            # choose another vertex nearest to selected vertex  at step 1.
            minimum = sys.maxsize
            x = 0
            y = 0
            for i in range(self.V):
                if selected[i]:
                    for j in range(self.V):
                        if ((not selected[j]) and self.G[i][j]):  
                            # not in selected and there is an edge
                            if minimum > self.G[i][j]:
                                minimum = self.G[i][j]
                                x = i
                                y = j
            print(str(x) + "-" + str(y) + ":" + str(self.G[x][y]))
            self.answer_node[0].append(min(x,y))
            self.answer_node[1].append(max(x,y))
            self.answer_cost.append(self.G[x][y])
            selected[y] = True
            no_edge += 1
            self.draw_graph()
        # self.draw_graph()
        

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
                        if i == self.answer_node[0][k] and j == self.answer_node[1][k]:
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
        self.master = tk.Tk(className="Prim_Algorithm - " + str(len(self.answer_node[0]) + 1))
        self.master.geometry("600x400")
        
 
    def saveData(self): 
        tmp = []
        tmp.append(self.entry1.get())
        tmp.append(self.entry2.get())
        # create a 2d array of size 5x5
        # for adjacency matrix to represent graph
        if tmp[0] == "" or tmp[1] == "":
            # self.G = [
            #     [0, 1, 0, 0, 0],
            #     [1, 0, 2, 6, 0],
            #     [0, 2, 0, 3, 0],
            #     [0, 6, 3, 0, 6],
            #     [0, 0, 0, 6, 0]]
            # self.V = 5
            tmp[0] = "ABCDE"
            tmp[1] = "(B,A,1)(B,C,2)(C,D,3)(D,B,6)(D,E,6)"
        
        self.V = len(tmp[0])
        for i in tmp[0]:
            self.items.append(i)
        
        t = [[],[],[]]
        for i in range(len(tmp[1])):
            if i % 7 == 1:
                j = 0
                while tmp[1][i] != self.items[j]:
                    j += 1
                t[0].append(j)
            elif i % 7 == 3:
                j = 0
                while tmp[1][i] != self.items[j]:
                    j += 1
                t[1].append(j)
            elif i % 7 == 5:
                t[2].append(int(tmp[1][i]))


        for i in range(self.V):
            tt = []
            for j in range(self.V):
                tt.append(0)
            self.G.append(tt)
        
        for i in range(len(t[0])):
            self.G[t[0][i]][t[1][i]] = t[2][i]
            self.G[t[1][i]][t[0][i]] = t[2][i]
                


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
        
        self.draw_graph()
        self.Prim_Algorithm()
    def create_scrollingbar(self):
        self.main_frame = tk.Frame(self)

        self.main_frame.pack(fill=BOTH, expand=1)

        self.my_canvas = tk.Canvas(self.main_frame)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.my_scrollbar = tk.Scrollbar(self.main_frame, orient=VERTICAL, command=self.my_canvas.yview)
        self.my_scrollbar.pack(side=RIGHT, fill=Y)

        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))
root = tk.Tk(className='Prim_Algorithm - 0')
root.geometry("600x400")
root.fullScreenState = False
app = Application(master=root)



app.mainloop()