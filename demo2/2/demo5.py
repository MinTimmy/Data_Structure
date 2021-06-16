import tkinter as tk
import sys
from tkinter.constants import Y

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.vertices = []
        self.edges = []
        self.pack()
        self.items = []
        self.N = 0 #number of item
        self.MAX = 9999
        self.visited_and_distance = [[0, 0]]
        self.create_entry_and_button()

    def create_entry_and_button(self):
        self.label1 = tk.Label(self.master, text="出發點：")
        self.label1.place(x=10, y=10)
        self.entry1 = tk.Entry(self.master)
        self.entry1.place(x=90,y=10)

        self.label2 = tk.Label(self.master, text="路徑：")
        self.label2.place(x=10, y=30)
        self.entry2 = tk.Entry(self.master)
        self.entry2.place(x=90,y=30)
        
        tk.Button(self.master, text='Submit', command=self.saveData).place(x = 270, y = 10)

    def to_be_visited(self):
        # global visited_and_distance
        v = -10
        # Choosing the vertex with the minimum distance
        for index in range(self.N):
            if self.visited_and_distance[index][0] == 0 and (v < 0 or self.visited_and_distance[index][1] <= self.visited_and_distance[v][1]):
                v = index
        # print(self.items[v])
        return v

    
    def Dijkstra_algorithm(self):
        self.previous_node = [0]
        self.create_entry_and_button()
        self.pass_by = []
        self.new_distance = 0
        for i in range(self.N-1):
            self.visited_and_distance.append([0, self.MAX])
            self.previous_node.append(0)
            self.pass_by.append(0)

        for vertex in range(self.N):
        # Finding the next vertex to be visited.
            to_visit = self.to_be_visited()
            for neighbor_index in range(self.N):
                # Calculating the new distance for all unvisited neighbors
                # of the chosen vertex.
                if self.vertices[to_visit][neighbor_index] == 1 and self.visited_and_distance[neighbor_index][0] == 0:
                    self.new_distance = self.visited_and_distance[to_visit][1] + self.edges[to_visit][neighbor_index]
                # Updating the distance of the neighbor if its current distance
                # is greater than the distance that has just been calculated
                    if self.visited_and_distance[neighbor_index][1] > self.new_distance:
                        self.visited_and_distance[neighbor_index][1] = self.new_distance
                        self.previous_node[neighbor_index] = to_visit
                        # self.pass_by[neighbor_index] = 
                # Visiting the vertex found earlier
                self.visited_and_distance[to_visit][0] = 1
            # print(self.visited_and_distance, "\n----------------------------")
            self.draw(vertex, to_visit)
        self.draw_final_answer()

        
    def draw_final_answer(self):
        master = tk.Tk(className="Dijkstra’s Algorithm - final_answer")
        master.geometry("600x400")
        init_point = [10,10]
        font_size = 50

        for i in range(self.N):
            
            string = self.items[i]
            j = i
            temp = self.previous_node[i]
            while self.previous_node[j] != 0:
                j = self.previous_node[j]
                string =  self.items[j] + "->" + string
            string = str(self.visited_and_distance[i][1]) + ": " + self.items[0] + "->" + string   
            label1 = tk.Label(master, text = string, font=("Arial", font_size))
            label1.place(x = init_point[0], y = init_point[1] + font_size * i * 2)

    def draw(self, index, choose):
        string = 'Initial'
        if index != 0:
            string = 'Including ' + self.items[choose]

        if index % 4 == 0:
            self.master = tk.Tk(className="Dijkstra’s Algorithm - " + str(int(index/4 + 1)))
            self.master.geometry("600x400")

        index %= 4
        initial_point = [10,10]
        box_scale = [80,50] #width and height
        
        label1 = tk.Label(self.master, text=string)
        label1.place(x = initial_point[0], y = initial_point[1] + box_scale[1] * (1 + index * 4) - 20)

        for i in range(self.N + 2):
            for j in range(self.N + 1):
                if j < 4:
                    canvas2 = tk.Canvas(self.master, width=box_scale[0] * (self.N + 1), height=1, background='black')
                    canvas2.place(x = initial_point[0], y = initial_point[1] + (index * 4 + j + 1) * box_scale[1])
                # canvas2.create_line(0,0,box_scale[0] * (self.N + 1), 1)
                if i == 0 and j == 1:
                    label2 = tk.Label(self.master, text=self.items[0])
                    label2.place(x = initial_point[0] + box_scale[0] / 2, y = initial_point[1] + (index * 4 + j + 1) * box_scale[1] + box_scale[1] / 2)
                if j == 0 and i >= 1 and i <= self.N:
                    label3 = tk.Label(self.master, text=self.items[i-1])
                    label3.place(x = initial_point[0] + i * box_scale[0] + box_scale[0] / 2, y = initial_point[1] + box_scale[1] * (1 + index * 4) + box_scale[1] / 2) 
                if j == 1 and i >= 1 and i <= self.N:
                    label4 = tk.Label(self.master, text=str(self.visited_and_distance[i-1][1]))
                    label4.place(x = initial_point[0] + i * box_scale[0] + box_scale[0] / 2, y = initial_point[1] + box_scale[1] * (2 + index * 4) + box_scale[1] / 2)
                if j == 2 and i >= 1 and i <= self.N:
                    label5 = tk.Label(self.master, text= self.items[self.previous_node[i-1]])
                    label5.place(x = initial_point[0] + i * box_scale[0] + box_scale[0] / 2, y = initial_point[1] + box_scale[1] * (3 + index * 4) + box_scale[1] / 2)
                if i == 0 and j == 2:
                    label6 = tk.Label(self.master, text="pass-by")
                    label6.place(x = initial_point[0] + box_scale[0] / 10, y = initial_point[1] + (index * 4 + j + 1) * box_scale[1] + box_scale[1] / 2)
            canvas1 = tk.Canvas(self.master, width=1, height = box_scale[1] * 3, background='black')
            canvas1.place(x = initial_point[0] + i * box_scale[0], y = initial_point[1] + box_scale[1] * (1 + index * 4))
            # canvas1.create_line(0,0,1,box_scale[1] * 2)

    def draw_origin_table(self):
        master = tk.Tk(className="Dijkstra’s Algorithm - origin_table")
        master.geometry("600x400")

        init_point = [10,10] # x,y
        box_scale = [50,50]#width and height

        for i in range(self.N):
            label2 = tk.Label(master, text=self.items[i])
            label2.place(x = init_point[0] + box_scale[0] * ( i + 1.5), y = init_point[1] + box_scale[1] * 0.5)
            label3 = tk.Label(master, text=self.items[i])
            label3.place(x = init_point[0] + box_scale[0] * 0.5, y = init_point[1] + box_scale[1] * ( i + 1.5))

            canvas1 = tk.Canvas(master, width=box_scale[0] * (self.N + 1), height=1, background='black')
            canvas1.place(x=init_point[0], y = init_point[1] + box_scale[1] * (i +1 ))
            canvas2 = tk.Canvas(master, width=1,height = (self.N + 1 )*box_scale[1], background='black')
            canvas2.place(x = init_point[0] + box_scale[0] * (i+1),y = init_point[1])
            for j in range(self.N):
                label1 = tk.Label(master, text=str(self.edges[i][j]))
                label1.place(x = init_point[0] + box_scale[0] * (i + 1.2), y = init_point[1] + box_scale[1] * ( j + 1.2))
            



    def saveData(self): 
        i1 = self.entry1.get()
        i2 = self.entry2.get()
        if i1 == "":
            i1 = "A"
        if i2 == "":
            # i2 = "A B 7,B C 10"
            i2 = 'A B 4,A C 5,A D 2,A E 12,B C 3,B E 1,C D 1,C H 13,D F 11,E G 6,E H 9,F H 8'
        self.items = []

        self.items.append(i1)

        first = True
        temp = []
        n = ""
        i2 += ','
        for i in i2:
            if ord(i) >= 65 and ord(i) <= 90:
                same = False
                for j in range(len(self.items)):
                    if i == self.items[j]:
                        same = True
                if not same:
                    self.items.append(i)
                    self.items = [self.items[0]] + sorted(self.items[1:])
                for j in range(len(self.items)):
                    if first:
                        if i == self.items[j]:
                            temp.append([j,-1,-1])
                            first = False
                            break
                    else:
                        if i == self.items[j]:
                            temp[len(temp)-1][1] = j
                            first = True
                            break
            if ord(i) >= 48 and ord(i) <= 57:
                n += i
            elif i == ',':
                temp[len(temp)-1][2] = int(n)
                n = "" 
        self.N = len(self.items)
        self.vertices = [[0 for i in range(self.N)] for j in range(self.N)]
        self.edges = [[self.MAX for i in range(self.N)] for j in range(self.N)]
        for i in range(self.N):
            self.edges[i][i] = 0

        for i in range(len(temp)):
            self.vertices[temp[i][0]][temp[i][1]] = 1
            self.edges[temp[i][0]][temp[i][1]] = temp[i][2]
            self.vertices[temp[i][1]][temp[i][0]]= 1
            self.edges[temp[i][1]][temp[i][0]]= temp[i][2]
        
        self.draw_origin_table()
        self.Dijkstra_algorithm()

    
root = tk.Tk(className='Python Examples - Window Size')
root.geometry("600x400")
root.fullScreenState = False
app = Application(master=root)



app.mainloop()