from tkinter import *
from Ball import *
import random

class BallDraw(object):
    def __init__ (self, parent):
  
        self.b = Ball(100,150,20,-15,7,"white")

        self.wait_time = 100 

        self.isstopped = False 

        self.maxx = 400 # canvas width, in pixels
        self.maxy = 400 # canvas height, in pixels

        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        self.top_frame = Frame(self.frame)
        self.top_frame.pack(side=TOP)
        self.canvas = Canvas(self.top_frame, background="white", \
                             width=self.maxx, height=self.maxy )
        self.canvas.pack()
        self.bottom_frame = Frame(self.frame)
        self.bottom_frame.pack(side=BOTTOM)
        self.restart = Button(self.bottom_frame, text="Restart", command=self.restart)
        self.restart.pack(side=LEFT)
        self.slow = Button(self.bottom_frame, text="Slower", command=self.slower)
        self.slow.pack(side=LEFT)
        self.fast = Button(self.bottom_frame, text="Faster", command=self.faster)
        self.fast.pack(side=LEFT)
        self.quit = Button(self.bottom_frame, text="Quit", command=self.quit)
        self.quit.pack(side=RIGHT)

    def faster(self):      
        if self.wait_time > 2:
            self.wait_time //= 2
            
    def slower(self):     
        self.wait_time *= 2
            
    def restart(self):
        self.isstopped = False
        self.ball.x,self.ball.y = 80,200
        self.animate()
        
    def quit(self):
        self.isstopped = True
        self.parent.destroy()
        
    def draw_ball(self):
        #  Remove all the previously-drawn balls
        self.canvas.delete("all")
        
        # Draw an oval on the canvas within the bounding box
        bounding_box = self.b.bounding_box()
        self.canvas.create_oval(bounding_box, fill=self.ball.c)
        self.canvas.update()      # Actually refresh the drawing on the canvas.

        # Pause execution.  This allows the eye to catch up
        self.canvas.after(self.wait_time)

    def animate(self):
        ##  Loop until the ball runs off the screen.        
        while True:
            # Move the ball  
           # for b in self.ballist:
            self.draw_ball()
            self.ball.move()
            self.ball.checkandreverse(self.maxx,self.maxy)
            
            
if __name__ == "__main__":
    ##  We will create a root object, which will contain all 
    ##  our user interface elements
    ##
    root = Tk()
    root.title("Tkinter: Lab 11")
    colorList = ["blue", "red", "green", "yellow", "magenta", "orange"]
    maxx = 400
    maxy = 400
    wait_time = 90
    chart1 = Canvas(root, width = maxx, height = maxy, background = "white")
    chart1.grid(row = 0, column = 0)
    chart1.pack()
    balllist = []
    ## Create a class to handle all our animation
    bd = BallDraw(root)
    for i in range(0,10):
        ball = Ball(random.randint(10,390),random.randint(10,390),random.randint(-8,8),random.randint(-8,8), random.randint(5,10),random.choice(colorList))
        balllist.append(ball)
    while True:
        chart1.delete(ALL)
        for i in range(0,10):
            bounding_box = balllist[i].bounding_box()
            chart1.create_oval(bounding_box, fill = balllist[i].get_color())
        chart1.update()
        chart1.after(wait_time)     
        for j in range(0,10):
            balllist[j].move()
            balllist[j].check_and_reverse(maxx,maxy)
    ## Run the animation by continuously drawing the ball and then moving it
   # bd.animate()

    ## This is an infinite loop that allows the window to listen to
    ## "events", which are user inputs.  The only user event here is
    ## closing the window, which ends the program. 
    root.mainloop()


    
