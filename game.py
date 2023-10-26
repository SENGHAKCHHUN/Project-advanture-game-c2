#============================<<< IMPORTS >>>============================
import tkinter as tk
from tkinter import *
from typing import Self
from PIL import ImageTk, Image
from pygame import mixer
import time

#============================<<< VARIABLES >>>============================
keyPressed = []
isKey = False
isRun = False

#============================<<< GLOBAL >>>============================
score=0
dimond = 10
coin = 5
money = 5
x4 = 1

#============================<<< MAIN WINDOW >>>============================
window = tk.Tk()
window.title("ADVANTURE GAME")
frame = tk.Frame()
canvas = tk.Canvas(frame)

#============================<<< CONSTANTS >>>============================
WINDOW_WIDTH= window.winfo_screenwidth()
WINDOW_HEIGHT=window.winfo_screenheight()
window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
GRAVITY_FORCE = 9
JUMP_FORCE = 35
SPEED = 5
TIMED_LOOP = 6

#======================<<< SCROLLBAR BACKGROUND >>>=======================
scrollbar_bottom = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))

#======================<<< IMAGES >>>============================
home_img = Image.open("Images/bg-defualt.png")
home_resize = home_img.resize((WINDOW_WIDTH, WINDOW_HEIGHT))
home_bg = ImageTk.PhotoImage(home_resize)
all_levels_bg = Image.open("Images/bg-all-levels.png")
allLevels_resize = all_levels_bg.resize((WINDOW_WIDTH, WINDOW_HEIGHT))
allLevels_bg = ImageTk.PhotoImage(allLevels_resize)
lose_win_bg = Image.open("Images/lose-win-bg.png")
lose_win = lose_win_bg.resize((WINDOW_WIDTH, WINDOW_HEIGHT))
bg_lose_win = ImageTk.PhotoImage(lose_win)
rainy_bg = Image.open("Images/rainy.png")
rainy_img = rainy_bg.resize((WINDOW_WIDTH, WINDOW_HEIGHT))
rainy = ImageTk.PhotoImage(rainy_img)
start_img = PhotoImage(file="Images/start-button.png")
help_btn = PhotoImage(file="Images/help-button.png")
exit_img = PhotoImage(file="Images/exit-button.png")
level1_img = PhotoImage(file="Images/level1.png")
level2_img = PhotoImage(file="Images/level2.png")
level3_img = PhotoImage(file="Images/level3.png")
back_img = PhotoImage(file="Images/back.png")
help_board = PhotoImage(file="Images/help_board.png")
grass_img = PhotoImage(file="Images/grass.png")
stone_img = PhotoImage(file="Images/stone.png")
coin_img = PhotoImage(file="Images/coin.png")
door_img = PhotoImage(file="Images/door.png")
key_img = PhotoImage(file="Images/key.png")
flower_img = PhotoImage(file="Images/flower.png")
money_img = PhotoImage(file="Images/money.png")
thorn_img = PhotoImage(file="Images/thorn.png")
dimond_img = PhotoImage(file="Images/dimond.png")
monster_img = PhotoImage(file="Images/monster.png")
player_img = PhotoImage(file="Images/player.png")
goldstone_img=PhotoImage(file="Images/goldstone.png")
worm_img=PhotoImage(file="Images/worm.png")
spring_bg=PhotoImage(file="Images/spring_bg.png")
snow_bg = PhotoImage(file="Images/snow_bg.png")
ice_stone = PhotoImage(file="Images/ice_stone.png")
christmas_branch = PhotoImage(file="Images/Christmas_branch.png")
ice_thorn = PhotoImage(file="Images/ice_thorn.png")
present_png = PhotoImage(file="Images/present.png")
worm_img=PhotoImage(file="Images/worm.png")
spring_bg=PhotoImage(file="Images/spring_bg.png")
goldstone_img=PhotoImage(file="Images/goldstone.png")
lose_img = PhotoImage(file="Images/lose.png")
win_img = PhotoImage(file="Images/win.png")
player_left = PhotoImage(file="Images/player-turn-left.png")
ice_img = PhotoImage(file="Images/ice.png")
next_level = PhotoImage(file="Images/next.png")
grass_flower = PhotoImage(file="Images/flower-grass.png")
grass_l2 = PhotoImage(file="Images/grass-l2.png")
restart = PhotoImage(file="Images/restartgame.png")

