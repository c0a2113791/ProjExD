import tkinter as tk
import tkinter.messagebox as tkm

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
        #tkm.showinfo("", f"{i}ボタンが押されました")
        #6
        entry.insert(tk.END, i)
#1
root = tk.Tk()
root.geometry("300x500")
#4
entry = tk.Entry(root, justify="right", width=10,font=("",40))
entry.grid(row=0, column= 0,columnspan=3)
#2
r,c = 1,0
for i in range(9,-1,-1):
    button = tk.Button(root, text=f"{i}",width=4,height=2,font=(" ",30))
    button.grid(row=r,column=c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 == 0:
        r += 1 
        c = 0

op = ["+","="]
for ope in op:
    button = tk.Button(root, text=f"{ope}",width=4,height=2,font=(" ",30))
    button.grid(row=r ,column=c)
    button.bind("<1>",button_click)
    c += 1
    if c%3 == 0:
        r += 1 
        c = 0


root.mainloop()

