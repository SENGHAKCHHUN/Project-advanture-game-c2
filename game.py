#============================ IMPORTS ============================
import tkinter as tk
from tkinter import *
from typing import Self
# from PIL import ImageTk, Image

#============================ CONSTANTS ============================

WINDOW_WIDTH=1420
WINDOW_HEIGHT=800
GRAVITY_FORCE = 9
JUMP_FORCE = 35
SPEED = 7
TIMED_LOOP = 6

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
window.geometry(str(WINDOW_WIDTH)+"x"+str(WINDOW_HEIGHT))
window.title("ADVANTURE GAME")
frame = tk.Frame()
canvas = tk.Canvas(frame)
#============================ SCROLLAR ============================

scrollbar_bottom = tk.Scrollbar(window, orient='horizontal', command=canvas.xview)
canvas.configure(xscrollcommand=scrollbar_bottom.set)
scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')
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
back_game = PhotoImage(file="Images/back_result.png")


#============================ SCROLL BACKGROUND LEVEL 1 ============================

def scroll_background():
    canvas.move(background1,-1,0)
    canvas.move(background2,-1,0)
    if canvas.coords(background1)[0]<-1420:
        canvas.coords(background1,1420,0)
    elif canvas.coords(background2)[0]<-1420:
        canvas.coords(background2,1420,0)
    canvas.after(5,scroll_background)


#=========================== ALL LEVELS =======================

