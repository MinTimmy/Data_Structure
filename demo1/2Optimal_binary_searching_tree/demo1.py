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
        self.ITEMS = ["Salmon", "Tuna", "Istiophoridae", "Fenneropenaeus", "Borealis", "Adductor", "Haliotis", "Gratilla", "Kuroge", "Chionoecetes", "Eriocheir", "Palinuridae"]
        self.ABBREVIATION = "STIFBAHGKCEP"
        self.items = [] # it stores integer 
        self.answer = []
        self.N = 0 #number of item
        self.create_entry_and_button()
        self.treeHeight = 0
        
        # self.printTable()
        # self.printAnswer()

    def create_entry_and_button(self):
        self.label1 = tk.Label(self.master, text="食材代號:")
        self.label1.place(x=10, y=10)
        self.entry1 = tk.Entry(self.master)
        self.entry1.place(x=70,y=10)
        
        self.label2 = tk.Label(self.master, text="吃的貫數:")
        self.label2.place(x=10, y=40)
        self.entry2 = tk.Entry(self.master)
        self.entry2.place(x=70,y=40)
        tk.Button(self.master, text='Submit', command=self.saveData).place(x = 250, y = 10)
       
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
        self.create_newWindow()
        self.root = TreeNode(self.best[0][self.N-1])
        self.makeTree(self.root, 0, self.N-1)
        self.nodeX = 500
        self.nodeY = 10
        self.printAnswer(self.root, self.nodeX, self.nodeY)
    def printTable(self):
        self.table_square_weight = []
        self.table_square_height = 30
        self.table_start_x = 10
        self.table_start_y = 70
        self.wordPixel = 10
        for i in range(self.N):
            self.table_square_weight.append(len(self.ITEMS[self.items[i]]))
        count = 0
        for i in range(self.N):
            count2 = 0
            for j in range(self.N):
                string1 = ""
                if i < j:
                    string1 += str(self.cost[i][j]) + self.ABBREVIATION[self.items[self.best[i][j]]]
                elif i == j:
                    string1 += str(self.cost[i][j]) + self.ABBREVIATION[self.items[i]]
                else:
                    string1 = ""
                if string1 != "":
                    label3 = tk.Label(self.master, text=string1).place(x = self.table_start_x + (max(self.table_square_weight) + count2) * self.wordPixel, y = self.table_start_y + (i + 1) * self.table_square_height)
                count2 += self.table_square_weight[j]
            label1 = tk.Label(self.master, text=self.ITEMS[self.items[i]]).place(x = self.table_start_x + (max(self.table_square_weight) + count) *self.wordPixel, y = self.table_start_y)
            label2 = tk.Label(self.master, text=self.ITEMS[self.items[i]]).place(x = self.table_start_x, y = self.table_start_y + (i + 1) * self.table_square_height )
            canvas1 = tk.Canvas(self.master,width= (sum(self.table_square_weight) + max(self.table_square_weight)) * self.wordPixel,height=1)
            canvas1.create_line(0,1,(sum(self.table_square_weight) + max(self.table_square_weight))* self.wordPixel, 1)
            canvas1.place(x=self.table_start_x, y = self.table_start_y + (i + 1) * self.table_square_height )
            canvas2 = tk.Canvas(self.master, width=1, height=(self.N + 1) * self.table_square_height)
            canvas2.create_line(1,0,1,(self.N + 1) * self.table_square_height)
            canvas2.place(x = self.table_start_x + (count + max(self.table_square_weight) )* self.wordPixel, y = self.table_start_y)
            count += self.table_square_weight[i]
    

    def printAnswer(self, root, nodeX, nodeY):
        print("tree height: ",self.treeHeight)
        self.node_height = 18
        self.node_weight = 110
        self.nodeToNode_height = 45
        self.nodeToNode_width = 150
        self.wordPixel = 3
        print(root.val)
        label1 = tk.Label(self.master, text=self.ITEMS[self.items[root.val]], width=16, height=1, bg='blue').place(x = nodeX, y = nodeY)
        # canvas3 = tk.Canvas(self.master, bg='red',width=143, height=1)
        # canvas3.create_line(1,0,0,1300)
        # canvas3.place(x = nodeX, y = nodeY + 18)

        if root.left != None and root.left.val != -1:
            canvas1 = tk.Canvas(self.master, bg = 'red', width=(self.treeHeight - root.height) * 18 ,height=(self.treeHeight - root.height) * 18 - self.node_height * self.wordPixel)
            canvas1.create_line(0, (self.treeHeight - root.height) * self.nodeToNode_height,(self.treeHeight - root.height) * self.nodeToNode_width,0)
            canvas1.place(x = nodeX - (self.treeHeight - root.height) * self.nodeToNode_width + (self.node_weight / 2) * self.wordPixel, y = nodeY + (self.node_height + 1) * self.wordPixel)
            print("left")
            self.printAnswer(root.left, nodeX - (self.treeHeight - root.height) * self.nodeToNode_width, nodeY + (self.treeHeight - root.height) * self.nodeToNode_height )
        
        if root.right != None and root.right.val != -1:
            canvas2 = tk.Canvas(self.master, width=(self.treeHeight - root.height) * self.nodeToNode_width,height=(self.treeHeight - root.height) * self.nodeToNode_height)
            canvas2.create_line(0, 0,(self.treeHeight - root.height) * self.nodeToNode_width,(self.treeHeight - root.height) * self.nodeToNode_height-13)
            canvas2.place(x = nodeX + (self.treeHeight - root.height) * self.nodeToNode_width - (self.node_weight / 2) * self.wordPixel, y = nodeY + (self.node_height + 1) * self.wordPixel)
            print("right")
            self.printAnswer(root.right, nodeX + (self.treeHeight - root.height) * self.nodeToNode_width, nodeY + (self.treeHeight - root.height) * self.nodeToNode_height)
            # self.root.left
            




    def makeTree(self, root, left, right):
        # print(left, self.best[left][right]-1)
        # print(left, right)
        if self.best[left][right] - 1 >= 0:
            root.left = TreeNode(self.best[left][self.best[left][right]-1])
            root.left.height = root.height + 1
        if self.best[left][right] + 1 < self.N:
            root.right = TreeNode(self.best[self.best[left][right]+1][right])
            root.right.height = root.height + 1

        if self.treeHeight < root.height + 1:
            self.treeHeight = root.height + 1
        
        if left < self.best[left][right] - 1:
            self.makeTree(root.left, left, self.best[left][right] - 1)
        if right > self.best[left][right] + 1:
            self.makeTree(root.right, self.best[left][right]+1,right)

    def create_newWindow(self):
        self.master = tk.Tk(className="Optimal_Binary_Searching_Tree - 2")
        self.master.geometry("600x400")

    def saveData(self): 
        tmp = []
        tmp.append(self.entry1.get())
        tmp.append(self.entry2.get())

        if tmp[0] == "" or tmp[1] == "":
            tmp[0] = "SIFAP"
            tmp[1] = "41,26,18,13,55"
        # tmp[0] = "STIFBAHGKCEP"
        # tmp[1] = "21,32,43,32,45,56,67,87,45,34,23,54"
        self.N = 0
        self.cost = []
        self.best = []
        self.freq = []
        for i in tmp[0]:
            for j in range(len(self.ABBREVIATION)):
                if i == self.ABBREVIATION[j]:
                    self.items.append(j)
                    break
        string1 = ""
        for i in tmp[1]:
            if i != ',':
                string1+= i
            else:
                self.freq.append(int(string1))
                string1 = ""
        self.freq.append(int(string1))
        self.N = len(self.freq)

        # for i in range(self.N):
        #     print(self.ITEMS[self.items[i]])
        #     print(self.freq[i])
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
        #     print(self.cost[i])

        self.Optimal_Binary_Searching_Tree()

root = tk.Tk(className='Optimal_Binary_Searching_Tree - 1')
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