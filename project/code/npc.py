import pygame
from entity import Entity
from settings import *
import pygame.gfxdraw


class Npc (Entity):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.surface = pygame.Surface((TILESIZE, TILESIZE))
        # self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()

        pygame.gfxdraw.aacircle(self.surface, 15, 15, 14, (0, 255, 0))
        pygame.gfxdraw.filled_circle(self.surface, 15, 15, 14, (0, 255, 0))
        # self.image = pygame.draw.circle(self.surface, "blue", pos, 32)
        
        self.image = self.surface

        self.rect = self.image.get_rect(center = (pos[0] - TILESIZE, pos[1] - TILESIZE))
        # self.rect = self.image.get_rect(topleft = pos)
        self.sprite_type = 'npc'
        self.surface.blit(self.surface,self.rect)




    # def create_companion(self):
    #     # pygame.Circle
    #     x = self.player.rect.centerx
    #     y = self.player.rect.centery
    #     print('piep')
    #     # circle = pygame.Circle
    #     pygame.draw.circle(self.display_surface, 'blue', (x,y-64), 64, 3)