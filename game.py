#============================ IMPORTS ============================
import tkinter as tk
from tkinter import *
from typing import Self
# from PIL import ImageTk, Image

#============================ CONSTANTS ============================

WINDOW_WIDTH=1420
WINDOW_HEIGHT=800
GRAVITY_FORCE = 9
JUMP_FORCE = 30
SPEED = 7
TIMED_LOOP = 6

#============================ VARIABLES ============================

keyPressed = []

#============================ GLOBAL ============================
score=0


#============================ MAIN WINDOW ============================
window = tk.Tk()
window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
window.title("ADVANTURE GAME")
frame = tk.Frame()
canvas = tk.Canvas(frame)

#============================ IMAGES ============================
start_img = PhotoImage(file="Images/start-button.png")
help_btn = PhotoImage(file="Images/help-button.png")
exit_img = PhotoImage(file="Images/exit-button.png")
home_bg = PhotoImage(file='Images/bg-defualt.png')
level_img = PhotoImage(file="Images/level.png")
winter_bg = PhotoImage(file="Images/summer1.png")
summer_bg = PhotoImage(file="Images/summer_bg.png")
back_img = PhotoImage(file="Images/back.png")
help_board = PhotoImage(file="Images/help.png")
grass_img = PhotoImage(file="Images/grass.png",)
stone_img = PhotoImage(file="Images/stone.png")
coin_img = PhotoImage(file="Images/coin.png")
door_img = PhotoImage(file="Images/door.png")
key_img = PhotoImage(file="Images/key.png")
flower_img = PhotoImage(file="Images/flower.png")
money_img = PhotoImage(file="Images/money.png")
thorn_img = PhotoImage(file="Images/thorn.png")
dimond_img = PhotoImage(file="Images/dimond.png")
monster_img = PhotoImage(file="Images/monster.png")
level3_bg = PhotoImage(file="Images/level3_bg.png")
player_img = PhotoImage(file="Images/player.png")
goldstone_img=PhotoImage(file="Images/goldstone.png")
worm_img=PhotoImage(file="Images/worm.png")
spring_bg=PhotoImage(file="Images/spring_bg.png")

#=========================== ALL LEVELS =======================

