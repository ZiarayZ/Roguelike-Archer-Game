import pygame,random,math,sys,os
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
class Settings:
    def __init__(self,master):
        self.resolution=[(640,480),(800,600),(960,720),(1024,768),(1280,960),(1400,1050),(1440,1080),(1600,1200),(1856,1392),(1920,1440),(2048,1536)]
        self.master=master
        master.title("Initial Settings")
        master.geometry("125x250+"+str(int(master.winfo_screenwidth()/2-62.5))+"+"+str(int(master.winfo_screenheight()/2-87.5)))
        self.variable=tkinter.IntVar()
        self.variable.set(1)
        self.variable1=tkinter.StringVar(master)
        self.variable1.set("")
        self.variable2=tkinter.IntVar()
        self.variable2.set(10)
        tkinter.Label(master,text="VIDEO").grid(row=0,column=1,columnspan=2)
        tkinter.Radiobutton(master,variable=self.variable,value=3,command=self.assign).grid(row=1,column=1,sticky="E")
        tkinter.Radiobutton(master,variable=self.variable,value=2,command=self.assign).grid(row=2,column=1,sticky="E")
        tkinter.Radiobutton(master,variable=self.variable,value=1,command=self.assign).grid(row=3,column=1,sticky="E")
        tkinter.Label(master,text="16:10").grid(row=1,column=2,sticky="W")
        tkinter.Label(master,text="16:9").grid(row=2,column=2,sticky="W")
        tkinter.Label(master,text="4:3").grid(row=3,column=2,sticky="W")
        self.menu=tkinter.OptionMenu(master,self.variable1,*self.resolution)
        self.menu.grid(row=4,column=1,columnspan=2)
        tkinter.Label(master,text="AUDIO").grid(row=5,column=1,columnspan=2)
        tkinter.OptionMenu(master,self.variable2,0,1,2,3,4,5,6,7,8,9,10).grid(row=6,column=1,columnspan=2)
        tkinter.Label(master,text="TEMPORARY").grid(row=7,column=1,columnspan=2)
        self.text=tkinter.Entry(master)
        self.text.grid(row=8,column=1,columnspan=2)
        tkinter.Button(master,text="Continue",command=self.cont).grid(row=9,column=1,columnspan=2)
    def assign(self):
        if self.variable.get()==1:
            self.height=450
            self.width=600
            self.ratio="4x3"
            self.resolution=[(640,480),(800,600),(960,720),(1024,768),(1280,960),(1400,1050),(1440,1080),(1600,1200),(1856,1392),(1920,1440),(2048,1536)]
        elif self.variable.get()==2:
            self.height=450
            self.width=800
            self.ratio="16x9"
            self.resolution=[(1024,576),(1152,648),(1280,720),(1366,768),(1600,900),(1920,1080),(2560,1440),(3840,2160)]
        elif self.variable.get()==3:
            self.height=450
            self.width=720
            self.ratio="16x10"
            self.resolution=[(1280,800),(1440,900),(1680,1050),(1920,1200),(2560,1600)]
        options=self.menu["menu"]
        options.delete(0,"end")
        for string in self.resolution:
            options.add_command(label=string,command=lambda value=string: self.variable1.set(value))
    def cont(self):
        if self.variable1.get()!="":
            self.assign()
            self.message=self.text.get()
            self.master.destroy()
root=tkinter.Tk()
true_screen_width=root.winfo_screenwidth()
true_screen_height=root.winfo_screenheight()
my_gui=Settings(root)
root.mainloop()
volume=my_gui.variable2.get()/10
for char in my_gui.variable1.get():
    if char=="(":
        number=""
    if char==" ":
        screen_width=int(number)
        number=""
    if char==")":
        screen_height=int(number)
        del number
    try:
        int(char)
        number+=char
    except:
        pass
try:
    width=my_gui.width
    randomvalue=False
except:
    randomvalue=True
if randomvalue:
    sys.exit()
else:
    del randomvalue