#============================<< SCROLL BACKGROUND LEVEL 1 >>============================
def scroll_background():
    canvas.move(background1,-1,0)
    canvas.move(background2,-1,0)
    if canvas.coords(background1)[0]<-WINDOW_WIDTH:
        canvas.coords(background1,WINDOW_WIDTH,0)
    elif canvas.coords(background2)[0]<-WINDOW_WIDTH:
        canvas.coords(background2,WINDOW_WIDTH,0)
    canvas.after(5,scroll_background)
#==================<<< FUNCTION FOR CREATE IMGAGE ALL LEVELS >>>===================
def create_img_l1_p1():
    canvas.create_image(350,180, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(500,330, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(150,330, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(350,480, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(1100,430, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(800,280, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(1100,150, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(750,500, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(660,170, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(0,650, image = grass_flower, anchor="nw", tags = "platform")
    canvas.create_image(200,650, image = grass_flower, anchor="nw", tags = "platform") 
    canvas.create_image(390,650, image = grass_flower, anchor="nw", tags = "platform") 
    canvas.create_image(580,650, image = grass_flower, anchor="nw", tags = "platform") 
    canvas.create_image(770,650, image = grass_flower, anchor="nw", tags = "platform") 
    canvas.create_image(960,650, image = grass_flower, anchor="nw", tags = "platform") 
    canvas.create_image(1150,650, image = grass_flower, anchor="nw", tags = "platform") 
    canvas.create_image(380,100, image = door_img, anchor = "nw", tags = "door")
    canvas.create_image(900,250, image = key_img, anchor = "nw", tags = "key")
    canvas.create_image(150,600, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(650,500, image = stone_img, anchor="nw", tags = "platform")

def create_img_l1_p2():
    canvas.create_image(800,250, image = flower_img, anchor = "nw")
    canvas.create_image(800,470, image = flower_img, anchor = "nw")
    canvas.create_image(150,300, image = flower_img, anchor = "nw")
    canvas.create_image(150,600, image = flower_img, anchor = "nw")
    canvas.create_image(400,620, image = flower_img, anchor = "nw")
    canvas.create_image(1000,620, image = flower_img, anchor = "nw")
    canvas.create_image(800,620, image = flower_img, anchor = "nw")
    canvas.create_image(240,280, image = money_img, anchor = 'nw', tags = "money")
    canvas.create_image(730,600, image = money_img, anchor = "nw", tags = "money")
    canvas.create_image(400,420, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(1130,100, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(550,300, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(1100,390, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(1170,390, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(680,470, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(600,300, image =monster_img, anchor = 'nw', tags = "monster")
    canvas.create_image(1200,400, image =monster_img, anchor = 'nw', tags = "monster")
    canvas.create_image(1200,620, image =monster_img, anchor = 'nw', tags = "monster")
    canvas.create_image(1230,110, image =thorn_img, anchor = 'nw',  tags = "monster")
    canvas.create_image(470,610, image =thorn_img, anchor = 'nw', tags = "monster")

def create_img_l2_p1():
    canvas.create_image(350,180, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(500,330, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(150,330, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(350,480, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(1100,430, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(800,280, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(1100,150, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(750,500, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(660,170, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(0,665, image = grass_l2, anchor="nw", tags = "platform")
    canvas.create_image(190,665, image = grass_l2, anchor="nw", tags = "platform") 
    canvas.create_image(380,665, image = grass_l2, anchor="nw", tags = "platform") 
    canvas.create_image(570,665, image = grass_l2, anchor="nw", tags = "platform") 
    canvas.create_image(760,665, image = grass_l2, anchor="nw", tags = "platform") 
    canvas.create_image(950,665, image = grass_l2, anchor="nw", tags = "platform") 
    canvas.create_image(1140,665, image = grass_l2, anchor="nw", tags = "platform") 
    canvas.create_image(1330,665, image = grass_l2, anchor="nw", tags = "platform") 
    canvas.create_image(420,150, image = door_img, tags = "door")
    canvas.create_image(970,250, image = key_img, tags = "key")

def create_img_l2_p2():
    canvas.create_image(240,280, image = money_img, anchor = 'nw', tags = "money")
    canvas.create_image(730,600, image = money_img, anchor = "nw", tags = "money")
    canvas.create_image(120,600, image = money_img, anchor = "nw", tags = "money")
    canvas.create_image(400,420, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(1130,100, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(200,600, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(550,300, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(1100,390, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(1170,390, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(680,470, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(750,100, image =worm_img, anchor = 'nw', tags = "monster")
    canvas.create_image(135,270, image =worm_img, anchor = 'nw', tags = "monster")
    canvas.create_image(780,420, image =worm_img, anchor = 'nw', tags = "monster")
    canvas.create_image(780,200, image =worm_img, anchor = 'nw', tags = "monster")
    canvas.create_image(1100,580, image =worm_img, anchor = 'nw', tags = "monster")
    canvas.create_image(600,255, image =monster_img, anchor = 'nw', tags = "monster")

def create_img_l3_p1():
    canvas.create_image(280,150, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(830,250, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(120,610, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(350,550, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(1170,610, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(1100,280, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(640,570, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(1140,100, image = christmas_branch, anchor="nw", tags = "platform")
    canvas.create_image(90,350, image = christmas_branch, anchor="nw", tags = "platform")
    canvas.create_image(450,350, image = christmas_branch, anchor="nw", tags = "platform")
    canvas.create_image(0,730, image = christmas_branch, tags = "platform")
    canvas.create_image(200,730, image = christmas_branch, tags = "platform") 
    canvas.create_image(390,730, image = christmas_branch, tags = "platform") 
    canvas.create_image(490,100, image = christmas_branch, anchor="nw", tags = "platform") 
    canvas.create_image(580,730, image = christmas_branch, tags = "platform") 
    canvas.create_image(770,730, image = christmas_branch, tags = "platform") 
    canvas.create_image(960,730, image = christmas_branch, tags = "platform") 
    canvas.create_image(1150,730, image = christmas_branch, tags = "platform")
    canvas.create_image(850,500, image = christmas_branch, anchor="nw", tags = "platform")

def create_img_l3_p2():
    canvas.create_image(1250,60, image = door_img, anchor = 'nw', tags = "door")
    canvas.create_image(300,130, image = key_img, anchor = "nw", tags = "key")
    canvas.create_image(1030,470, image = money_img, anchor="nw", tags = "money")
    canvas.create_image(620,80, image = money_img, anchor="nw", tags = "money")
    canvas.create_image(400,520, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(1200,570, image =dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(280,325, image = present_png, anchor = 'nw', tags = "money")
    canvas.create_image(900,220, image = present_png, anchor = 'nw', tags = "money")
    canvas.create_image(650,350, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(680,550, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(850,470, image = ice_thorn, anchor="nw", tags = "monster")
    canvas.create_image(90,300, image = ice_thorn, anchor="nw", tags = "monster")
    canvas.create_image(460,300, image = ice_thorn, anchor = 'nw', tags = "monster")
    canvas.create_image(1140,230, image = ice_thorn, anchor = 'nw', tags = "monster")

#===========================<<< ALL LEVELS >>>=======================
    #================<<< LEVEL ONE >>>===================
def level1(event):
    canvas.delete("all")
    global background1, background2, player, score_id, levels_win_screen, score , play_again
    score = 0
    background1 = canvas.create_image(1, 0, image= rainy, anchor="nw")
    background2 = canvas.create_image(WINDOW_WIDTH, 0, image= rainy , anchor="nw")
    scroll_background()
    levels_win_screen = 0
    play_again = 0
    score_id = canvas.create_text(170, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)
    canvas.create_text(700,30, text="level one", font=("Robus", 50, "bold"), fill="red")         
    create_img_l1_p1()
    create_img_l1_p2()
    canvas.create_image(970,610, image =thorn_img, anchor = 'nw', tags = "monster")
    canvas.create_image(370,145, image =thorn_img, anchor = 'nw', tags = "monster")
    player = canvas.create_image(10,150, image =player_img)
    canvas.create_image(25, 5, image=back_img, anchor="nw", tags="back_all_levels")
    gravity()

    #===========================<<< LEVEL TWO >>>=======================
def level2(event):
    canvas.delete("all")
    global background1, background2, player, score_id, levels_win_screen, score, play_again
    score = 0
    background1 = canvas.create_image(1, 0, image= spring_bg, anchor="nw")
    background2 = canvas.create_image(WINDOW_WIDTH, 0, image= spring_bg, anchor="nw")
    scroll_background()
    levels_win_screen = 1
    play_again = 1
    score_id = canvas.create_text(170, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)
    canvas.create_text(700,30, text="level two", font=("Robus", 50, "bold"), fill="red")
    create_img_l2_p1()
    create_img_l2_p2()
    player = canvas.create_image(10,150, image =player_img)
    canvas.create_image(25, 5, image=back_img, anchor="nw", tags="back_all_levels")
    gravity() 

    #===========================<<< LEVEL THREE >>>=======================
def level3(event):
    canvas.delete("all")
    global background1, background2, player, score_id, score, play_again
    score = 0
    background1 = canvas.create_image(1, 0, image= snow_bg, anchor="nw")
    background2 = canvas.create_image(WINDOW_WIDTH, 0, image= snow_bg, anchor="nw")
    scroll_background()
    play_again = 2
    score_id = canvas.create_text(170, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)
    canvas.create_text(700,30, text="level three", font=("Robus", 50, "bold"), fill="red")
    create_img_l3_p1()
    create_img_l3_p2()
    player = canvas.create_image(10,150, image =player_img)
    canvas.create_image(25, 5, image=back_img, anchor="nw", tags="back_all_levels")
    gravity()  
   
# =======================<<< HOME PAGE >>>=============================
def home():
    canvas.create_image(0,0, image=home_bg, anchor="nw")
    canvas.create_image(550, 300, image=start_img, anchor="nw", tags="start")
    canvas.create_image(550, 420, image= help_btn, anchor="nw", tags="help")
    canvas.create_image(550, 540, image=exit_img, anchor="nw", tags="exit")

# =======================<<< BACK TO LEVELS PAGE >>>=============================
def backTolevel(event):
    allLevels()
def help(event):
    canvas.create_image(0,0, image=bg_lose_win , anchor="nw")
    canvas.create_image(380,120, image = help_board, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")

#=========<<< STARTS GAME >>>==========
def start(event):
    allLevels()

#=========<<< BACK HOME >>>=============
def backHome(event):
    home()

#==============<<< EXIT >>>=============
def exit(event):
    window.destroy()

#=============================<<< ALL LEVELS BUTTON >>>============================
def allLevels():
    canvas.create_image(1, 0, image=allLevels_bg , anchor="nw")  
    canvas.create_image(550, 300, image=level1_img, anchor="nw", tags="level1")          
    canvas.create_image(550, 420, image=level2_img, anchor="nw", tags="level2")        
    canvas.create_image(550, 540, image=level3_img, anchor="nw", tags="level3")        
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")

#=========================== LOSE =======================
def lose():
    canvas.delete("all")
    canvas.create_image(1,0, image = bg_lose_win ,anchor = "nw")
    canvas.create_image(700,350, image = lose_img)
    canvas.create_image(550,550, image = back_img, tags = "backgame")
    if play_again == 0:
        canvas.create_image(700,550, image = restart, tags = "level1")
    elif play_again == 1:
        canvas.create_image(700,550, image = restart, tags = "level2")
    elif play_again == 2:
        canvas.create_image(700,550, image = restart, tags = "level3")
    socre_id = canvas.create_text(750, 474, text=score, font=("arsenal", 25, "bold"), fill="black") 
    canvas.itemconfig(score_id, updatescore)
#=========================== WIN =======================
def win():
    if isKey and score > 24:
        canvas.delete("all")
        canvas.create_image(1,0, image = bg_lose_win, anchor = "nw")
        canvas.create_image(700, 350, image = win_img)
        canvas.create_image(550,550, image = back_img, tags = "backgame")
        if play_again == 0:
            canvas.create_image(700,550, image = restart, tags = "level1")
        elif play_again == 1:
            canvas.create_image(700,550, image = restart, tags = "level2")
        elif play_again == 2:
            canvas.create_image(700,550, image = restart, tags = "level3")
        socre_id = canvas.create_text(750, 474, text=score  , font=("arsenal", 25, "bold"), fill="black",) 
        if levels_win_screen == 0:
            canvas.create_image(850, 550, image = next_level, tags ="next_level1")
        elif levels_win_screen:
            canvas.create_image(850, 550, image = next_level, tags ="next_level2")
        canvas.itemconfig(score_id, updatescore)
       
def startSound():
    mixer.init() 
    mixer.music.load('Sounds/start.wav') 
    mixer.music.play()
    time.sleep(3)
#=========================== FUNCTIONS MOVE PLAYER =======================
    #======== CHECK MOVEMENT =========
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("platform")
    if coord[0] + dx < 0 or coord[1] + dx > WINDOW_WIDTH:
        return False
    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1] - 50) + player_img.height() + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+ dx, coord[1]+dy, coord[0]+ player_img.width() + dx, (coord[1] - 50) + player_img.height())
    for platform in platforms:
        if platform in overlap:
            return False
    return True

    #======== CHECK MOVEMENT MONSTER =========
def check_movement_monster():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("monster")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
         if platform in overlap:
           return platform
    return 0

    #======== CHECK MOVEMENT COIN =========
def check_movement_coin():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("coin")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0

    #======== CHECK MOVEMENT MONEY =========
def check_movement_money():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("money")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0

    #======== CHECK MOVEMENT DIMOND =========
def check_movement_dimond():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("dimond")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0

    #======== CHECK MOVEMENT KEY =========
def check_movement_key():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("key")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
    #======== CHECK MOVEMENT DOOR =========
def check_movement_door():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("door")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
    #======== CHECK MOVEMENT MONSTER =========
def check_movement_monster():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("monster")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0

#================= JUMP BY MOVING THE PLAYER UP BY FORECE PIXELS ===============
def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(TIMED_LOOP, jump, force-1)

#========================= START_MOVE =======================
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()

#========================= MOVE_PLAYER =======================
def move():
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            canvas.itemconfig(player, image = player_left)
            x -= SPEED
        if "Right" in keyPressed:
            canvas.itemconfig(player, image = player_img)
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(player, x, 0)
            window.after(TIMED_LOOP, move)
            check_more()

#======================= CHECK MORE MOVE ======================
def check_more():
    global score, coin , money, dimond, isKey, isRun
    monster_id = check_movement_monster()
    coin_id = check_movement_coin()
    money_id = check_movement_money()
    dimond_id = check_movement_dimond()
    key_id = check_movement_key()
    door_id = check_movement_door()
    if isRun:
        score = 0
        isKey = False 
        isRun = False
    elif monster_id > 0:
        lose()
    elif coin_id > 0:
        score += coin
        canvas.delete(coin_id)
        updatescore()
    elif money_id > 0:
        score += money
        canvas.delete(money_id)
        updatescore()
    elif dimond_id > 0:
        score += dimond
        canvas.delete(dimond_id)
        updatescore()
    elif key_id > 0:
        isKey = True
        canvas.delete(key_id)
    elif door_id > 0:
        
        win()

#============================ CHECK_PLAYER_MOVE ============================
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

#======================== STOP_MOVE AND REMOVE KEY =====================
def stop_move(event):
    global keyPressedgi
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

#============================ RESULT SCORE ============================
def updatescore():
    canvas.itemconfig(score_id,text="Score: " + str(score) )

#============================ KEY EVENT ===============================
window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)

#=============================== REMOTES =======================
canvas.tag_bind("start","<Button-1>", start)
canvas.tag_bind("help","<Button-1>", help)
canvas.tag_bind("exit","<Button-1>", exit)
canvas.tag_bind("back_home","<Button-1>",backHome)
canvas.tag_bind("backgame","<Button-1>",backTolevel)
canvas.tag_bind("back_all_levels","<Button-1>",backTolevel)
canvas.tag_bind("level1","<Button-1>",level1)
canvas.tag_bind("level2","<Button-1>",level2)
canvas.tag_bind("level3","<Button-1>",level3)
canvas.tag_bind("next_level1", "<Button-1>", level2)
canvas.tag_bind("next_level2", "<Button-1>", level3)

home()
startSound()
#========================= DISPLAY WINDOW =================
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()