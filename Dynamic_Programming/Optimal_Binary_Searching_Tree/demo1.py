import collections
import tkinter as tk
from tkinter.constants import BOTH, LEFT, N, RIGHT, VERTICAL, Y
from typing import Collection, Sized
import sys
class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1

class Tree(object):
    def insert(self, root, key): 
      
        # Step 1 - Perform normal BST 
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.freq= []
        self.cost = []
        self.best = []
        self.items = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
        self.answer = []
        self.N = 0 #number of item
        self.create_entry_and_button()
        self.treeHeight = 0
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
       
    def Optimal_Binary_Searching_Tree(self):
        temp = 0
        for j in range(1,self.N):
            for i in range(0,self.N-j):
                for k in range(i, i+j+1):
                    if k - 1 < 0:
                        temp = 0 + self.cost[k+1][i+j]
                    elif k+1 >= self.N:
                        temp = self.cost[i][k-1] + 0
                    else:
                        # print(i , k - 1, self.cost[i][k-1] , self.cost[k+1][i+j])
                        temp = self.cost[i][k-1] + self.cost[k+1][i+j]
                    if temp < self.cost[i][i+j]:
                        self.cost[i][i+j] = temp
                        self.best[i][i+j] = k
                temp = 0
                for k in range(i, i+j+1):
                    temp += self.freq[k]
                self.cost[i][i+j] = self.cost[i][i+j] + temp
        
        self.printTable()        
        self.root = TreeNode(self.best[0][self.N-1])
        self.makeTree(self.root, 0, self.N-1)
        self.nodeX = 1300
        self.nodeY = 10
        self.printAnswer(self.root, 1300, 10)

    def printTable(self):
        self.table_square = 60
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

        # for j in range(self.N):
        #     print(self.best[j])

        for r in range(self.N):
            for c in range(self.N):
                if self.cost[r][c] == 0:
                    string = "?"
                elif r == c:
                    string = str(self.cost[r][c])
                else:
                    string += self.items[self.best[r][c]] + str(self.cost[r][c])
                # label1 = tk.Label(self.master, text=string).grid(row=r*2+1,column=c+1)
                label1 = tk.Label(self.master, text=string).place(x=30+(c+1.5)*(self.table_square),y=30+(r+1.5)*(self.table_square))
                string = ""
            # canvas.grid(row=r*2+1)
        print('\n')

    def printAnswer(self, root, nodeX, nodeY):
        self.nodeToNode = 20
        print(root.val)
        label1 = tk.Label(self.master, text=self.items[root.val]).place(x = nodeX, y = nodeY)
       

        if root.left != None:
            canvas1 = tk.Canvas(self.master,width=(self.treeHeight - root.height) * self.nodeToNode,height=(self.treeHeight - root.height) * self.nodeToNode)
            canvas1.create_line(0, (self.treeHeight - root.height) * self.nodeToNode,(self.treeHeight - root.height) * self.nodeToNode,0)
            canvas1.place(x = nodeX - (self.treeHeight - root.height) * self.nodeToNode +5, y = nodeY + 15)
            self.printAnswer(root.left, nodeX - (self.treeHeight - root.height) * self.nodeToNode, nodeY + (self.treeHeight - root.height) * self.nodeToNode )
        if root.right != None:
            canvas1 = tk.Canvas(self.master,width=(self.treeHeight - root.height) * self.nodeToNode,height=(self.treeHeight - root.height) * self.nodeToNode)
            canvas1.create_line(0, 0,(self.treeHeight - root.height) * self.nodeToNode,(self.treeHeight - root.height) * self.nodeToNode-13)
            canvas1.place(x = nodeX+5, y = nodeY +15)
            self.printAnswer(root.right, nodeX + (self.treeHeight - root.height) * self.nodeToNode, nodeY + (self.treeHeight - root.height) * self.nodeToNode)
            # self.root.left
            




    def makeTree(self, root, left, right):
        # print(left, self.best[left][right]-1)
        root.left = TreeNode(self.best[left][self.best[left][right]-1])
        root.right = TreeNode(self.best[self.best[left][right]+1][right])
        root.left.height = root.height + 1
        root.right.height = root.height + 1

        if self.treeHeight < root.height + 1:
            self.treeHeight = root.height + 1
        
        if left < self.best[left][right] - 1:
            self.makeTree(root.left, left, self.best[left][right] - 1)
        if right > self.best[left][right] + 1:
            self.makeTree(root.right, self.best[left][right]+1,right)




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
            tmp = "4,2,1,3,5,2,1"
        self.N = 0
        self.cost = []
        self.best = []
        self.freq = []
        str = ""
        for i in tmp:
            if i != ',':
                str+= i
            else:
                self.freq.append(int(str))
                str = ""
        self.freq.append(int(str))
        self.N = len(self.freq)

        
        for i in range(self.N):
            temp = []
            t = []
            for j in range(self.N):
                if i == j:
                    temp.append(self.freq[i])
                elif i > j:
                    temp.append(0)
                else:
                    temp.append(sys.maxsize)
                t.append(-1)
            self.best.append(t)
            self.cost.append(temp)

        # print(self.freq)
        # for i in range(self.N):
        #     print(self.best[i])

        self.Optimal_Binary_Searching_Tree()

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