height=my_gui.height
aspect_ratio=my_gui.ratio
message=my_gui.message
del my_gui,tkinter,root
class Player(object):
    def __init__(self):
        self.direction="r"
        self.arrowdirection="r"
        self.width=16
        self.height=44
        self.g=0
        self.shottime=0
        self.animtime=0
        self.deathtime=0
        self.time=0
        self.velocity=0
        self.angle=0
        self.onGround=False
        self.Rolling=False
        self.drawn=False
        self.death=False
        self.rect=pygame.Rect(500,(height-82),self.width,self.height)
        self.image=psr
        self.dimension=(4,0)
        self.start=(self.rect.x,self.rect.y)
        self.arrows=[]
        self.shots=[]
    def move(self,dx=0,dy=0):
        if dx!=0:
            self.rect.x+=dx
        if dx>0:
            self.animation("r")
        if dx<0:
            self.animation("l")
        if dy!=0:
            self.onGround=False
            self.rect.y+=dy
        for block in blocks:
            if self.rect.colliderect(block.rect):
                if dy>0:
                    if not self.Rolling:
                        self.rect=pygame.Rect(self.rect.x,self.rect.y-32,self.width,self.height)
                    self.rect.bottom=block.rect.top
                    self.g=0
                    self.onGround=True
                if dy<0:
                    self.rect.top=block.rect.bottom
                    self.g=0
                if dx>0:
                    self.rect.right=block.rect.left
                if dx<0:
                    self.rect.left=block.rect.right
                else:
                    pass
    def jump(self):
        self.onGround=False
        self.g=-5
        self.rect=pygame.Rect(self.rect.x,self.rect.y,self.width,self.height-16)
        self.jumped=True
    def animation(self,direction):
        if self.onGround:
            self.direction=direction
            if direction=="r":
                if gamertime-self.animtime>60:
                    self.animtime=gamertime
                    self.image=pm1r
                    self.sprite="pm1r"
                    self.dimension=(10,0)
                elif gamertime-self.animtime>60*0.875:
                    self.image=pm8r
                    self.sprite="pm8r"
                    self.dimension=(3,0)
                elif gamertime-self.animtime>60*0.75:
                    self.image=pm7r
                    self.sprite="pm7r"
                    self.dimension=(11,0)
                elif gamertime-self.animtime>60*0.625:
                    self.image=pm6r
                    self.sprite="pm6r"
                    self.dimension=(14,0)
                elif gamertime-self.animtime>60*0.5:
                    self.image=pm5r
                    self.sprite="pm5r"
                    self.dimension=(8,0)
                elif gamertime-self.animtime>60*0.375:
                    self.image=pm4r
                    self.sprite="pm4r"
                    self.dimension=(2,0)
                elif gamertime-self.animtime>60*0.25:
                    self.image=pm3r
                    self.sprite="pm3r"
                    self.dimension=(7,0)
                elif gamertime-self.animtime>60*0.125:
                    self.image=pm2r
                    self.sprite="pm2r"
                    self.dimension=(19,0)
                else:
                    self.image=pm1r
                    self.sprite="pm1r"
                    self.dimension=(10,0)
            else:
                if gamertime-self.animtime>60:
                    self.animtime=gamertime
                    self.image=pm1l
                    self.sprite="pm1l"
                    self.dimension=(9,0)
                elif gamertime-self.animtime>60*0.875:
                    self.image=pm8l
                    self.sprite="pm8l"
                    self.dimension=(8,0)
                elif gamertime-self.animtime>60*0.75:
                    self.image=pm7l
                    self.sprite="pm7l"
                    self.dimension=(11,0)
                elif gamertime-self.animtime>60*0.625:
                    self.image=pm6l
                    self.sprite="pm6l"
                    self.dimension=(14,0)
                elif gamertime-self.animtime>60*0.5:
                    self.image=pm5l
                    self.sprite="pm5l"
                    self.dimension=(11,0)
                elif gamertime-self.animtime>60*0.375:
                    self.image=pm4l
                    self.sprite="pm4l"
                    self.dimension=(15,0)
                elif gamertime-self.animtime>60*0.25:
                    self.image=pm3l
                    self.sprite="pm3l"
                    self.dimension=(9,0)
                elif gamertime-self.animtime>60*0.125:
                    self.image=pm2l
                    self.sprite="pm2l"
                    self.dimension=(9,0)
                else:
                    self.image=pm1l
                    self.sprite="pm1l"
                    self.dimension=(9,0)
    def rolling(self):
        if self.direction=="r":
            if gamertime-self.animtime>60*0.999:
                self.image=pr1r
                self.sprite="pr1r"
                self.Rolling=False
                self.animtime=gamertime
                self.dimension=(20,16)
                self.move(dy=-1)
            elif gamertime-self.animtime>60*0.888:
                self.image=pr9r
                self.sprite="pr9r"
                self.dimension=(8,16)
            elif gamertime-self.animtime>60*0.777:
                self.image=pr8r
                self.sprite="pr8r"
                self.dimension=(12,16)
            elif gamertime-self.animtime>60*0.666:
                self.image=pr7r
                self.sprite="pr7r"
                self.dimension=(13,16)
            elif gamertime-self.animtime>60*0.555:
                self.image=pr6r
                self.sprite="pr6r"
                self.dimension=(6,16)
            elif gamertime-self.animtime>60*0.444:
                self.image=pr5r
                self.sprite="pr5r"
                self.dimension=(0,16)
            elif gamertime-self.animtime>60*0.333:
                self.image=pr4r
                self.sprite="pr4r"
                self.dimension=(7,16)
            elif gamertime-self.animtime>60*0.222:
                self.image=pr3r
                self.sprite="pr3r"
                self.dimension=(6,16)
            elif gamertime-self.animtime>60*0.111:
                self.image=pr2r
                self.sprite="pr2r"
                self.dimension=(25,16)
            else:
                self.image=pr1r
                self.sprite="pr1r"
                self.dimension=(20,16)
        else:
            if gamertime-self.animtime>60*0.999:
                self.image=pr1l
                self.sprite="pr1l"
                self.animtime=gamertime
                self.Rolling=False
                self.dimension=(20,16)
                self.move(dy=-1)
            elif gamertime-self.animtime>60*0.888:
                self.image=pr9l
                self.sprite="pr9l"
                self.dimension=(32,16)
            elif gamertime-self.animtime>60*0.777:
                self.image=pr8l
                self.sprite="pr8l"
                self.dimension=(28,16)
            elif gamertime-self.animtime>60*0.666:
                self.image=pr7l
                self.sprite="pr7l"
                self.dimension=(27,16)
            elif gamertime-self.animtime>60*0.555:
                self.image=pr6l
                self.sprite="pr6l"
                self.dimension=(34,16)
            elif gamertime-self.animtime>60*0.444:
                self.image=pr5l
                self.sprite="pr5l"
                self.dimension=(40,16)
            elif gamertime-self.animtime>60*0.333:
                self.image=pr4l
                self.sprite="pr4l"
                self.dimension=(33,16)
            elif gamertime-self.animtime>60*0.222:
                self.image=pr3l
                self.sprite="pr3l"
                self.dimension=(34,16)
            elif gamertime-self.animtime>60*0.111:
                self.image=pr2l
                self.sprite="pr2l"
                self.dimension=(15,16)
            else:
                self.image=pr1l
                self.sprite="pr1l"
                self.dimension=(20,16)
    def stationary(self):
        if self.onGround:
            if self.direction=="r":
                self.image=psr
                self.sprite="psr"
                self.dimension=(3,0)
            else:
                self.image=psl
                self.sprite="psl"
                self.dimension=(14,0)
    def jumping(self):
        if self.direction=="r":
            self.image=pjr
            self.sprite="pjr"
            self.dimension=(12,0)
        else:
            self.image=pjl
            self.sprite="pjl"
            self.dimension=(17,0)
    def drawing(self):
        if pygame.mouse.get_pos()[0]-width/2>0:
            self.direction="r"
        else:
            self.direction="l"
        try:
            self.angle=-math.atan(((pygame.mouse.get_pos()[1]-self.rect.y-24)/(math.sqrt((pygame.mouse.get_pos()[0]-width/2)**2+(pygame.mouse.get_pos()[1]-self.rect.y-24)**2)))/((pygame.mouse.get_pos()[0]-width/2)/(math.sqrt((pygame.mouse.get_pos()[0]-width/2)**2+(pygame.mouse.get_pos()[1]-self.rect.y-24)**2))))
        except:
            self.angle=math.pi/2
        if gamertime-self.time<60 and gamertime-self.time>31:
            self.velocity=(gamertime-self.time)/6
        elif gamertime-self.time>=60:
            self.velocity=10
        self.shooting()
    def shooting(self):
        if self.direction=="r":
            if gamertime-self.time>=45:
                self.image=pf4r
                self.sprite="pf4r"
                self.dimension=(7,0)
            elif gamertime-self.time>=30:
                self.image=pf3r
                self.sprite="pf3r"
                self.dimension=(7,0)
            elif gamertime-self.time>=15:
                self.image=pf2r
                self.sprite="pf2r"
                self.dimension=(7,0)
            else:
                self.image=pf1r
                self.sprite="pf1r"
                self.dimension=(7,0)
        else:
            if gamertime-self.time>=45:
                self.image=pf4l
                self.sprite="pf4l"
                self.dimension=(33,0)
            elif gamertime-self.time>=30:
                self.image=pf3l
                self.sprite="pf3l"
                self.dimension=(33,0)
            elif gamertime-self.time>=15:
                self.image=pf2l
                self.sprite="pf2l"
                self.dimension=(33,0)
            else:
                self.image=pf1l
                self.sprite="pf1l"
                self.dimension=(33,0)
    def fired(self):
        for arrow in self.shots:
            if arrow[1]=="r":
                arrow[0][0]+=arrow[2]*math.cos(arrow[3])
            else:
                arrow[0][0]-=arrow[2]*math.cos(arrow[3])
            arrow[0][1]-=arrow[2]*math.sin(arrow[3])
            arrow[2]=math.sqrt((arrow[2]*math.cos(arrow[3]))**2+((arrow[2]*math.sin(arrow[3]))-0.05)**2)
            arrow[3]=math.atan(((arrow[2]*math.sin(arrow[3]))-0.05)/(arrow[2]*math.cos(arrow[3])))
            if arrow[0][1]>height:
                self.shots.remove(arrow)
            if arrow[1]=="r":
                firstdrawpoint=((arrow[0][0]-10*math.cos(arrow[3]))-player.rect.x+width/2,(arrow[0][1]+10*math.sin(arrow[3])))
                lastdrawpoint=((arrow[0][0]+10*math.cos(arrow[3]))-player.rect.x+width/2,arrow[0][1]-10*math.sin(arrow[3]))
                pygame.draw.rect(gamescreen,(220,20,60),pygame.Rect(firstdrawpoint[0]-1,firstdrawpoint[1]-1,4,4))
                pygame.draw.line(gamescreen,(160,82,45),firstdrawpoint,lastdrawpoint,2)
                pygame.draw.rect(gamescreen,(255,255,255),pygame.Rect(lastdrawpoint[0],lastdrawpoint[1],2,2))
            else:
                firstdrawpoint=((arrow[0][0]-10*math.cos(arrow[3]))-player.rect.x+width/2,arrow[0][1]-10*math.sin(arrow[3]))
                lastdrawpoint=((arrow[0][0]+10*math.cos(arrow[3]))-player.rect.x+width/2,arrow[0][1]+10*math.sin(arrow[3]))
                pygame.draw.rect(gamescreen,(220,20,60),pygame.Rect(lastdrawpoint[0]-1,lastdrawpoint[1]-1,4,4))
                pygame.draw.line(gamescreen,(160,82,45),firstdrawpoint,lastdrawpoint,2)
                pygame.draw.rect(gamescreen,(255,255,255),pygame.Rect(firstdrawpoint[0],firstdrawpoint[1],2,2))
    def firing(self):
        if gamertime-self.time>=15:
            if self.direction=="r":
                self.image=pf5r
                self.sprite="pf5r"
                self.arrowdirection="r"
                self.shots.append([[self.rect.x+21,self.rect.y+17],self.arrowdirection,self.velocity,self.angle])
            else:
                self.image=pf5l
                self.sprite="pf5l"
                self.angle=math.pi-self.angle
                self.arrowdirection="l"
                self.shots.append([[self.rect.x-4,self.rect.y+17],self.arrowdirection,self.velocity,self.angle])
            channelplayed=False
            for channel in shotchannel:
                if not channel.get_busy():
                    channel.play(shotsound)
                    channelplayed=True
            del channelplayed
    def deathanim(self):
        if self.direction=="r":
            if gamertime-self.deathtime>24:
                self.dies()
                self.death=False
            elif gamertime-self.deathtime>18:
                self.image=pd4r
                self.dimension=(32,0)
            elif gamertime-self.deathtime>12:
                self.image=pd3r
                self.dimension=(30,0)
            elif gamertime-self.deathtime>6:
                self.image=pd2r
                self.dimension=(23,0)
            else:
                self.image=pd1r
                self.dimension=(4,0)
        else:
            if gamertime-self.deathtime>24:
                self.dies()
                self.death=False
            elif gamertime-self.deathtime>18:
                self.image=pd4l
                self.dimension=(26,0)
            elif gamertime-self.deathtime>12:
                self.image=pd3l
                self.dimension=(24,0)
            elif gamertime-self.deathtime>6:
                self.image=pd2l
                self.dimension=(17,0)
            else:
                self.image=pd1l
                self.dimension=(35,0)
    def dies(self):
        global enemies,blocks,backgrounds
        blocks=[]
        backgrounds=[]
        enemies=[]
        self.arrows=[]
        self.shots=[]
        self.rect.x,self.rect.y=self.start
        x=y=0
        with open("data/levels/1.txt","r")as f:
            for row in f:
                for col in row:
                    #Grass
                    if col.upper()=="=":
                        blocks.append(Block(x,y,"GTM"))
                    if col.upper()=="[":
                        blocks.append(Block(x,y,"GBL"))
                    if col.upper()=="]":
                        blocks.append(Block(x,y,"GBR"))
                    if col.upper()=="<":
                        blocks.append(Block(x,y,"GTL"))
                    if col.upper()==">":
                        blocks.append(Block(x,y,"GTR"))
                    if col.upper()=="(":
                        blocks.append(Block(x,y,"GTML"))
                    if col.upper()==")":
                        blocks.append(Block(x,y,"GTMR"))
                    #NonGrass
                    if col.upper()=="-":
                        blocks.append(Block(x,y,"TM"))
                    if col.upper()=="L":
                        blocks.append(Block(x,y,"TL"))
                    if col.upper()=="R":
                        blocks.append(Block(x,y,"TR"))
                    if col.upper()=="{":
                        blocks.append(Block(x,y,"LM"))
                    if col.upper()=="}":
                        blocks.append(Block(x,y,"RM"))
                    if col.upper()=="_":
                        blocks.append(Block(x,y,"BM"))
                    if col.upper()=="X":
                        blocks.append(Block(x,y,"BL"))
                    if col.upper()=="Y":
                        blocks.append(Block(x,y,"BR"))
                    #Aesthetics
                    if col.upper()=="T":
                        blocks.append(Block(x,y,"TREE"))
                    if col.upper()=="B":
                        backgrounds.append(pygame.Rect(x,y,16,16))
                    #Entities
                    if col.upper()=="M":
                        enemies.append(Enemy(x,y))
                    x+=16
                y+=16
                x=0
            f.close()
