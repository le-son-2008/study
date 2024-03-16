import pygame
pygame.init() #Khởi tạo tất cả mô-đun pygame -->Gọi ra đầu tiên
screen=pygame.display.set_mode((800,400)) #Khởi tạo mô-đun hiển thị (rộng,cao)
pygame.display.set_caption("Run")
clock=pygame.time.Clock()
bg=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\bg.png").convert() #Load ảnh backgroud
#Add player
player=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\player.png").convert_alpha() #Load ảnh player
#Add enemies
bullet_down=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\bullet_down.png").convert_alpha() #Load ảnh đạn dưới
bullet_surface=bullet_down
#Tạo khung bao quanh đối tượng
player_khung=player.get_rect(midbottom=(70,291))
bullet_khung=bullet_surface.get_rect(bottomleft=(800,274))
#Trọng lực
player_graviy=0

while True:
    for ev in pygame.event.get():

        #Thoát khi bấm X trên màn hình
        if ev.type==pygame.QUIT:
            pygame.quit()
            exit()

        #Check phím bấm
        if ev.type==pygame.KEYDOWN:
            if ev.key==pygame.K_SPACE:
                player_graviy=-12
            '''elif ev.key==pygame.K_DOWN:
                player=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\player_sit.png").convert_alpha()
                player_khung=player.get_rect(midbottom=(70,291))
        elif ev.type==pygame.KEYUP:
            player=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\player.png").convert_alpha()
            player_khung=player.get_rect(midbottom=(70,291))'''

    screen.blit(bg,(0,0)) #Đặt background

    #Player
    player_graviy+=1
    player_khung.y+=player_graviy
    if player_khung.bottom>=291:player_khung.bottom=291
    if player_khung.top<=145:player_khung.top=14
    screen.blit(player,player_khung) #Đặt player
    screen.blit(bullet_surface,bullet_khung) #Đặt đạn
    bullet_khung.x-=7 #Đạn bay

    pygame.display.update()
    clock.tick(60)