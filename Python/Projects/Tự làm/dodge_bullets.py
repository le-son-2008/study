import pygame
from random import randint

s=0
n=True
t=[]

def bullet_move(bullet_khung_list,bullet):
    if bullet_khung_list:
        for bullet_rect in bullet_khung_list:
            bullet_rect.x-=7
            screen.blit(bullet,bullet_rect)
            if bullet_rect.x<=-100:
                bullet_khung_list.remove(bullet_rect)
def vacham(player_khung,bullet_khung_list):
    if bullet_khung_list:
        for bullet_rect in bullet_khung_list:
            if player_khung.colliderect(bullet_rect):
                return False
    return True
    
pygame.init() #Khởi tạo tất cả mô-đun pygame -->Gọi ra đầu tiên
screen=pygame.display.set_mode((800,400)) #Khởi tạo mô-đun hiển thị (rộng,cao)
pygame.display.set_caption("Dodge bullets")
clock=pygame.time.Clock()
stand=pygame.image.load("C:\\Users\\Administrator\\OneDrive\\Code\\Python\\Pygame\\Game\\stand.png").convert() #Load ảnh ban đầu
bg=pygame.image.load("C:\\Users\\Administrator\\OneDrive\\Code\\Python\\Pygame\\Game\\bg.png").convert() #Load ảnh backgroud

#Add player
player=pygame.image.load("C:\\Users\\Administrator\\OneDrive\\Code\\Python\\Pygame\\Game\\player.png").convert_alpha() #Load ảnh player
player_surface=player
player_jump=pygame.image.load("C:\\Users\\Administrator\\OneDrive\\Code\\Python\\Pygame\\Game\\player_jump.png").convert_alpha() #Load ảnh player nhảy
player_jump_2=pygame.image.load("C:\\Users\\Administrator\\OneDrive\\Code\\Python\\Pygame\\Game\\player_jump_2.png")

#Add bullets
bullet_down=pygame.image.load("C:\\Users\\Administrator\\OneDrive\\Code\\Python\\Pygame\\Game\\bullet_down.png").convert_alpha() #Load ảnh đạn dưới
bullet_down_khung_list=[]
bullet_up=pygame.image.load("C:\\Users\\Administrator\\OneDrive\\Code\\Python\\Pygame\\Game\\bullet_up.png").convert_alpha() #Load ảnh đạn trên
bullet_up_khung_list=[]

#Thêm thời gian
bullet_timer=pygame.USEREVENT+1
pygame.time.set_timer(bullet_timer,1500)

#Chữ
font=pygame.font.Font("C:\\Users\\Administrator\\OneDrive\\Code\\Python\\Pygame\\Game\\Pixel Sans Serif Condensed.TTF",36) #Gọi font chữ
font_2=pygame.font.Font("C:\\Users\\Administrator\\OneDrive\\Code\\Python\\Pygame\\Game\\SVN-Retron 2000.TTF",24)
game_name=font.render("DODGE BULLETS",False,(255,0,255)) #Tên game đã vào game
game_hd=font.render("Press space to start",False,(255,0,0)) #Hướng dẫn
game_hd_2=font.render("Press space to restart",False,(255,0,0))

#Tạo khung bao quanh đối tượng
player_khung=player_surface.get_rect(midbottom=(70,291))
player_khung_2=player_jump_2.get_rect(midbottom=(70,291))
bullet_khung=bullet_down.get_rect(bottomleft=(800,285))
game_name_khung=game_name.get_rect(topleft=(0,-10))
game_hd_khung=game_hd.get_rect(midbottom=(400,400))

def restart(x,a=game_hd,b=game_hd_khung):
    global n
    if n==True:
        screen.blit(a,b)
        n=False
    else:
        n=True
        
#Trọng lực
player_graviy=0

#Màn hình chờ vào game
game_active=None
while game_active==None:
    screen.blit(stand,(0,0))
    restart(n)
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            pygame.quit()
            exit()
        if ev.type==pygame.KEYDOWN and ev.key==pygame.K_SPACE:
            game_active=True
            break
    pygame.display.update()
    clock.tick(20)

#Thêm nhạc nền
bg_music=pygame.mixer.Sound("C:\\Users\\Administrator\\OneDrive\\Code\\Python\\Pygame\\Game\\bg_music.mp3")
bg_music.play(loops=-1)
bg_music.set_volume(0.1)

while True:

    #Điểm số
    score=font_2.render(f"Score:{s}",True,(255,255,0)) 
    score_khung=score.get_rect(topleft=(0,40))
    s+=1

    for ev in pygame.event.get():

        #Thoát khi bấm X trên màn hình
        if ev.type==pygame.QUIT:
            pygame.quit()
            exit()

        #Check phím bấm
        if game_active:
            if ev.type==pygame.KEYDOWN:
                if ev.key==pygame.K_SPACE and player_khung.bottom>=291:
                    player_graviy=-14
                    jump_sound=pygame.mixer.Sound("C:\\Users\\Administrator\\OneDrive\\Code\\Python\\Pygame\\Game\\jump_sound.mp3")
                    jump_sound.play()
                if ev.key==pygame.K_DOWN:
                    player=pygame.image.load("C:\\Users\\Administrator\\OneDrive\\Code\\Python\\Pygame\\Game\\player_sit.png").convert_alpha()
            if ev.type==pygame.KEYUP:
                player=pygame.image.load("C:\\Users\\Administrator\\OneDrive\\Code\\Python\\Pygame\\Game\\player.png").convert_alpha()
            
            if ev.type==bullet_timer:
                bullet_down_khung_list.append(bullet_down.get_rect(bottomleft=(randint(900,1300),285)))
                if s>=500:bullet_up_khung_list.append(bullet_up.get_rect(bottomleft=(randint(2000,2100),219)))

        else:
            if ev.type==pygame.KEYDOWN and ev.key==pygame.K_SPACE:
                game_active=True
                bullet_khung.bottomleft=(800,285)

    if game_active:
        screen.blit(bg,(0,0)) #Đặt background

        #Player
        if player_khung.top<209:
            player_surface=player_jump
            player_khung=player_khung_2
        else:
            player_surface=player
            player_khung=player_surface.get_rect(midbottom=(70,291))
        player_graviy+=1
        player_khung.y+=player_graviy
        if player_khung.bottom>=291:player_khung.bottom=291 #Đứng trên mặt đất
        screen.blit(player_surface,player_khung) #Đặt player

        #Đặt chữ
        screen.blit(game_name,game_name_khung) #Dặt tên game
        screen.blit(score,score_khung) #Dặt điểm số

        #Đạn
        bullet_move(bullet_down_khung_list,bullet_down)
        bullet_move(bullet_up_khung_list,bullet_up)
        
        #Va chạm
        game_active=vacham(player_khung,bullet_down_khung_list) and vacham(player_khung,bullet_up_khung_list)
       
    else:

        #Game over
        screen.blit(pygame.image.load("C:\\Users\\Administrator\\OneDrive\\Code\\Python\\Pygame\\Game\\game_over.png"),(0,0))
        screen.blit(game_hd_2,game_hd_khung) #Đặt restart game
        s=0
        
        #Xoá list bullet khi chết
        bullet_down_khung_list.clear()
        bullet_up_khung_list.clear()



    pygame.display.update()
    clock.tick(60)