class Enemy(object):
    def __init__(self,wx,wy):
        self.width=16
        self.height=40
        self.rect=pygame.Rect(wx,wy-self.height+16,self.width,self.height)
        self.g=0
        self.image=emm1l
        self.animtime=0
        self.spawntime=0
        self.deathtime=0
        self.onGround=False
        self.spawned=False
        self.spawnstart=False
        self.death=False
        self.deathstart=False
        self.direction="l"
        self.deathdirection="l"
        self.dimension=(4,3)
    def move(self,dx=0,dy=0):
        global gamertime
        if self.rect.colliderect(player.rect)and not player.death:
            player.death=True
            player.deathtime=gamertime
        if dx!=0:
            self.rect.x+=dx
        if dx>0:
            self.animation("r")
        if dx<0:
            self.animation("l")
        if dy!=0:
            self.onGround=False
            self.rect.y+=dy
        for block in blocks:
            if self.rect.colliderect(block.rect):
                if dy>0:
                    self.rect=pygame.Rect(self.rect.x,self.rect.y,self.width,self.height)
                    self.rect.bottom=block.rect.top
                    self.g=0
                    self.onGround=True
                if dy<0:
                    self.rect.top=block.rect.bottom
                if dx>0:
                    self.rect.right=block.rect.left
                    if self.onGround:
                        self.jump()
                if dx<0:
                    self.rect.left=block.rect.right
                    if self.onGround:
                        self.jump()
    def animation(self,direction):
        if self.onGround:
            self.direction=direction
            if direction=="r":
                if gamertime-self.animtime>60*1.08:
                    self.animtime=gamertime
                    self.image=emm1r
                    self.sprite="emm1r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*1.02:
                    self.image=emm18r
                    self.sprite="emm18r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.96:
                    self.image=emm17r
                    self.sprite="emm17r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.9:
                    self.image=emm16r
                    self.sprite="emm16r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.84:
                    self.image=emm15r
                    self.sprite="emm15r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.78:
                    self.image=emm14r
                    self.sprite="emm14r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.72:
                    self.image=emm13r
                    self.sprite="emm13r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.66:
                    self.image=emm12r
                    self.sprite="emm12r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.6:
                    self.image=emm11r
                    self.sprite="emm11r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.54:
                    self.image=emm10r
                    self.sprite="emm10r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.48:
                    self.image=emm9r
                    self.sprite="emm9r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.42:
                    self.image=emm8r
                    self.sprite="emm8r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.36:
                    self.image=emm7r
                    self.sprite="emm7r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.3:
                    self.image=emm6r
                    self.sprite="emm6r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.24:
                    self.image=emm5r
                    self.sprite="emm5r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.18:
                    self.image=emm4r
                    self.sprite="emm4r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.12:
                    self.image=emm3r
                    self.sprite="emm3r"
                    self.dimension=(4,3)
                elif gamertime-self.animtime>60*0.06:
                    self.image=emm2r
                    self.sprite="emm2r"
                    self.dimension=(4,3)
                else:
                    self.image=emm1r
                    self.sprite="emm1r"
                    self.dimension=(4,3)
            else:
                if gamertime-self.animtime>60*1.08:
                    self.animtime=gamertime
                    self.image=emm1l
                    self.sprite="emm1l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*1.02:
                    self.image=emm18l
                    self.sprite="emm18l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.96:
                    self.image=emm17l
                    self.sprite="emm17l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.9:
                    self.image=emm16l
                    self.sprite="emm16l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.84:
                    self.image=emm15l
                    self.sprite="emm15l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.78:
                    self.image=emm14l
                    self.sprite="emm14l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.72:
                    self.image=emm13l
                    self.sprite="emm13l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.66:
                    self.image=emm12l
                    self.sprite="emm12l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.6:
                    self.image=emm11l
                    self.sprite="emm11l"
                    self.dimension=(16,3)
                elif gamertime-self.animtime>60*0.54:
                    self.image=emm10l
                    self.sprite="emm10l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.48:
                    self.image=emm9l
                    self.sprite="emm9l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.42:
                    self.image=emm8l
                    self.sprite="emm8l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.36:
                    self.image=emm7l
                    self.sprite="emm7l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.3:
                    self.image=emm6l
                    self.sprite="emm6l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.24:
                    self.image=emm5l
                    self.sprite="emm5l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.18:
                    self.image=emm4l
                    self.sprite="emm4l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.12:
                    self.image=emm3l
                    self.sprite="emm3l"
                    self.dimension=(13,3)
                elif gamertime-self.animtime>60*0.06:
                    self.image=emm2l
                    self.sprite="emm2l"
                    self.dimension=(13,3)
                else:
                    self.image=emm1l
                    self.sprite="emm1l"
                    self.dimension=(13,3)
    def spawning(self):
        if gamertime-self.spawntime>30*2.1:
            self.spawned=True
            self.spawnstart=False
            self.image=ems1
            self.sprite="ems1"
            self.dimension=(4,3)
        elif gamertime-self.spawntime>30*1.96:
            self.image=ems15
            self.sprite="ems15"
            self.dimension=(4,3)
        elif gamertime-self.spawntime>30*1.82:
            self.image=ems14
            self.sprite="ems14"
            self.dimension=(4,3)
        elif gamertime-self.spawntime>30*1.68:
            self.image=ems13
            self.sprite="ems13"
            self.dimension=(4,3)
        elif gamertime-self.spawntime>30*1.54:
            self.image=ems12
            self.sprite="ems12"
            self.dimension=(4,3)
        elif gamertime-self.spawntime>30*1.4:
            self.image=ems11
            self.sprite="ems11"
            self.dimension=(4,3)
        elif gamertime-self.spawntime>30*1.26:
            self.image=ems10
            self.sprite="ems10"
            self.dimension=(4,3)
        elif gamertime-self.spawntime>30*1.12:
            self.image=ems9
            self.sprite="ems9"
            self.dimension=(4,3)
        elif gamertime-self.spawntime>30*0.98:
            self.image=ems8
            self.sprite="ems8"
            self.dimension=(4,3)
        elif gamertime-self.spawntime>30*0.84:
            self.image=ems7
            self.sprite="ems7"
            self.dimension=(4,3)
        elif gamertime-self.spawntime>30*0.7:
            self.image=ems6
            self.sprite="ems6"
            self.dimension=(4,3)
        elif gamertime-self.spawntime>30*0.56:
            self.image=ems5
            self.sprite="ems5"
            self.dimension=(4,3)
        elif gamertime-self.spawntime>30*0.42:
            self.image=ems4
            self.sprite="ems4"
            self.dimension=(4,3)
        elif gamertime-self.spawntime>30*0.28:
            self.image=ems3
            self.sprite="ems3"
            self.dimension=(4,3)
        elif gamertime-self.spawntime>30*0.14:
            self.image=ems2
            self.sprite="ems2"
            self.dimension=(4,3)
        else:
            self.image=ems1
            self.sprite="ems1"
            self.dimension=(4,3)
            channelplayed=False
            for channel in spawnchannel:
                if not channel.get_busy():
                    channel.play(spawnsound)
                    channelplayed=True
            del channelplayed
    def dies(self):
        if self.deathdirection=="r":
            if gamertime-self.deathtime>120:
                self.death=True
                self.deathstart=False
            elif gamertime-self.animtime>60*1.9:
                self.image=emd20r
                self.sprite="emd20r"
                self.dimension=(4,3)
            elif gamertime-self.animtime>60*1.8:
                self.image=emd19r
                self.sprite="emd19r"
                self.dimension=(4,3)
            elif gamertime-self.animtime>60*1.7:
                self.image=emd18r
                self.sprite="emd18r"
                self.dimension=(4,6)
            elif gamertime-self.animtime>60*1.6:
                self.image=emd17r
                self.sprite="emd17r"
                self.dimension=(4,14)
            elif gamertime-self.animtime>60*1.5:
                self.image=emd16r
                self.sprite="emd16r"
                self.dimension=(4,14)
            elif gamertime-self.animtime>60*1.4:
                self.image=emd15r
                self.sprite="emd15r"
                self.dimension=(4,12)
            elif gamertime-self.animtime>60*1.3:
                self.image=emd14r
                self.sprite="emd14r"
                self.dimension=(4,6)
            elif gamertime-self.animtime>60*1.2:
                self.image=emd13r
                self.sprite="emd13r"
                self.dimension=(4,3)
            elif gamertime-self.animtime>66:
                self.image=emd12r
                self.sprite="emd12r"
                self.dimension=(4,3)
            elif gamertime-self.animtime>60:
                self.image=emd11r
                self.sprite="emd11r"
                self.dimension=(4,3)
            elif gamertime-self.animtime>60*0.9:
                self.image=emd10r
                self.sprite="emd10r"
                self.dimension=(4,3)
            elif gamertime-self.animtime>60*0.8:
                self.image=emd9r
                self.sprite="emd9r"
                self.dimension=(4,3)
            elif gamertime-self.animtime>60*0.7:
                self.image=emd8r
                self.sprite="emd8r"
                self.dimension=(4,3)
            elif gamertime-self.animtime>60*0.6:
                self.image=emd7r
                self.sprite="emd7r"
                self.dimension=(4,3)
            elif gamertime-self.animtime>60*0.5:
                self.image=emd6r
                self.sprite="emd6r"
                self.dimension=(4,3)
            elif gamertime-self.animtime>60*0.4:
                self.image=emd5r
                self.sprite="emd5r"
                self.dimension=(4,3)
            elif gamertime-self.animtime>60*0.3:
                self.image=emd4r
                self.sprite="emd4r"
                self.dimension=(4,3)
            elif gamertime-self.animtime>60*0.2:
                self.image=emd3r
                self.sprite="emd3r"
                self.dimension=(4,3)
            elif gamertime-self.animtime>60*0.1:
                self.image=emd2r
                self.sprite="emd2r"
                self.dimension=(4,3)
            else:
                self.image=emd1r
                self.sprite="emd1r"
                self.dimension=(4,3)
        else:
            if gamertime-self.deathtime>120:
                self.death=True
                self.deathstart=False
            elif gamertime-self.animtime>60*1.9:
                self.image=emd20l
                self.sprite="emd20l"
                self.dimension=(13,3)
            elif gamertime-self.animtime>60*1.8:
                self.image=emd19l
                self.sprite="emd19l"
                self.dimension=(13,3)
            elif gamertime-self.animtime>60*1.7:
                self.image=emd18l
                self.sprite="emd18l"
                self.dimension=(13,6)
            elif gamertime-self.animtime>60*1.6:
                self.image=emd17l
                self.sprite="emd17l"
                self.dimension=(13,14)
            elif gamertime-self.animtime>60*1.5:
                self.image=emd16l
                self.sprite="emd16l"
                self.dimension=(13,14)
            elif gamertime-self.animtime>60*1.4:
                self.image=emd15l
                self.sprite="emd15l"
                self.dimension=(13,12)
            elif gamertime-self.animtime>60*1.3:
                self.image=emd14l
                self.sprite="emd14l"
                self.dimension=(13,6)
            elif gamertime-self.animtime>60*1.2:
                self.image=emd13l
                self.sprite="emd13l"
                self.dimension=(13,3)
            elif gamertime-self.animtime>66:
                self.image=emd12l
                self.sprite="emd12l"
                self.dimension=(13,3)
            elif gamertime-self.animtime>60:
                self.image=emd11l
                self.sprite="emd11l"
                self.dimension=(13,3)
            elif gamertime-self.animtime>60*0.9:
                self.image=emd10l
                self.sprite="emd10l"
                self.dimension=(13,3)
            elif gamertime-self.animtime>60*0.8:
                self.image=emd9l
                self.sprite="emd9l"
                self.dimension=(13,3)
            elif gamertime-self.animtime>60*0.7:
                self.image=emd8l
                self.sprite="emd8l"
                self.dimension=(13,3)
            elif gamertime-self.animtime>60*0.6:
                self.image=emd7l
                self.sprite="emd7l"
                self.dimension=(13,3)
            elif gamertime-self.animtime>60*0.5:
                self.image=emd6l
                self.sprite="emd6l"
                self.dimension=(13,3)
            elif gamertime-self.animtime>60*0.4:
                self.image=emd5l
                self.sprite="emd5l"
                self.dimension=(13,3)
            elif gamertime-self.animtime>60*0.3:
                self.image=emd4l
                self.sprite="emd4l"
                self.dimension=(13,3)
            elif gamertime-self.animtime>60*0.2:
                self.image=emd3l
                self.sprite="emd3l"
                self.dimension=(13,3)
            elif gamertime-self.animtime>60*0.1:
                self.image=emd2l
                self.sprite="emd2l"
                self.dimension=(13,3)
            else:
                self.image=emd1l
                self.sprite="emd1l"
                self.dimension=(13,3)
    def jump(self):
        self.onGround=False
        self.g=-5