def level1(event):
    canvas.delete("all")
    global background1
    global background2
    global player
    global score_id
    score = 0
    background1 = canvas.create_image(1, 0, image= summer_bg, anchor="nw")
    background2 = canvas.create_image(WINDOW_WIDTH, 0, image= summer_bg, anchor="nw")
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
    # canvas.create_image(350,450, image =monster_img, anchor = 'nw',  tags = "monster")
    canvas.create_image(600,300, image =monster_img, anchor = 'nw', tags = "monster")
    canvas.create_image(1200,400, image =monster_img, anchor = 'nw', tags = "monster")
    canvas.create_image(1200,620, image =monster_img, anchor = 'nw', tags = "monster")
    # canvas.create_image(260,620, image =monster_img, anchor = 'nw', tags = "monster")
    # canvas.create_image(570,620, image =monster_img, anchor = 'nw', tags = "monster")
    # canvas.create_image(920,250, image =monster_img, anchor = 'nw', tags = "monster")

    # _______ THORN IMAGES _________
    canvas.create_image(1230,110, image =thorn_img, anchor = 'nw',  tags = "monster")
    canvas.create_image(470,610, image =thorn_img, anchor = 'nw', tags = "monster")
    canvas.create_image(970,610, image =thorn_img, anchor = 'nw', tags = "monster")
    canvas.create_image(370,145, image =thorn_img, anchor = 'nw', tags = "monster")

    # ==================  PLAYER ===============
    player = canvas.create_image(10,150, image =player_img, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")
    window.after(TIMED_LOOP, gravity)  

def level2(event):
    canvas.delete("all")
    global background1
    global background2
    global player
    global score_id
    score = 0
    background1 = canvas.create_image(1, 0, image= spring_bg, anchor="nw")
    background2 = canvas.create_image(WINDOW_WIDTH, 0, image= spring_bg, anchor="nw")
    scroll_background()
    score_id = canvas.create_text(170, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)
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
    canvas.create_image(680,295, image = key_img, anchor = "nw")
# ==================  COINS, DIMOND, MONEY ===============
    canvas.create_image(370,315, image = coin_img, anchor = 'nw')
    canvas.create_image(600,130, image = coin_img, anchor = 'nw')
    canvas.create_image(290,450, image = coin_img, anchor = 'nw')
    canvas.create_image(720,550, image = coin_img, anchor = 'nw')
    canvas.create_image(610,290, image = coin_img, anchor = 'nw')
    canvas.create_image(770,220, image = coin_img, anchor = 'nw')
    canvas.create_image(980,120, image = coin_img, anchor = 'nw')
    canvas.create_image(790,430, image = coin_img, anchor = 'nw')

    canvas.create_image(1080,210, image = dimond_img, anchor = 'nw')
    canvas.create_image(530,410, image = dimond_img, anchor = 'nw')

# ==================  ENEMY ===============
    canvas.create_image(420,255, image =worm_img, anchor = 'nw')
    canvas.create_image(90,290, image =worm_img, anchor = 'nw')
    canvas.create_image(390,510, image =worm_img, anchor = 'nw')
    canvas.create_image(820,160, image =worm_img, anchor = 'nw')
    canvas.create_image(960,440, image =worm_img, anchor = 'nw')
    canvas.create_image(960,280, image =worm_img, anchor = 'nw')

    player = canvas.create_image(10,150, image =player_img, anchor="nw")
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")
    score_id = canvas.create_text(170, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)
    window.after(TIMED_LOOP, gravity) 

def level3(event):
    canvas.delete("all")
    global background1
    global background2
    global player
    global score_id
    score = 0
    background1 = canvas.create_image(1, 0, image= snow_bg, anchor="nw")
    background2 = canvas.create_image(WINDOW_WIDTH, 0, image= snow_bg, anchor="nw")
    scroll_background()
    score_id = canvas.create_text(170, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)

    # =============   ICE_STONE​​ IMAGE  =========

    canvas.create_image(200,100, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(300,330, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(350,550, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(100,600, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(700,400, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(900,100, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(1030,350, image = ice_stone, anchor="nw", tags = "platform")
    canvas.create_image(800,600, image = ice_stone, anchor="nw", tags = "platform")    
    # ==================  DOOR AND KEY IMAGE ===============
    canvas.create_image(1300,40, image = door_img, anchor = "nw", tags = "door")
    canvas.create_image(320,80, image = key_img, anchor = "nw", tags = "key")
    # ==================  CHRISTMAS_BRANCH IMAGES ===============
    canvas.create_image(500,100, image = christmas_branch, anchor="nw", tags = "platform")
    canvas.create_image(0,620, image = christmas_branch, anchor="nw", tags = "platform")
    canvas.create_image(500,620, image = christmas_branch, anchor="nw", tags = "platform")
    canvas.create_image(500,620, image = christmas_branch, anchor="nw", tags = "platform")
    canvas.create_image(1150,50, image = christmas_branch, anchor="nw", tags = "platform")
    # canvas.create_image(740,380, image = christmas_branch, anchor="nw", tags = "platform")
    # canvas.create_image(1100,380, image = christmas_branch, anchor="nw", tags = "platform")
    # ==================  CHRISTMAS_TREE IMAGE ===============
    # canvas.create_image(550,360, image = christmas_tree, anchor="nw", tags = "platform")
    # canvas.create_image(500,560, image = christmas_tree, anchor="nw", tags = "platform")
    # canvas.create_image(900,550, image = christmas_tree, anchor="nw", tags = "platform")

    # ==================  COINS, DIMOND, ICE_THORN, PRESENT, MONEY ===============

    # canvas.create_image(80,410, image = monster_img, anchor = 'nw', tags = "monster")
    # canvas.create_image(740,500, image = monster_img, anchor = 'nw', tags = "monster")
    # canvas.create_image(880,400, image = monster_img, anchor = 'nw', tags = "monster")
    # canvas.create_image(650,700, image = monster_img, anchor = 'nw', tags = "monster")
    # canvas.create_image(1080,700, image = monster_img, anchor = 'nw', tags = "monster")
    # canvas.create_image(500,4, image = monster_snow, anchor = 'nw', tags = "monster")
    # canvas.create_image(15,140, image = monster_snow, anchor = 'nw', tags = "monster")
    # canvas.create_image(500,4, image = monster_snow, anchor = 'nw', tags = "monster")
    # canvas.create_image(320,250, image = monster_snow, anchor = 'nw', tags = "monster")
    # canvas.create_image(1040,220, image = ice_thorn, anchor = 'nw', tags = "monster")
    # canvas.create_image(1150,550, image = ice_thorn, anchor = 'nw', tags = "monster")
    
    # canvas.create_image(200,200, image = present_png, anchor = 'nw', tags = "money")
    # canvas.create_image(630,250, image = present_png, anchor = 'nw', tags = "money")
    # canvas.create_image(370,450, image = present_png, anchor = 'nw', tags = "money")
    # canvas.create_image(1250,400, image = present_png, anchor = 'nw', tags = "money")

    # canvas.create_image(950,60, image = coin_img, anchor = 'nw', tags = "coin")
    # canvas.create_image(800,400, image = coin_img, anchor = 'nw', tags = "coin")
    # canvas.create_image(990,700, image = coin_img, anchor = 'nw', tags = "coin")
    # canvas.create_image(320,660, image = coin_img, anchor = 'nw', tags = "coin")

    # canvas.create_image(660,60, image = dimond_img, anchor = 'nw', tags = "dimond")
    # canvas.create_image(180,410, image = dimond_img, anchor = 'nw', tags = "dimond")
    # canvas.create_image(640,500, image = dimond_img, anchor = 'nw', tags = "dimond")
    # canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")

    # player = canvas.create_image(10,150, image =player_img, anchor="nw")
    # canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_all_levels")
    # score_id = canvas.create_text(170, 50, text=" score : " + str(score), font=("arsenal", 20, "bold"), fill="white",)
    # window.after(TIMED_LOOP, gravity) 

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
    canvas.create_image(620, 300, image=level_img, anchor="nw", tags="level1")
    canvas.create_text(695, 330, text="Level 1", font=("arsenal", 20, "bold"), fill="white",tags="level1")             
    canvas.create_image(620, 370, image=level_img, anchor="nw", tags="level2")
    canvas.create_text(695, 400, text="Level 2", font=("arsenal", 23, "bold"), fill="white",tags="level2")         
    canvas.create_image(620, 440, image=level_img, anchor="nw", tags="level3")
    canvas.create_text(695, 470, text="Level 3", font=("arsenal", 23, "bold"), fill="white",tags="level3")         
    canvas.create_image(25, 10, image=back_img, anchor="nw", tags="back_home")
    
# def moveturtle4():
#     global x4
#     canvas.move('monster', x4, 0)
#     (leftPos, topPos, rightPos, bottomPos) = canvas.bbox('monster')
#     if leftPos <= 1850 or rightPos >= 2150:
#         x4 = -x4
#     canvas.after(30, moveturtle4)
# canvas.after(30, moveturtle4)

#=========================== LOSE AND WIN =======================
def lose():
    canvas.delete("all")
    canvas.create_image(1,0, image = winter_bg ,anchor = "nw")
    canvas.create_image(700,350, image = lose_img)
    canvas.create_image(550,550, image = back_game, tags = "backgame")
    socre_id = canvas.create_text(750, 474, text=score, font=("arsenal", 25, "bold"), fill="black") 
    canvas.itemconfig(score_id, updatescore)
    
def win():
    if isKey and score > 25:
        canvas.delete("all")
        canvas.create_image(1,0, image = winter_bg, anchor = "nw")
        canvas.create_image(700, 350, image = win_img)
        canvas.create_image(550,550, image = back_game, tags = "backgame")
        socre_id = canvas.create_text(750, 474, text=score, font=("arsenal", 25, "bold"), fill="black",) 
        canvas.itemconfig(score_id, updatescore)
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
# -----------------------Jump by moving the player up by force pixels-----------------------------
def jump(force):
    if force > 0:
        if check_movement(0, -force):
            canvas.move(player, 0, -force)
            window.after(TIMED_LOOP, jump, force-1)
# ----------------start_move------------------------
def start_move(event):
    if event.keysym not in keyPressed:
        keyPressed.append(event.keysym)
        if len(keyPressed) == 1:
            move()
#---------------Move_object----------------------------------
def move():
    global score
    global coin
    global money
    global dimond
    global isKey
    global isRun
    if not keyPressed == []:
        x = 0
        if "Left" in keyPressed:
            x -= SPEED
        if "Right" in keyPressed:
            x += SPEED
        if "space" in keyPressed and not check_movement(0, GRAVITY_FORCE, True):
            jump(JUMP_FORCE)
        if check_movement(x):
            canvas.move(player, x, 0)
            window.after(TIMED_LOOP, move)
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
            canvas.delete(coin_id)
            updatescore()
        if money_id > 0:
            score += money
            canvas.delete(money_id)
            updatescore()
        if dimond_id > 0:
            score += dimond
            canvas.delete(dimond_id)
            updatescore()
        if key_id > 0:
            isKey = True
            canvas.delete(key_id)
            print("ok")
        if door_id > 0:
            win()
#--------check_player_move---------------------
def gravity():
    if check_movement(0, GRAVITY_FORCE, True):
        canvas.move(player, 0, GRAVITY_FORCE)
    window.after(TIMED_LOOP, gravity)

#--------------stop_move and remove key------------------------
def stop_move(event):
    global keyPressed
    if event.keysym in keyPressed:
        keyPressed.remove(event.keysym)

#============================ RESULT SCORE ============================
def updatescore():
    canvas.itemconfig(score_id,text="Score: " + str(score) )

#============================ KEY EVENT ============================
window.bind("<Key>", start_move)
window.bind("<KeyRelease>", stop_move)
#========================= REMOTES =================

canvas.tag_bind("start","<Button-1>", start)
canvas.tag_bind("help","<Button-1>",help)
canvas.tag_bind("exit","<Button-1>", exit)
canvas.tag_bind("back_home","<Button-1>",backHome)
canvas.tag_bind("backgame","<Button-1>",backTolevel)
canvas.tag_bind("back_all_levels","<Button-1>",backTolevel)
canvas.tag_bind("level1","<Button-1>",level1)
canvas.tag_bind("level2","<Button-1>",level2)
canvas.tag_bind("level3","<Button-1>",level3)
home()
#========================= DISPLAY WINDOW =================
canvas.pack(expand=True, fill="both")
frame.pack(expand=True, fill="both")
window.mainloop()