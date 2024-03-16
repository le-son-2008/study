import pygame
pygame.init() #Khởi tạo tất cả mô-đun pygame -->Gọi ra đầu tiên
screen=pygame.display.set_mode((800,400)) #Khởi tạo mô-đun hiển thị (rộng,cao)
pygame.display.set_caption("R")
clock=pygame.time.Clock()
bg=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\bg.png") #Load ảnh backgroud
#Add player
player=pygame.image.load("C:\\Users\\Admin\\Documents\\Code\\Python\\Pygame\\Game\\player.png") 

while True:
    #Tạo nút thoát khi bấm thoát trên màn hình
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(bg,(0,0)) #Đặt background
    screen.blit(player,(100,191)) #Đặt player
    pygame.display.update()
    clock.tick(60)