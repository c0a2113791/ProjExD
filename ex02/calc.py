import tkinter as tk
import tkinter.messagebox as tkm
import math

#3
def button_click(event):
    btn = event.widget
    i = btn["text"]
    if i == "=":
        siki = entry.get()
        ans = eval(siki) #式の評価
        entry.delete(0, tk.END)#表示された文字の削除
        entry.insert(tk.END, ans)

    else:
        entry.insert(tk.END, i)

        #tkm.showinfo("", f"{i}ボタンが押されました")
        #6
def click_ac(event):
    entry.delete(0, tk.END)

def click_b(event):
    back = entry.get()
    entry.delete(len(back)-1,tk.END)

def click_sqrt(event):
    siki = entry.get()
    ans = math.sqrt(int(siki))
    entry.delete(0, tk.END)#表示された文字の削除
    entry.insert(tk.END, ans)



#1
root = tk.Tk()
root.geometry("400x600")
#4
entry = tk.Entry(root, justify="right", width=10,font=("",40))
entry.grid(row=0, column= 0,columnspan=3)
#2
r,c = 2,0
for i in range(7,10):
    button = tk.Button(root, text=f"{i}",width=4,height=2,font=(" ",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 == 0:
        r += 1 
        c = 0
for i in range(4,7):
    button = tk.Button(root, text=f"{i}",width=4,height=2,font=(" ",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 == 0:
        r += 1 
        c = 0
for i in range(1,4):
    button = tk.Button(root, text=f"{i}",width=4,height=2,font=(" ",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 == 0:
        r += 1 
        c = 0
op = ["0","00","=","+"]
for ope in op:
    button = tk.Button(root, text=f"{ope}",width=4,height=2,font=(" ",30))
    button.grid(row=r ,column=c)
    button.bind("<1>",button_click)
    c += 1
    if c%4 == 0:
        r += 1 
        c = 0

button_ac = tk.Button(root, text="AC",width=4,height=2,font=(" ",30))
button_ac.grid(row=1 ,column=2)
button_ac.bind("<1>",click_ac)

button_sub = tk.Button(root, text="-",width=4,height=2,font=(" ",30))
button_sub.grid(row=4 ,column=3)
button_sub.bind("<1>",button_click)

button_div = tk.Button(root, text="/",width=4,height=2,font=(" ",30))
button_div.grid(row=2 ,column=3)
button_div.bind("<1>",button_click)

button_mul = tk.Button(root, text="*",width=4,height=2,font=(" ",30))
button_mul.grid(row=3 ,column=3)
button_mul.bind("<1>",button_click)

button_back = tk.Button(root, text="B",width=4,height=2,font=(" ",30))
button_back.grid(row=1 ,column=0)
button_back.bind("<1>",click_b)

button_sq = tk.Button(root, text="√",width=4,height=2,font=(" ",30))
button_sq.grid(row=1 ,column=3)
button_sq.bind("<1>",click_sqrt)


root.mainloop()

