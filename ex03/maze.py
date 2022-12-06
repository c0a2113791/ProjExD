import tkinter as tk
import maze_maker 
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = " "

def mm():
    global maze_lst , my , mx
    maze_lst = maze_maker.make_maze(25, 15)
    maze_maker.show_maze(Canvas, maze_lst)
    my = 1
    mx = 1
    cx, cy = mx*50+25, my*50+25
    Canvas.create_image(cx ,cy ,image = phot ,tag="koukaton")
    main_proc()
maze_lst = []



def main_proc():
    global mx ,my ,cx ,cy
    print(key)
    if key == "w":
        my -= 1

    if key == "s":
        my += 1
    
    if key == "a":
        mx -= 1

    if key == "d":
        mx += 1
    
    if key == "r":
        mx ,my = 1, 1
    if key== "R":
        mm()
        return
        

    #1マス移動する際に，移動先が壁なら移動させない
    if maze_lst[mx][my] ==1:
        if key == "w":
            my += 1

        if key == "s":
            my -= 1
        
        if key == "a":
            mx += 1

        if key == "d":
            mx -= 1
    
    cx, cy = mx*50+25, my*50+25
    Canvas.coords("koukaton" ,cx , cy)
    if mx == 23 and my == 13:
        tkm.showinfo("","ゴールしました")
        return 
    root.after(120, main_proc)
    print(mx,my)
    
def count_up():
    global tmr
    label["text"] = tmr
    tmr += 1
    root.after(1000, count_up)
        
if __name__ == "__main__":
    

    root = tk.Tk()
    root.title("迷えるこうかとん")
    Canvas = tk.Canvas(root, width=1250, height=750, bg= "black")
    Canvas.pack()

    label = tk.Label(root, text= "", font=("", 80))

    label.pack()

    maze_lst = maze_maker.make_maze(25, 15)
    maze_maker.show_maze(Canvas, maze_lst)

    tmr = 0

    phot = tk.PhotoImage(file="fig/8.png")
    mx ,my = 1 ,1
    cx, cy = mx*100+50, my*100+50
    Canvas.create_image(cx ,cy ,image = phot ,tag="koukaton")
    Canvas.pack()
     
    root.after(0,count_up)

    key = " "
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()

    root.mainloop()



    