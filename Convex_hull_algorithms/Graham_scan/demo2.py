import subprocess
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        r = tk.Tk()
        self.canvas = tk.Canvas(r)
        self.create_entry_and_button()
        self.origin_points = []
        self.answer_points = []
        r.mainloop()

    def create_entry_and_button(self):
        self.label1 = tk.Label(self.master, text="Node")
        self.label1.place(x = 10, y = 10)
        self.entry1 = tk.Entry(self.master, )
        self.entry1.place(x = 100, y = 10)

        tk.Button(self.master, text="Submit", command=self.saveData).place(x = 300, y = 10)

    def create_point(self, point, radius):
        x0 = point[0] - radius + self.start_x
        y0 = point[1] - radius + self.start_y
        x1 = point[0] + radius + self.start_x
        y1 = point[1] + radius + self.start_y
        print(x0)
        # self.canvas.create_oval(x0,y0,x1,y1)
        self.canvas.create_oval(10.0,10.0,20.0,20.0)

    def draw(self):
        self.start_x = 20
        self.start_y = 20
        self.point_radius = 5

        for i in self.origin_points:
            self.create_point(i, self.point_radius)
    def saveData(self):
        f1 = open("input1", "r")
        for i in f1:
            a = 0
            b = 0
            temp = ""
            check = 1
            for j in i:
                if j == ' ' or j == '\n':
                    if check:
                        a = int(temp)
                        check = 0
                        temp = ""
                    else:
                        b = int(temp)
                else:
                    temp += j
            self.origin_points.append([a,b]) 

        subprocess.call("./demo2 < input1 > output1", shell=True)  
        f2 = open("output1", "r")
        for i in f2:
            a = 0
            b = 0
            temp = ""
            check = 1
            for j in i:
                if j == ' ' or j == '\n':
                    if check:
                        a = int(temp)
                        check = 0
                        temp = ""
                    else:
                        b = int(temp)
                else:
                    temp += j
            self.answer_points.append([a,b])
        
        self.draw()
                    

root = tk.Tk(className="Grahma_scan - 0")
root.geometry("600x400")
app = Application(master=root)



app.mainloop()