class Block(object):
    def __init__(self,wx,wy,obj):
        self.type=obj
        if obj=="TREE":
            if random.choice([0,1])==1:
                self.dimensions=(16,64)
                self.rect=pygame.Rect(wx,wy,32,16)
                self.image=treer
            else:
                self.dimensions=(32,64)
                self.rect=pygame.Rect(wx,wy,32,16)
                self.image=treel
        if obj=="BL":
            self.dimensions=(0,0)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=bl
        if obj=="BM":
            self.dimensions=(0,0)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=bm
        if obj=="BR":
            self.dimensions=(0,0)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=br
        if obj=="GBL":
            self.dimensions=(0,0)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=gbl
        if obj=="GBR":
            self.dimensions=(0,0)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=gbr
        if obj=="GBUSHL":
            self.dimensions=(0,16)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=gbushl
        if obj=="GBUSHR":
            self.dimensions=(0,16)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=gbushr
        if obj=="GTL":
            self.dimensions=(0,3)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=gtl
        if obj=="GTM":
            self.dimensions=(0,4)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=gtm
        if obj=="GTML":
            self.dimensions=(0,4)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=gtml
        if obj=="GTMR":
            self.dimensions=(0,4)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=gtmr
        if obj=="GTR":
            self.dimensions=(0,4)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=gtr
        if obj=="LM":
            self.dimensions=(0,0)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=lm
        if obj=="TL":
            self.dimensions=(0,0)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=tl
        if obj=="TM":
            self.dimensions=(0,0)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=tm
        if obj=="TR":
            self.dimensions=(0,0)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=tr
        if obj=="RM":
            self.dimensions=(0,0)
            self.rect=pygame.Rect(wx,wy,16,16)
            self.image=rm
