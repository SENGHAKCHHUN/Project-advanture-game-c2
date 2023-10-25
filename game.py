#============================ IMPORTS ============================
import tkinter as tk
from tkinter import *
from typing import Self
from PIL import ImageTk, Image
from pygame import mixer
import time

#============================ VARIABLES ============================
keyPressed = []
isKey = False
isRun = False

#============================ GLOBAL ============================
score=0
dimond = 10
coin = 5
money = 5
x4 = 1

#============================ MAIN WINDOW ============================
window = tk.Tk()
window.title("ADVANTURE GAME")
frame = tk.Frame()
canvas = tk.Canvas(frame)

#============================ CONSTANTS ============================
WINDOW_WIDTH= window.winfo_screenwidth()
WINDOW_HEIGHT=window.winfo_screenheight()
window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
GRAVITY_FORCE = 9
JUMP_FORCE = 35
SPEED = 5
TIMED_LOOP = 6

#============================ SCROLLBAR BACKGROUND ============================
scrollbar_bottom = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')
window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))

#============================ IMAGES ============================
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
christmas_tree = PhotoImage(file="Images/Christmas_tree.png")
christmas_branch = PhotoImage(file="Images/Christmas_branch.png")
snow_house = PhotoImage(file="Images/snow_house.png")
monster_snow = PhotoImage(file="Images/monster_snow.png")
ice_thorn = PhotoImage(file="Images/ice_thorn.png")
present_png = PhotoImage(file="Images/present.png")
worm_img=PhotoImage(file="Images/worm.png")
spring_bg=PhotoImage(file="Images/spring_bg.png")
goldstone_img=PhotoImage(file="Images/goldstone.png")
lose_img = PhotoImage(file="Images/lose.png")
win_img = PhotoImage(file="Images/win.png")
player_left = PhotoImage(file="Images/player-turn-left.png")
ice_img = PhotoImage(file="Images/ice.png")
snow_monster = PhotoImage(file="Images/snow-monster.png")
next_level = PhotoImage(file="Images/next.png")

#============================ SCROLL BACKGROUND LEVEL 1 ============================
def scroll_background():
    canvas.move(background1,-1,0)
    canvas.move(background2,-1,0)
    if canvas.coords(background1)[0]<-WINDOW_WIDTH:
        canvas.coords(background1,WINDOW_WIDTH,0)
    elif canvas.coords(background2)[0]<-WINDOW_WIDTH:
        canvas.coords(background2,WINDOW_WIDTH,0)
    canvas.after(5,scroll_background)

