import pygame

class End:
    def __init__(self,surface):
        
        self.display_surface = surface

        self.end_img = pygame.image.load("../graphics/start/game_over.png").convert_alpha() 


        self.font = pygame.font.SysFont("ARCADEPI" , 50 , True , False)
        self.quit = self.font.render("PRESS " , True , (255,255,255))
        self.quit_image = pygame.image.load("../graphics/start/quit.png").convert_alpha()  


    def draw(self,surface):
        surface.blit(self.end_img,(250,0))
        surface.blit(self.quit , (470,100))
        surface.blit(self.quit_image,(630,90))