def volume_change(boolean):
    global volume,volumetime,shotsound,spawnsound,channel0
    if boolean:
        volume+=0.1
    else:
        volume-=0.1
    if volume>=1:
        volume=0.9
    if volume<0:
        volume=0
    for channel in shotchannel:
        channel.set_volume(volume)
    for channel in spawnchannel:
        channel.set_volume(volume)
    channel0.set_volume(volume)
    volumetime=gamertime
spriteLOC="data/sprites/"
r=True
blocks=[]
backgrounds=[]
enemies=[]
os.environ["SDL_VIDEO_WINDOW_POS"]=str(int((true_screen_width-screen_width)/2))+","+str(int((true_screen_height-screen_height)/2))
pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))
gamescreen=pygame.Surface((width,height))
clock=pygame.time.Clock()
pygame.mouse.set_visible(False)
cursorimg=pygame.image.load(spriteLOC+"crosshair.png")
myfont=pygame.font.Font("data/prstart.ttf",20)
testtextimg=myfont.render(message,0,(255,255,255))
#Player
#Stationary
psr=pygame.image.load(spriteLOC+"entities/player/stationary.png")
psl=pygame.transform.flip(psr,True,False)
#Jumping
pjr=pygame.image.load(spriteLOC+"entities/player/jumping.png")
pjl=pygame.transform.flip(pjr,True,False)
#Moving
pm1r=pygame.image.load(spriteLOC+"entities/player/run/1.png")
pm2r=pygame.image.load(spriteLOC+"entities/player/run/2.png")
pm3r=pygame.image.load(spriteLOC+"entities/player/run/3.png")
pm4r=pygame.image.load(spriteLOC+"entities/player/run/4.png")
pm5r=pygame.image.load(spriteLOC+"entities/player/run/5.png")
pm6r=pygame.image.load(spriteLOC+"entities/player/run/6.png")
pm7r=pygame.image.load(spriteLOC+"entities/player/run/7.png")
pm8r=pygame.image.load(spriteLOC+"entities/player/run/8.png")
pm1l=pygame.transform.flip(pm1r,True,False)
pm2l=pygame.transform.flip(pm2r,True,False)
pm3l=pygame.transform.flip(pm3r,True,False)
pm4l=pygame.transform.flip(pm4r,True,False)
pm5l=pygame.transform.flip(pm5r,True,False)
pm6l=pygame.transform.flip(pm6r,True,False)
pm7l=pygame.transform.flip(pm7r,True,False)
pm8l=pygame.transform.flip(pm8r,True,False)
#Firing
pf1r=pygame.image.load(spriteLOC+"entities/player/fire/1.png")
pf2r=pygame.image.load(spriteLOC+"entities/player/fire/2.png")
pf3r=pygame.image.load(spriteLOC+"entities/player/fire/3.png")
pf4r=pygame.image.load(spriteLOC+"entities/player/fire/4.png")
pf5r=pygame.image.load(spriteLOC+"entities/player/fire/5.png")
pf1l=pygame.transform.flip(pf1r,True,False)
pf2l=pygame.transform.flip(pf2r,True,False)
pf3l=pygame.transform.flip(pf3r,True,False)
pf4l=pygame.transform.flip(pf4r,True,False)
pf5l=pygame.transform.flip(pf5r,True,False)
#Rolling
pr1r=pygame.image.load(spriteLOC+"entities/player/roll/1.png")
pr2r=pygame.image.load(spriteLOC+"entities/player/roll/2.png")
pr3r=pygame.image.load(spriteLOC+"entities/player/roll/3.png")
pr4r=pygame.image.load(spriteLOC+"entities/player/roll/4.png")
pr5r=pygame.image.load(spriteLOC+"entities/player/roll/5.png")
pr6r=pygame.image.load(spriteLOC+"entities/player/roll/6.png")
pr7r=pygame.image.load(spriteLOC+"entities/player/roll/7.png")
pr8r=pygame.image.load(spriteLOC+"entities/player/roll/8.png")
pr9r=pygame.image.load(spriteLOC+"entities/player/roll/9.png")
pr1l=pygame.transform.flip(pr1r,True,False)
pr2l=pygame.transform.flip(pr2r,True,False)
pr3l=pygame.transform.flip(pr3r,True,False)
pr4l=pygame.transform.flip(pr4r,True,False)
pr5l=pygame.transform.flip(pr5r,True,False)
pr6l=pygame.transform.flip(pr6r,True,False)
pr7l=pygame.transform.flip(pr7r,True,False)
pr8l=pygame.transform.flip(pr8r,True,False)
pr9l=pygame.transform.flip(pr9r,True,False)
#Death
pd1r=pygame.image.load(spriteLOC+"entities/player/death/1.png")
pd2r=pygame.image.load(spriteLOC+"entities/player/death/2.png")
pd3r=pygame.image.load(spriteLOC+"entities/player/death/3.png")
pd4r=pygame.image.load(spriteLOC+"entities/player/death/4.png")
pd1l=pygame.transform.flip(pd1r,True,False)
pd2l=pygame.transform.flip(pd2r,True,False)
pd3l=pygame.transform.flip(pd3r,True,False)
pd4l=pygame.transform.flip(pd4r,True,False)
#Enemy
#Moving
emm1r=pygame.image.load(spriteLOC+"entities/mummy/run/1.png")
emm2r=pygame.image.load(spriteLOC+"entities/mummy/run/2.png")
emm3r=pygame.image.load(spriteLOC+"entities/mummy/run/3.png")
emm4r=pygame.image.load(spriteLOC+"entities/mummy/run/4.png")
emm5r=pygame.image.load(spriteLOC+"entities/mummy/run/5.png")
emm6r=pygame.image.load(spriteLOC+"entities/mummy/run/6.png")
emm7r=pygame.image.load(spriteLOC+"entities/mummy/run/7.png")
emm8r=pygame.image.load(spriteLOC+"entities/mummy/run/8.png")
emm9r=pygame.image.load(spriteLOC+"entities/mummy/run/9.png")
emm10r=pygame.image.load(spriteLOC+"entities/mummy/run/10.png")
emm11r=pygame.image.load(spriteLOC+"entities/mummy/run/11.png")
emm12r=pygame.image.load(spriteLOC+"entities/mummy/run/12.png")
emm13r=pygame.image.load(spriteLOC+"entities/mummy/run/13.png")
emm14r=pygame.image.load(spriteLOC+"entities/mummy/run/14.png")
emm15r=pygame.image.load(spriteLOC+"entities/mummy/run/15.png")
emm16r=pygame.image.load(spriteLOC+"entities/mummy/run/16.png")
emm17r=pygame.image.load(spriteLOC+"entities/mummy/run/17.png")
emm18r=pygame.image.load(spriteLOC+"entities/mummy/run/18.png")
emm1l=pygame.transform.flip(emm1r,True,False)
emm2l=pygame.transform.flip(emm2r,True,False)
emm3l=pygame.transform.flip(emm3r,True,False)
emm4l=pygame.transform.flip(emm4r,True,False)
emm5l=pygame.transform.flip(emm5r,True,False)
emm6l=pygame.transform.flip(emm6r,True,False)
emm7l=pygame.transform.flip(emm7r,True,False)
emm8l=pygame.transform.flip(emm8r,True,False)
emm9l=pygame.transform.flip(emm9r,True,False)
emm10l=pygame.transform.flip(emm10r,True,False)
emm11l=pygame.transform.flip(emm11r,True,False)
emm12l=pygame.transform.flip(emm12r,True,False)
emm13l=pygame.transform.flip(emm13r,True,False)
emm14l=pygame.transform.flip(emm14r,True,False)
emm15l=pygame.transform.flip(emm15r,True,False)
emm16l=pygame.transform.flip(emm16r,True,False)
emm17l=pygame.transform.flip(emm17r,True,False)
emm18l=pygame.transform.flip(emm18r,True,False)
#Spawning
ems1=pygame.image.load(spriteLOC+"entities/mummy/spawn/1.png")
ems2=pygame.image.load(spriteLOC+"entities/mummy/spawn/2.png")
ems3=pygame.image.load(spriteLOC+"entities/mummy/spawn/3.png")
ems4=pygame.image.load(spriteLOC+"entities/mummy/spawn/4.png")
ems5=pygame.image.load(spriteLOC+"entities/mummy/spawn/5.png")
ems6=pygame.image.load(spriteLOC+"entities/mummy/spawn/6.png")
ems7=pygame.image.load(spriteLOC+"entities/mummy/spawn/7.png")
ems8=pygame.image.load(spriteLOC+"entities/mummy/spawn/8.png")
ems9=pygame.image.load(spriteLOC+"entities/mummy/spawn/9.png")
ems10=pygame.image.load(spriteLOC+"entities/mummy/spawn/10.png")
ems11=pygame.image.load(spriteLOC+"entities/mummy/spawn/11.png")
ems12=pygame.image.load(spriteLOC+"entities/mummy/spawn/12.png")
ems13=pygame.image.load(spriteLOC+"entities/mummy/spawn/13.png")
ems14=pygame.image.load(spriteLOC+"entities/mummy/spawn/14.png")
ems15=pygame.image.load(spriteLOC+"entities/mummy/spawn/15.png")
#Death
emd1l=pygame.image.load(spriteLOC+"entities/mummy/death/1.png")
emd2l=pygame.image.load(spriteLOC+"entities/mummy/death/2.png")
emd3l=pygame.image.load(spriteLOC+"entities/mummy/death/3.png")
emd4l=pygame.image.load(spriteLOC+"entities/mummy/death/4.png")
emd5l=pygame.image.load(spriteLOC+"entities/mummy/death/5.png")
emd6l=pygame.image.load(spriteLOC+"entities/mummy/death/6.png")
emd7l=pygame.image.load(spriteLOC+"entities/mummy/death/7.png")
emd8l=pygame.image.load(spriteLOC+"entities/mummy/death/8.png")
emd9l=pygame.image.load(spriteLOC+"entities/mummy/death/9.png")
emd10l=pygame.image.load(spriteLOC+"entities/mummy/death/10.png")
emd11l=pygame.image.load(spriteLOC+"entities/mummy/death/11.png")
emd12l=pygame.image.load(spriteLOC+"entities/mummy/death/12.png")
emd13l=pygame.image.load(spriteLOC+"entities/mummy/death/13.png")
emd14l=pygame.image.load(spriteLOC+"entities/mummy/death/14.png")
emd15l=pygame.image.load(spriteLOC+"entities/mummy/death/15.png")
emd16l=pygame.image.load(spriteLOC+"entities/mummy/death/16.png")
emd17l=pygame.image.load(spriteLOC+"entities/mummy/death/17.png")
emd18l=pygame.image.load(spriteLOC+"entities/mummy/death/18.png")
emd19l=pygame.image.load(spriteLOC+"entities/mummy/death/19.png")
emd20l=pygame.image.load(spriteLOC+"entities/mummy/death/20.png")
emd1r=pygame.transform.flip(emd1l,True,False)
emd2r=pygame.transform.flip(emd2l,True,False)
emd3r=pygame.transform.flip(emd3l,True,False)
emd4r=pygame.transform.flip(emd4l,True,False)
emd5r=pygame.transform.flip(emd5l,True,False)
emd6r=pygame.transform.flip(emd6l,True,False)
emd7r=pygame.transform.flip(emd7l,True,False)
emd8r=pygame.transform.flip(emd8l,True,False)
emd9r=pygame.transform.flip(emd9l,True,False)
emd10r=pygame.transform.flip(emd10l,True,False)
emd11r=pygame.transform.flip(emd11l,True,False)
emd12r=pygame.transform.flip(emd12l,True,False)
emd13r=pygame.transform.flip(emd13l,True,False)
emd14r=pygame.transform.flip(emd14l,True,False)
emd15r=pygame.transform.flip(emd15l,True,False)
emd16r=pygame.transform.flip(emd16l,True,False)
emd17r=pygame.transform.flip(emd17l,True,False)
emd18r=pygame.transform.flip(emd18l,True,False)
emd19r=pygame.transform.flip(emd19l,True,False)
emd20r=pygame.transform.flip(emd20l,True,False)
#Blocks
#Plain
bl=pygame.image.load(spriteLOC+"blocks/bl.png")
bm=pygame.image.load(spriteLOC+"blocks/bm.png")
br=pygame.image.load(spriteLOC+"blocks/br.png")
gbl=pygame.image.load(spriteLOC+"blocks/gbl.png")
gbr=pygame.image.load(spriteLOC+"blocks/gbr.png")
gtl=pygame.image.load(spriteLOC+"blocks/gtl.png")
gtm=pygame.image.load(spriteLOC+"blocks/gtm.png")
gtml=pygame.image.load(spriteLOC+"blocks/gtml.png")
gtmr=pygame.image.load(spriteLOC+"blocks/gtmr.png")
gtr=pygame.image.load(spriteLOC+"blocks/gtr.png")
lm=pygame.image.load(spriteLOC+"blocks/lm.png")
tl=pygame.image.load(spriteLOC+"blocks/tl.png")
tm=pygame.image.load(spriteLOC+"blocks/tm.png")
tr=pygame.image.load(spriteLOC+"blocks/tr.png")
rm=pygame.image.load(spriteLOC+"blocks/rm.png")
gbushl=pygame.image.load(spriteLOC+"blocks/gbushl.png")
gbushr=pygame.image.load(spriteLOC+"blocks/gbushr.png")
treer=pygame.image.load(spriteLOC+"treer.png")
treel=pygame.image.load(spriteLOC+"treel.png")
#Background
#Sky
bg=pygame.image.load(spriteLOC+aspect_ratio+"/bg.png")
#Sounds
#Music
#music=pygame.mixer.Sound("data/sounds/music.wav")
#Effects
shotsound=pygame.mixer.Sound("data/sounds/fire.wav")
spawnsound=pygame.mixer.Sound("data/sounds/spawn.wav")
#Channels
pygame.mixer.set_num_channels(16)
channel0=pygame.mixer.Channel(0)
channel0.set_volume(volume)
shotchannel=[pygame.mixer.Channel(1),pygame.mixer.Channel(2),pygame.mixer.Channel(3),pygame.mixer.Channel(4),pygame.mixer.Channel(5)]
spawnchannel=[pygame.mixer.Channel(6),pygame.mixer.Channel(7),pygame.mixer.Channel(8),pygame.mixer.Channel(9),pygame.mixer.Channel(10)]
player=Player()
gamertime=0
volumetime=0
player.dies()
del os,spriteLOC,aspect_ratio,message
while r:
    clock.tick(60)
    gamertime+=1
    gamescreen.blit(bg,(0,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            r=False
    #if not channel0.get_busy():
    #    channel0.play(music)
    try:
        del e
    except:
        pass
    user_input=pygame.key.get_pressed()
    if(user_input[pygame.K_a]or user_input[pygame.K_LEFT])and not player.drawn and not player.Rolling:
        player.move(-2)
    elif(user_input[pygame.K_d]or user_input[pygame.K_RIGHT])and not player.drawn and not player.Rolling:
        player.move(2)
    else:
        player.stationary()
    if user_input[pygame.K_SPACE]and not player.Rolling and not player.drawn and player.onGround:
        player.Rolling=True
        player.animtime=gamertime
        player.rect=pygame.Rect(player.rect.x,player.rect.y+16,player.width,player.height-16)
    elif player.Rolling and player.onGround:
        if gamertime-player.animtime<=60*0.777:
            if player.direction=="r":
                player.move(4,0)
            else:
                player.move(-4,0)
        elif gamertime-player.animtime>60:
            player.Rolling=False
        player.rolling()
    elif player.Rolling:
        if gamertime-player.animtime<=60*0.777:
            if player.direction=="r":
                player.move(4,0)
            else:
                player.move(-4,0)
        elif gamertime-player.animtime>60:
            player.Rolling=False
    if(user_input[pygame.K_w]or user_input[pygame.K_UP])and player.onGround and not player.drawn and not player.Rolling:
        player.jump()
    elif not player.onGround:
        player.move(dy=player.g)
        player.g+=0.25
        player.jumping()
    else:
        tempy=int(player.rect.y)
        player.rect.y=tempy+1
        for block in blocks:
            if player.rect.colliderect(block.rect):
                player.rect.y-=1
                player.onGround=True
        if int(player.rect.y)!=tempy:
            player.onGround=False
            player.rect=pygame.Rect(player.rect.x,player.rect.y,player.width,player.height-16)
    if player.rect.y>height:
        player.dies()
    if user_input[pygame.K_ESCAPE]:
        r=False
    try:
        player.arrow[0]+=1
        player.arrow[0]-=1
    except:
        if pygame.mouse.get_pressed()[0]and not(player.drawn or player.Rolling):
            player.drawn=True
            player.time=gamertime
            player.drawing()
        elif pygame.mouse.get_pressed()[0]and not(not player.drawn or player.Rolling):
            player.drawing()
        elif player.drawn and not player.Rolling:
            player.drawn=False
            player.firing()
    mouse_pos=pygame.mouse.get_pos()
    for arrow in player.arrows:
        if not arrow[4]:
            if arrow[2]=="r":
                pygame.draw.rect(gamescreen,(220,20,60),pygame.Rect(arrow[0][0]-1+arrow[3]-player.rect.x,arrow[0][1]-1,4,4))
                pygame.draw.line(gamescreen,(160,82,45),(arrow[0][0]+arrow[3]-player.rect.x,arrow[0][1]),(arrow[1][0]+arrow[3]-player.rect.x,arrow[1][1]),2)
                pygame.draw.rect(gamescreen,(255,255,255),pygame.Rect(arrow[1][0]+arrow[3]-player.rect.x,arrow[1][1],2,2))
            else:
                pygame.draw.rect(gamescreen,(220,20,60),pygame.Rect(arrow[1][0]-1+arrow[3]-player.rect.x,arrow[1][1]-1,4,4))
                pygame.draw.line(gamescreen,(160,82,45),(arrow[0][0]+arrow[3]-player.rect.x,arrow[0][1]),(arrow[1][0]+arrow[3]-player.rect.x,arrow[1][1]),2)
                pygame.draw.rect(gamescreen,(255,255,255),pygame.Rect(arrow[0][0]+arrow[3]-player.rect.x,arrow[0][1],2,2))
    try:
        del arrow
    except:
        pass
    if player.death:
        player.deathanim()
    gamescreen.blit(player.image,(int(player.rect.x-player.dimension[0])-player.rect.x+width/2,int(player.rect.y-player.dimension[1])))
    for enemy in enemies:
        if enemy.rect.y>height:
            enemies.remove(enemy)
        if(player.rect.x+width/2)>enemy.rect.x and(player.rect.x-width)<enemy.rect.x and not(enemy.death or enemy.deathstart or not enemy.spawned):
            if player.rect.x<enemy.rect.x:
                enemy.move(-2.5)
            else:
                enemy.move(2.5)
            if not enemy.onGround:
                enemy.move(dy=enemy.g)
                enemy.g+=0.25
            else:
                tempy=int(enemy.rect.y)
                enemy.rect.y=tempy+1
                for block in blocks:
                    if enemy.rect.colliderect(block.rect):
                        enemy.rect.y-=1
                        enemy.onGround=True
                if int(enemy.rect.y)!=tempy:
                    enemy.onGround=False
            for arrow in player.shots:
                try:
                    if enemy.rect.collidepoint(arrow[0]):
                        enemy.deathstart=True
                        enemy.deathtime=gamertime
                        enemy.deathdirection=enemy.direction
                        player.shots.remove(arrow)
                except:
                    pass
            gamescreen.blit(enemy.image,(int(enemy.rect.x-enemy.dimension[0])-player.rect.x+width/2,int(enemy.rect.y-enemy.dimension[1])))
        elif enemy.spawnstart and not(enemy.death or enemy.deathstart):
            enemy.spawning()
            gamescreen.blit(enemy.image,(int(enemy.rect.x-enemy.dimension[0])-player.rect.x+width/2,int(enemy.rect.y-enemy.dimension[1])))
        elif(player.rect.x+width/2)>enemy.rect.x and(player.rect.x-width)<enemy.rect.x and not(enemy.death or enemy.deathstart):
            enemy.spawnstart=True
            enemy.spawntime=gamertime
        elif enemy.deathstart:
            enemy.dies()
            gamescreen.blit(enemy.image,(int(enemy.rect.x-enemy.dimension[0])-player.rect.x+width/2,int(enemy.rect.y-enemy.dimension[1])))
        elif not((player.rect.x+width/2)>enemy.rect.x and(player.rect.x-width)<enemy.rect.x)and enemy.death:
            enemies.remove(enemy)
    try:
        del enemy
    except:
        pass
    try:
        player.fired()
    except:
        pass
    for arrow in player.arrows:
        if arrow[4]:
            if arrow[2]=="r":
                pygame.draw.rect(gamescreen,(220,20,60),pygame.Rect(arrow[0][0]-1+arrow[3]-player.rect.x,arrow[0][1]-1,4,4))
                pygame.draw.line(gamescreen,(160,82,45),(arrow[0][0]+arrow[3]-player.rect.x,arrow[0][1]),(arrow[1][0]+arrow[3]-player.rect.x,arrow[1][1]),2)
                pygame.draw.rect(gamescreen,(255,255,255),pygame.Rect(arrow[1][0]+arrow[3]-player.rect.x,arrow[1][1],2,2))
            else:
                pygame.draw.rect(gamescreen,(220,20,60),pygame.Rect(arrow[1][0]-1+arrow[3]-player.rect.x,arrow[1][1]-1,4,4))
                pygame.draw.line(gamescreen,(160,82,45),(arrow[0][0]+arrow[3]-player.rect.x,arrow[0][1]),(arrow[1][0]+arrow[3]-player.rect.x,arrow[1][1]),2)
                pygame.draw.rect(gamescreen,(255,255,255),pygame.Rect(arrow[0][0]+arrow[3]-player.rect.x,arrow[0][1],2,2))
    try:
        del arrow
    except:
        pass
    for background in backgrounds:
        if(player.rect.x+width/2)>background.x and(player.rect.x-width)<background.x:
            background.x-=player.rect.x-width/2
            pygame.draw.rect(gamescreen,(0,0,0),background)
            background.x+=player.rect.x-width/2
    try:
        del background
    except:
        pass
    for block in blocks:
        try:
            for arrow in player.shots:
                if block.rect.collidepoint(arrow[0]):
                    if arrow[1]=="r":
                        firstdrawpoint=((arrow[0][0]-18*math.cos(arrow[3]))-player.rect.x+width/2,(arrow[0][1]+18*math.sin(arrow[3])))
                        lastdrawpoint=((arrow[0][0]+2*math.cos(arrow[3]))-player.rect.x+width/2,arrow[0][1]-2*math.sin(arrow[3]))
                    else:
                        firstdrawpoint=((arrow[0][0]-2*math.cos(arrow[3]))-player.rect.x+width/2,arrow[0][1]-2*math.sin(arrow[3]))
                        lastdrawpoint=((arrow[0][0]+18*math.cos(arrow[3]))-player.rect.x+width/2,arrow[0][1]+18*math.sin(arrow[3]))
                    player.arrows.append((firstdrawpoint,lastdrawpoint,arrow[1],player.rect.x,random.choice([True,False])))
                    player.shots.remove(arrow)
        except:
            pass
        if(player.rect.x+width/2)>block.rect.x and(player.rect.x-width)<block.rect.x:
            gamescreen.blit(block.image,(int(block.rect.x-block.dimensions[0])-player.rect.x+width/2,int(block.rect.y-block.dimensions[1])))
    try:
        del block
    except:
        pass
    if user_input[pygame.K_LEFTBRACKET]and gamertime-volumetime>6:
        volume_change(False)
    if user_input[pygame.K_RIGHTBRACKET]and gamertime-volumetime>6:
        volume_change(True)
    gamescreen.blit(cursorimg,(int(mouse_pos[0]-2),int(mouse_pos[1]-2)))
    gamescreen.blit(testtextimg,(0,0))
    screen.blit(pygame.transform.scale(gamescreen,(screen_width,screen_height)),(0,0))
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