#=========================== ALL LEVELS =======================
def level1(event):
    canvas.delete("all")
    global background1, background2, player, score_id
    score = 0
    background1 = canvas.create_image(1, 0, image= rainy, anchor="nw")
    background2 = canvas.create_image(WINDOW_WIDTH, 0, image= rainy , anchor="nw")
    scroll_background()

    score_id = canvas.create_text(170, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)
    
    # =============   GRASS IMAGES =========
    canvas.create_image(350,180, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(500,330, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(150,330, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(350,480, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(1100,430, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(800,280, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(1100,150, image = grass_img, anchor="nw", tags = "platform")

    canvas.create_image(750,500, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(660,170, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(0,650, image = grass_img, anchor="nw", tags = "platform")
    canvas.create_image(200,650, image = grass_img, anchor="nw", tags = "platform") 
    canvas.create_image(390,650, image = grass_img, anchor="nw", tags = "platform") 
    canvas.create_image(580,650, image = grass_img, anchor="nw", tags = "platform") 
    canvas.create_image(770,650, image = grass_img, anchor="nw", tags = "platform") 
    canvas.create_image(960,650, image = grass_img, anchor="nw", tags = "platform") 
    canvas.create_image(1150,650, image = grass_img, anchor="nw", tags = "platform") 

    # ==================  DOOR AND KEY IMAGE ===============
    canvas.create_image(380,100, image = door_img, anchor = "nw", tags = "door")
    canvas.create_image(900,250, image = key_img, anchor = "nw", tags = "key")

    # ==================  STONE IMAGES ===============
    canvas.create_image(150,600, image = stone_img, anchor="nw", tags = "platform")
    canvas.create_image(650,500, image = stone_img, anchor="nw", tags = "platform")

    # ==================  FLOWERS ===============
    canvas.create_image(800,250, image = flower_img, anchor = "nw")
    canvas.create_image(800,470, image = flower_img, anchor = "nw")
    canvas.create_image(150,300, image = flower_img, anchor = "nw")
    canvas.create_image(150,600, image = flower_img, anchor = "nw")
    canvas.create_image(400,620, image = flower_img, anchor = "nw")
    canvas.create_image(1000,620, image = flower_img, anchor = "nw")
    canvas.create_image(800,620, image = flower_img, anchor = "nw")

    # _______ MONEY IMAGES _________
    canvas.create_image(240,280, image = money_img, anchor = 'nw', tags = "money")
    canvas.create_image(730,600, image = money_img, anchor = "nw", tags = "money")
    
    # _______ DIMOND IMAGES _________
    canvas.create_image(400,420, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(1130,100, image = dimond_img, anchor = 'nw', tags = "dimond")

    # _______ COIN IMAGES _________
    canvas.create_image(550,300, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(1100,390, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(1170,390, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(680,470, image = coin_img, anchor = 'nw', tags = "coin")

    # _______ MONSTER IMAGES _________
    canvas.create_image(600,300, image =monster_img, anchor = 'nw', tags = "monster")
    canvas.create_image(1200,400, image =monster_img, anchor = 'nw', tags = "monster")
    canvas.create_image(1200,620, image =monster_img, anchor = 'nw', tags = "monster")

    # _______ THORN IMAGES _________
    canvas.create_image(1230,110, image =thorn_img, anchor = 'nw',  tags = "monster")
    canvas.create_image(470,610, image =thorn_img, anchor = 'nw', tags = "monster")
    canvas.create_image(970,610, image =thorn_img, anchor = 'nw', tags = "monster")
    canvas.create_image(370,145, image =thorn_img, anchor = 'nw', tags = "monster")

    # ==================  PLAYER ===============
    player = canvas.create_image(10,150, image =player_img)
    canvas.create_image(25, 5, image=back_img, anchor="nw", tags="back_all_levels")
    window.after(TIMED_LOOP, gravity)  

def level2(event):

    canvas.delete("all")
    global background1, background2, player, score_id
    score = 0
    background1 = canvas.create_image(1, 0, image= spring_bg, anchor="nw")
    background2 = canvas.create_image(WINDOW_WIDTH, 0, image= spring_bg, anchor="nw")
    scroll_background()
    score_id = canvas.create_text(170, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)
    
    # =============   GRASS IMAGES =========
    canvas.create_image(350,180, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(500,330, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(150,330, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(350,480, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(1100,430, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(800,280, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(1100,150, image = goldstone_img, anchor="nw", tags = "platform")

    canvas.create_image(750,500, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(660,170, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(0,650, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(200,650, image = goldstone_img, anchor="nw", tags = "platform") 
    canvas.create_image(390,650, image = goldstone_img, anchor="nw", tags = "platform") 
    canvas.create_image(580,650, image = goldstone_img, anchor="nw", tags = "platform") 
    canvas.create_image(770,650, image = goldstone_img, anchor="nw", tags = "platform") 
    canvas.create_image(960,650, image = goldstone_img, anchor="nw", tags = "platform") 
    canvas.create_image(1150,650, image = goldstone_img, anchor="nw", tags = "platform") 
    canvas.create_image(150,600, image = goldstone_img, anchor="nw", tags = "platform")
    canvas.create_image(650,500, image = goldstone_img, anchor="nw", tags = "platform")

    # ==================  DOOR AND KEY IMAGE ===============
    canvas.create_image(380,100, image = door_img, anchor = "nw", tags = "door")
    canvas.create_image(900,250, image = key_img, anchor = "nw", tags = "key")

    # _______ MONEY IMAGES _________
    canvas.create_image(240,280, image = money_img, anchor = 'nw', tags = "money")
    canvas.create_image(730,600, image = money_img, anchor = "nw", tags = "money")

    # _______ DIMOND IMAGES _________
    canvas.create_image(400,420, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(1130,100, image = dimond_img, anchor = 'nw', tags = "dimond")

    # _______ COIN IMAGES _________
    canvas.create_image(550,300, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(1100,390, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(1170,390, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(680,470, image = coin_img, anchor = 'nw', tags = "coin")

    canvas.create_image(750,125, image =worm_img, anchor = 'nw', tags = "monster")
    canvas.create_image(130,270, image =worm_img, anchor = 'nw', tags = "monster")
    canvas.create_image(780,420, image =worm_img, anchor = 'nw', tags = "monster")
    canvas.create_image(820,200, image =worm_img, anchor = 'nw', tags = "monster")
    canvas.create_image(1100,580, image =worm_img, anchor = 'nw', tags = "monster")
    canvas.create_image(600,255, image =monster_img, anchor = 'nw', tags = "monster")

    # ==================  PLAYER ===============
    player = canvas.create_image(10,150, image =player_img)
    canvas.create_image(25, 5, image=back_img, anchor="nw", tags="back_all_levels")
    window.after(TIMED_LOOP, gravity)  

def level3(event):
    canvas.delete("all")
    global background1, background2, player, score_id 
    score = 0
    background1 = canvas.create_image(1, 0, image= snow_bg, anchor="nw")
    background2 = canvas.create_image(WINDOW_WIDTH, 0, image= snow_bg, anchor="nw")
    scroll_background()
    score_id = canvas.create_text(170, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)
    
    # ==================  ICE_STONE ===============
    canvas.create_image(280,150, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(830,250, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(120,610, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(350,550, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(1170,610, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(1100,280, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(640,570, image = ice_stone, anchor="nw", tags = "platform")

    # ==================  CHRISTMAS_BRANCH ===============
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

    # ==================  DOOR & KEY ===============
    canvas.create_image(1250,60, image = door_img, anchor = 'nw', tags = "door")
    canvas.create_image(300,130, image = key_img, anchor = "nw", tags = "key")
    
    # ==================  MONEY ===============
    canvas.create_image(1030,470, image = money_img, anchor="nw", tags = "money")
    canvas.create_image(620,80, image = money_img, anchor="nw", tags = "money")

    # ==================  DIMOND ===============
    canvas.create_image(400,520, image = dimond_img, anchor = 'nw', tags = "dimond")
    canvas.create_image(1200,570, image =dimond_img, anchor = 'nw', tags = "dimond")

    # ==================  PRESENT ===============
    canvas.create_image(280,325, image = present_png, anchor = 'nw', tags = "money")
    canvas.create_image(900,220, image = present_png, anchor = 'nw', tags = "money")
    canvas.create_image(650,350, image = coin_img, anchor = 'nw', tags = "coin")
    canvas.create_image(680,550, image = coin_img, anchor = 'nw', tags = "coin")

    # ==================  ICE_THORN ===============
    canvas.create_image(850,470, image = ice_thorn, anchor="nw", tags = "monster")
    canvas.create_image(90,300, image = ice_thorn, anchor="nw", tags = "monster")
    canvas.create_image(460,300, image = ice_thorn, anchor = 'nw', tags = "monster")
    canvas.create_image(1140,230, image = ice_thorn, anchor = 'nw', tags = "monster")

    player = canvas.create_image(10,150, image =player_img)
    canvas.create_image(25, 5, image=back_img, anchor="nw", tags="back_all_levels")
    window.after(TIMED_LOOP, gravity)  
   
# ======================= HOME_PAGE =============================
def home():
    canvas.create_image(0,0, image=home_bg, anchor="nw")
    canvas.create_image(550, 300, image=start_img, anchor="nw", tags="start")
    canvas.create_image(550, 420, image= help_btn, anchor="nw", tags="help")
    canvas.create_image(550, 540, image=exit_img, anchor="nw", tags="exit")
    

# ======================= BACK TO LEVELS PAGE =============================
def backTolevel(event):
    allLevels()
def help(event):
    canvas.create_image(0,0, image=allLevels_bg , anchor="nw")
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
    canvas.create_image(1, 0, image=allLevels_bg , anchor="nw")  
    canvas.create_image(550, 300, image=level1_img, anchor="nw", tags="level1")          
    canvas.create_image(550, 420, image=level2_img, anchor="nw", tags="level2")        
    canvas.create_image(550, 540, image=level3_img, anchor="nw", tags="level3")        
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")


#=========================== SOUND =======================
def Start_Sound():
    mixer.init()
    mixer.music.load('Sounds/start.wav')
    mixer.music.play()
    time.sleep(4)
    mixer.music.stop()

def Lose_Sound():
    mixer.init() 
    mixer.music.load('Sounds/lose.wav') 
    mixer.music.play() 
    time.sleep(3)
    mixer.music.stop()

def Win_Sound():
    mixer.init() 
    mixer.music.load('Sounds/win.mp3') 
    mixer.music.play()
    time.sleep(3)
    mixer.music.stop()

def Eat_Sound():
    mixer.init() 
    mixer.music.load('Sounds/eat.mp3') 
    mixer.music.play()
    
def Eat_Sound():
    mixer.init() 
    mixer.music.load('Sounds/eat.mp3') 
    mixer.music.play()

#=========================== LOSE AND WIN =======================
def lose():
    canvas.delete("all")
    Lose_Sound()
    canvas.create_image(1,0, image = bg_lose_win ,anchor = "nw")
    canvas.create_image(700,350, image = lose_img)
    canvas.create_image(550,550, image = back_img, tags = "backgame")
    socre_id = canvas.create_text(750, 474, text=score, font=("arsenal", 25, "bold"), fill="black") 
    canvas.itemconfig(score_id, updatescore)
    
def win():
    if isKey and score > 24:
        canvas.delete("all")
        Win_Sound()
        canvas.create_image(1,0, image = bg_lose_win, anchor = "nw")
        canvas.create_image(700, 350, image = win_img)
        canvas.create_image(550,550, image = back_img, tags = "backgame")
        socre_id = canvas.create_text(750, 474, text=score, font=("arsenal", 25, "bold"), fill="black",) 
        canvas.itemconfig(score_id, updatescore)

        canvas.create_image(900, 474, image = next_level, tags ="next_level1")

       
#=========================== FUNCTIONS MOVE PLAYER =======================
def check_movement(dx=0, dy=0, checkGround=False):
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("platform")
    if coord[0] + dx < 0 or coord[1] + dx > WINDOW_WIDTH:
        return False
    if checkGround:
        overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1] - 50) + player_img.height() + dy)
    else:
        overlap = canvas.find_overlapping(coord[0]+dx, coord[1]+dy, coord[0]+ player_img.width() + dx, (coord[1] - 50) + player_img.height())
    for platform in platforms:
        if platform in overlap:
            return False
    return True
def check_movement_monster():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("monster")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
def check_movement_coin():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("coin")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
def check_movement_money():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("money")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
def check_movement_dimond():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("dimond")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
def check_movement_key():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("key")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
def check_movement_door():
    coord = canvas.coords(player)
    platforms = canvas.find_withtag("door")
    overlap = canvas.find_overlapping(coord[0], coord[1], coord[0] + player_img.width(), (coord[1]) + player_img.height())    
    for platform in platforms:
        if platform in overlap:
            return platform
    return 0
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
        isRun = False
    if monster_id > 0:
        isRun = True
        lose()
    if coin_id > 0:
        score += coin
        Eat_Sound()
        canvas.delete(coin_id)
        updatescore()
    if money_id > 0:
        score += money
        Eat_Sound()
        canvas.delete(money_id)
        updatescore()
    if dimond_id > 0:
        score += dimond
        Eat_Sound()
        canvas.delete(dimond_id)
        updatescore()
    if key_id > 0:
        isKey = True
        Eat_Sound()
        canvas.delete(key_id)
        print("ok")
    if door_id > 0:
        win()

#============================ CHECK_PLAYER_MOVE ============================
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

#======================== STOP_MOVE AND REMOVE KEY =====================
def stop_move(event):
    global keyPressed
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
home()

#========================= DISPLAY WINDOW =================
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()
