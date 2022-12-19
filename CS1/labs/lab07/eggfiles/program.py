def sierpinski(chart_1, lowleft, top, lowright, level,maxlevel):
    if level == maxlevel:
        return
    else:
        chart_1.create_polygon([lowleft, top, lowright], fill="white")
        leftmid = (lowleft[0]+top[0])/2,(lowleft[1]+top[1])/2
        rightmid = (lowright[0]+top[0])/2,(lowright[1]+top[1])/2
        bottommid = (lowright[0]+lowleft[0])/2,(lowright[1]+lowleft[1])/2
        chart_1.create_polygon([leftmid, rightmid, bottommid], fill="red")
        level += 1
        chart_1.update()
        sierpinski(chart_1, lowleft, leftmid, bottommid, level,maxlevel)
        sierpinski(chart_1, leftmid, top, rightmid, level,maxlevel)
        sierpinski(chart_1, bottommid, rightmid, lowright, level,maxlevel)
def restart(chart):
    chart_1.delete(tk.ALL)
    sierpinski(chart, (0,600), (300,600-300*math.sqrt(3)), (600,600),0,maxlevel[0])
    maxlevel[0] += 1

import tkinter as tk, math
root = tk.Tk()
root.title("Test")
chart_1 = tk.Canvas(root, width=600, height=600, background="white")
chart_1.grid(row=0, column=0)
maxlevel = [5]
restart(chart_1)
root.frame = tk.Frame(root)
root.frame.button = tk.Button(root.frame, text="push me", command=lambda:root.destroy())
root.frame.button2 = tk.Button(root.frame, text="don't push me", command=lambda:restart(chart_1))
root.frame.button.grid()
root.frame.button2.grid()
root.frame.grid()
root.mainloop()
