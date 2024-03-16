import pygame
import time
from random import randint

def bullet_move(bullet_khung_list):
    if bullet_khung_list:
        for bullet_rect in bullet_khung_list:
            bullet_rect.x-=7
            screen.blit(bullet_surface,bullet_rect)
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
pygame.display.set_caption("Run")
clock=pygame.time.Clock()
bg=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\bg.png").convert() #Load ảnh backgroud

#Add player
player=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\player.png").convert_alpha() #Load ảnh player
player_surface=player
player_jump=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\player_jump.png").convert_alpha() #Load ảnh player nhảy
player_jump_2=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\player_jump_2.png")

#Add bullets
bullet_down=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\bullet_down.png").convert_alpha() #Load ảnh đạn dưới
bullet_surface=bullet_down
bullet_khung_list=[]

#Thêm thời gian
bullet_timer=pygame.USEREVENT+1
pygame.time.set_timer(bullet_timer,1500)

#Chữ
font=pygame.font.Font("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\Pixel Sans Serif Condensed.TTF",36) #Gọi font chữ
game_name=font.render("DODGE BULLETS",False,(255,0,255))
game_hd=font.render("Press space to restart",False,(255,0,0))

#Tạo khung bao quanh đối tượng
player_khung=player_surface.get_rect(midbottom=(70,291))
player_khung_2=player_jump_2.get_rect(midbottom=(70,291))
bullet_khung=bullet_surface.get_rect(bottomleft=(800,285))
game_name_khung=game_name.get_rect(topleft=(200,0))
game_hd_khung=game_hd.get_rect(midbottom=(400,400))

#Trọng lực
player_graviy=0

#Thêm nhạc nền
bg_music=pygame.mixer.Sound("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\bg_music.mp3")
bg_music.play(loops=-1)
bg_music.set_volume(0.1)

game_active=False

while True:
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
                    jump_sound=pygame.mixer.Sound("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\jump_sound.mp3")
                    jump_sound.play()
                '''elif ev.key==pygame.K_DOWN:
                    player=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\player_sit.png").convert_alpha()
                    player_khung=player.get_rect(midbottom=(70,291))
            elif ev.type==pygame.KEYUP:
                player=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\player.png").convert_alpha()
                player_khung=player.get_rect(midbottom=(70,291))'''
            if ev.type==bullet_timer:
                bullet_khung_list.append(bullet_surface.get_rect(bottomleft=(randint(900,1500),285)))
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
        if player_khung.top>=209:player_khung.top=209 #Đứng trên mặt đất
        screen.blit(player_surface,player_khung) #Đặt player

        #Đặt chữ
        screen.blit(game_name,game_name_khung) #Dặt tên game
        
        #Đạn
        bullet_move(bullet_khung_list)
        
        #Va chạm
        game_active=vacham(player_khung,bullet_khung_list)

    else:
        screen.blit(pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\game_over.png"),(0,0))
        screen.blit(game_hd,game_hd_khung)

        #Xoá list bullet khi chết
        bullet_khung_list.clear()
        
    pygame.display.update()
    clock.tick(60)