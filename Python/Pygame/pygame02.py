import pygame
pygame.init() #Khởi tạo tất cả mô-đun pygame -->Gọi ra đầu tiên
screen=pygame.display.set_mode((800,400)) #Khởi tạo mô-đun hiển thị (rộng,cao)
pygame.display.set_caption("Run")
clock=pygame.time.Clock()
bg=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\bg.png").convert() #Load ảnh backgroud
#Add player
player_stand=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\player.png").convert_alpha() #Load ảnh player
player_surface=player_stand
#Add enemies
bullet_down=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\bullet_down.png").convert_alpha() #Load ảnh đạn dưới
bullet_surface=bullet_down
#Tạo khung bao quanh đối tượng
player_khung=player_surface.get_rect(midbottom=(70,291))
bullet_khung=bullet_surface.get_rect(bottomleft=(800,274))

while True:
    #Tạo nút thoát khi bấm thoát trên màn hình
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(bg,(0,0)) #Đặt background
    screen.blit(player_surface,player_khung) #Đặt player
    screen.blit(bullet_surface,bullet_khung) #Đặt đạn
    bullet_khung.x-=7 #Đạn bay
    pygame.display.update()
    clock.tick(60)