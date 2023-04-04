import pygame
from settings import *
from random import randint

class MagicPlayer:
    def __init__(self, animation_player):
        self.animation_player = animation_player
        self.sounds = {
            'heal': pygame.mixer.Sound('../audio/heal.wav'),
            'flame': pygame.mixer.Sound('../audio/fire.wav')
        }

    def heal(self, player, strength, cost, groups):
        if player.energy >= cost:
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats['health']:
                player.health = player.stats['health']
            offset = pygame.math.Vector2(0,50)
            self.animation_player.create_particles('heal', player.rect.center - offset , groups)
            self.animation_player.create_particles('aura', player.rect.center, groups)
            self.sounds['heal'].play()
            

    def flame(self,player, cost, groups):
        if player.energy >= cost:
            player.energy -= cost
            direction = None
            if player.status.split('_')[0] == 'up':
                direction = pygame.math.Vector2(0,-1)
            elif player.status.split('_')[0] == 'down':
                direction = pygame.math.Vector2(0,1)
            elif player.status.split('_')[0] == 'left':
                direction = pygame.math.Vector2(-1,0)
            else:
                direction = pygame.math.Vector2(1,0)
            
            self.sounds['flame'].play()

            for i in range (1,6):
                x_pos = player.rect.centerx + randint(-TILESIZE // 6, TILESIZE // 6)
                y_pos = player.rect.centery + randint(-TILESIZE // 6, TILESIZE // 6)
                if direction.x:
                    offset_x = direction.x * i * TILESIZE
                    self.animation_player.create_particles('flame', (x_pos + offset_x, y_pos), groups)
                    self.animation_player.create_particles('aura', player.rect.center, groups)
                else:
                    offset_y = direction.y * i * TILESIZE
                    self.animation_player.create_particles('flame', (x_pos, y_pos + offset_y), groups)
                    self.animation_player.create_particles('aura', player.rect.center, groups)