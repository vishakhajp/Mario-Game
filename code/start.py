import pygame

class Start:
    def __init__(self,surface):

        self.display_surface = surface
        self.clicked = False

        self.background = pygame.image.load("../graphics/start/background.png").convert()
    
        self.start_img = pygame.image.load("../graphics/start/start_press.png").convert_alpha()  
        
        self.font = pygame.font.SysFont("ARCADEPI" , 30 , True , False)
        self.text1 = self.font.render("PRESS X TO " , True , (0,255,255))
        self.exit_img = pygame.image.load("../graphics/start/exit.png").convert_alpha()  

    def draw(self,surface):
        surface.blit(self.background,(0,0))
        surface.blit(self.start_img,(150,150))
        surface.blit(self.text1 , (970,650))
        surface.blit(self.exit_img,(1120,632))
      

