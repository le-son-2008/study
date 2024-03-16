import pygame
import time

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
#Add enemies
bullet_down=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\bullet_down.png").convert_alpha() #Load ảnh đạn dưới
bullet_surface=bullet_down
#Chữ
font=pygame.font.Font("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\Pixel Sans Serif Condensed.TTF",36) #Gọi font chữ
game_name=font.render("DODGE BULLETS",False,(255,0,255))
game_hd=font.render("Press to restart",False,(255,0,0))
#Tạo khung bao quanh đối tượng
player_khung=player_surface.get_rect(midbottom=(70,291))
player_khung_2=player_jump_2.get_rect(midbottom=(70,291))
bullet_khung=bullet_surface.get_rect(bottomleft=(800,285))
game_name_khung=game_name.get_rect(topleft=(0,0))
game_hd_khung=game_hd.get_rect(midbottom=(400,400))
#Trọng lực
player_graviy=0

game_active=True
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
                '''elif ev.key==pygame.K_DOWN:
                    player=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\player_sit.png").convert_alpha()
                    player_khung=player.get_rect(midbottom=(70,291))
            elif ev.type==pygame.KEYUP:
                player=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\player.png").convert_alpha()
                player_khung=player.get_rect(midbottom=(70,291))'''
        else:
            if ev.key==pygame.K_SPACE:
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
        

        #Enemies
        screen.blit(bullet_surface,bullet_khung) #Đặt đạn
        bullet_khung.x-=7 #Đạn bay
        if bullet_khung.colliderect(player_khung):
            game_active=False
    else:
        screen.blit(pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\game_over.png"),(0,0))
        screen.blit(game_hd,game_hd_khung)
        
    pygame.display.update()
    clock.tick(60)