def level1(event):
    canvas.delete("all")
    global player
    # =============   GRASS IMAGES =========
    canvas.create_image(1, 0, image=summer_bg, anchor="nw")
    canvas.create_image(300,180, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(430,280, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(150,330, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(680,380, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(990,430, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(710,230, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(980,300, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(130,500, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(330,630, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(480,530, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(980,630, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(10,650, image = grass_img, anchor="nw", tags = "platform")
    # ==================  DOOR AND KEY IMAGE ===============
    canvas.create_image(380,100, image = door_img, anchor = "nw")
    canvas.create_image(1120,250, image = key_img, anchor = "nw")
    # ==================  STONE IMAGES ===============
    canvas.create_image(650,600, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(450,400, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(800,550, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(950,450, image = stone_img, anchor="nw", tags = "platform")
    # ==================  FLOWERS ===============
    canvas.create_image(950,200, image = flower_img, anchor = "nw")
    canvas.create_image(900,520, image = flower_img, anchor = "nw")
    canvas.create_image(100,390, image = flower_img, anchor = "nw")

    # ==================  COINS, DIMOND, THORN, MONEY ===============

    # _______ MONEY IMAGES _________
    canvas.create_image(240,280, image = money_img, anchor = 'nw')
    canvas.create_image(730,330, image = money_img, anchor = "nw")
    
    # _______ DIMOND IMAGES _________
    canvas.create_image(470,350, image = dimond_img, anchor = 'nw')
    canvas.create_image(820,500, image = dimond_img, anchor = 'nw')

    # _______ COIN IMAGES _________
    canvas.create_image(410,600, image = coin_img, anchor = 'nw')
    canvas.create_image(980,420, image = coin_img, anchor = 'nw')
    canvas.create_image(1170,380, image = coin_img, anchor = 'nw')

    # _______ MONSTER IMAGES _________
    canvas.create_image(270,450, image =monster_img, anchor = 'nw')
    canvas.create_image(510,240, image =monster_img, anchor = 'nw')
    canvas.create_image(800,340, image =monster_img, anchor = 'nw')

    # _______ THORN IMAGES _________
    canvas.create_image(770,130, image =thorn_img, anchor = 'nw')
    canvas.create_image(550,430, image =thorn_img, anchor = 'nw')
    canvas.create_image(1060,530, image =thorn_img, anchor = 'nw')

    # ==================  PLAYER ===============
    player = canvas.create_image(10,150, image =player_img, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")
    window.after(TIMED_LOOP, gravity)  
    
def level2(event):
    canvas.delete("all")
    canvas.create_image(1, 0, image=summer_bg, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")
    
    canvas.create_image(1, 0, image=spring_bg, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")
    canvas.create_image(700,410, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(710,200, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(200,430, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(0,500, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(310,550, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(310,300, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(10,700, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(450,410, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(10,330, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(550,275, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(620,530, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(510,110, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(890,480, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(890,100, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(900,320, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(1050,30, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(1000,210, image = goldstone_img, anchor="nw", tags = "platform")

# ==================  DOOR AND KEY IMAGE ===============
    canvas.create_image(1180,0, image = door_img, anchor = "nw")
    canvas.create_image(680,255, image = key_img, anchor = "nw")
# ==================  COINS, DIMOND, MONEY ===============
    canvas.create_image(370,300, image = coin_img, anchor = 'nw')
    canvas.create_image(600,110, image = coin_img, anchor = 'nw')
    canvas.create_image(290,430, image = coin_img, anchor = 'nw')
    canvas.create_image(720,530, image = coin_img, anchor = 'nw')
    canvas.create_image(610,270, image = coin_img, anchor = 'nw')
    canvas.create_image(760,200, image = coin_img, anchor = 'nw')
    canvas.create_image(980,100, image = coin_img, anchor = 'nw')
    canvas.create_image(790,410, image = coin_img, anchor = 'nw')

    canvas.create_image(1080,210, image = dimond_img, anchor = 'nw')
    canvas.create_image(530,410, image = dimond_img, anchor = 'nw')
# ==================  PLAYER ===============
    canvas.create_image(80,450, image =player_img, anchor = 'nw')
# ==================  ENEMY ===============
    canvas.create_image(420,255, image =worm_img, anchor = 'nw')
    canvas.create_image(90,290, image =worm_img, anchor = 'nw')
    canvas.create_image(390,510, image =worm_img, anchor = 'nw')
    canvas.create_image(820,160, image =worm_img, anchor = 'nw')
    canvas.create_image(960,440, image =worm_img, anchor = 'nw')
    canvas.create_image(960,280, image =worm_img, anchor = 'nw')

def level3(event):
    canvas.create_image(1, 0, image=level3_bg, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")


# ======================= HOME_PAGE =============================
def home():
    canvas.create_image(0,0, image=home_bg, anchor="nw")
    canvas.create_image(630, 300, image=start_img, anchor="nw", tags="start")
    canvas.create_image(630, 370, image=help_btn, anchor="nw", tags="help")
    canvas.create_image(630, 440, image=exit_img, anchor="nw", tags="exit")


# ======================= BACK TO LEVELS PAGE =============================
def backTolevel(event):
    allLevels()
def help(event):
    canvas.create_image(1, 0, image=winter_bg, anchor="nw")
    canvas.create_image(380,100, image = help_board, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
def start(event):
    allLevels()
def backHome(event):
    home()
#============================ EXIT ============================
def exit(event):
    window.destroy()

#============================ ALL LEVELS BUTTON ============================
def allLevels():
    
    canvas.create_image(1, 0, image=winter_bg, anchor="nw")
                            #==== LEVEL 1 =====
    canvas.create_image(620, 300, image=level_img, anchor="nw", tags="level1")
    canvas.create_text(695, 330, text="Level 1", font=("arsenal", 20, "bold"), fill="white",tags="level1")
                            #==== LEVEL 2 =====
    canvas.create_image(620, 370, image=level_img, anchor="nw", tags="level2")
    canvas.create_text(695, 400, text="Level 2", font=("arsenal", 23, "bold"), fill="white",tags="level2")
                            #==== LEVEL 3 =====
    canvas.create_image(620, 440, image=level_img, anchor="nw", tags="level3")
    canvas.create_text(695, 470, text="Level 3", font=("arsenal", 23, "bold"), fill="white",tags="level3")
                            #==== BACK BUTTON=====
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
    
#=========================== FUNCTIONS MOVE PLAYER =======================
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("platform")
    if coord[0] + dx < 0 or coord[1] + dy > WINDOW_WIDTH:
        return False
    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+ player_img.width(), coord[1] + player_img.height())
    else:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0]+ player_img.width(), coord[1] + player_img.height())
    print(overlap)
    for platform in platforms:
        if platform in overlap:
            return False
    return True
def jump(force):
    global player
    if force > 0:
        if check_movement(0, -force): 
            canvas.move(player, 0, -force)
    window.after(TIMED_LOOP, jump, force-1)
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        print(keyPressed)
        if len(keyPressed) == 1:
            move()
def move():
    global player
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            x -= SPEED
        if "Right" in keyPressed:
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):   
            jump(JUMP_FORCE)
        if not check_movement(x):
            canvas.move(player, x, 0)
            window.after(TIMED_LOOP, move)
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
        window.after(TIMED_LOOP, gravity)
def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)


#============================ KEY EVENT ============================
canvas.tag_bind("start","<Button-1>", start)
canvas.tag_bind("help","<Button-1>",help)


#========================= REMOTES =================
window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)
canvas.tag_bind("exit","<Button-1>", exit)
canvas.tag_bind("back_home","<Button-1>",backHome)
canvas.tag_bind("back_all_levels","<Button-1>",backTolevel)
canvas.tag_bind("level1","<Button-1>",level1)
canvas.tag_bind("level2","<Button-1>",level2)
canvas.tag_bind("level3","<Button-1>",level3)


home()

#========================= DISPLAY WINDOW =================
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()