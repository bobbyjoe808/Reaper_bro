import tkinter as tk
import time
import random
import os

### main variables 
height = 120
width = 120
pos = -(width / 4)
_speed = 7


root = tk.Tk()
screen_height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width, height, pos, screen_height - height - 25))
#root.title('Reaper')

#path = (os.path.dirname( os.path.realpath(__file__)) +'\iteam_tags.txt')


# create list with each frame of animation #
reaper_l_1 = []
for num in range(0, 8):
    reaper0 = tk.PhotoImage(file=os.path.dirname( os.path.realpath(__file__))+"\PassiveRunningReaper2.gif", format=f"gif -index {num}")
    reaper = reaper0.subsample(4, 4)
    reaper_l_1.append(reaper)

reaper_l_1f = []
for num in range(0, 8):
    reaper0 = tk.PhotoImage(file=os.path.dirname( os.path.realpath(__file__))+"\PassiveRunningReaper2f.gif", format=f"gif -index {num}")
    reaper = reaper0.subsample(4, 4)
    reaper_l_1f.append(reaper)

reaper_l_2 = []
for num in range(0, 5):
    reaper0 = tk.PhotoImage(file=os.path.dirname(os.path.realpath(__file__))+"\PassiveIdleReaper2.gif", format=f"gif -index {num}")
    reaper = reaper0.subsample(4, 4)
    reaper_l_2.append(reaper)

reaper_l_2f = []
for num in range(0, 5):
    reaper0 = tk.PhotoImage(file=os.path.dirname( os.path.realpath(__file__)) +"\PassiveIdleReaper2f.gif", format=f"gif -index {num}")
    reaper = reaper0.subsample(4, 4)
    reaper_l_2f.append(reaper)

reaper_l_3 = []
for num in range(0, 8):
    reaper0 = tk.PhotoImage(file=os.path.dirname( os.path.realpath(__file__)) +"\HostileRunningReaper2.gif", format=f"gif -index {num}")
    reaper = reaper0.subsample(4, 4)
    reaper_l_3.append(reaper)

reaper_l_3f = []
for num in range(0, 8):
    reaper0 = tk.PhotoImage(file=os.path.dirname( os.path.realpath(__file__)) +"\HostileRunningReaper2f.gif", format=f"gif -index {num}")
    reaper = reaper0.subsample(4, 4)
    reaper_l_3f.append(reaper)
###


class start():

    def __init__(self, current_image):
        self.current_image = current_image
        self.anim = None
        self.speed =  -_speed
        self.activity = 'walk'
        self.x = root.winfo_screenwidth()



    def animation(self, count, pos, flip=True):

        # list activies of ghost
        activities = ['walk', 'walk', 'walk', 'stop', 'follow']
      
        if random.randint(0,70) == 70 and self.activity != 'stop':
            self.activity = random.choice(activities)
        
        if random.randint(0,20) == 20 and self.activity == 'stop':
            self.activity = random.choice(activities)


        if self.activity == 'walk':
    
            if self.x == 0:
                if pos - _speed == 0:
                    self.x = root.winfo_screenwidth()

            else:
                self.x = root.winfo_screenwidth()
            if self.x == root.winfo_screenwidth():
                if pos  == root.winfo_screenwidth()-3:
                    self.x = 0
            

        if self.activity == 'stop':
            self.x = pos

        if self.activity == 'follow':
            self.x = (root.winfo_pointerx() - 60)
   
        next_frame = self.current_image[count]
        label.config(image=next_frame)
        count += 1

        if pos + _speed < self.x:

            self.speed = _speed

            flip = True
            if self.current_image == reaper_l_3f:
                print('4')
                self.current_image = reaper_l_3
            if self.current_image == reaper_l_1f or self.current_image == reaper_l_2f:
                self.current_image = reaper_l_1

        if pos - _speed > self.x:
            self.speed = -_speed
            flip = False
            if self.current_image == reaper_l_3:
                self.current_image = reaper_l_3f
            if self.current_image == reaper_l_1 or self.current_image == reaper_l_2:
                self.current_image = reaper_l_1f

        if pos - _speed <= self.x <= pos + _speed:
            if flip:
                self.current_image = reaper_l_2
            else:
                self.current_image = reaper_l_2f
            self.speed = 0


        pos += self.speed

        # size of ghost
        root.geometry('%dx%d+%d+%d' % (width, height, pos, 719))
        if count >= len(self.current_image):
            count = 0

        ## main loop ##
        self.anim = root.after(100, lambda: start.animation(count, pos,flip))

    

label = tk.Label(root, bd=0, bg='#0400FF')

button = tk.Button(root, bg='#0400FF')

label.place(relx=2, rely=1)

# remove background#
label = tk.Label(root, bd=0, bg='#0400FF')
root.config(highlightbackground='#0400FF')
root.wm_attributes('-transparentcolor', '#0400FF')
root.overrideredirect(True)

# add image #sw

label.pack()

start = start(reaper_l_2)
start.animation(count=0, pos=0)

root.mainloop()
