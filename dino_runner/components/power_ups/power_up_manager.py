import random

import pygame
from dino_runner.components.power_ups.hammer import Hammer

from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.smallheart import SmallHeart
from dino_runner.utils.constants import SHIELD_TYPE, SOUNDS


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0
        self.points = 0
        self.option_number = list(range(1,10))

    def reset_power_ups(self, points):
        self.power_ups = []
        self.points = points
        self.when_appers = random.randint(200,300) + points

    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_appers == self.points:
                aleatory = 3 #random.randint(1,3)
                if aleatory == 1:
                    self.power_ups.append(Shield())
                elif aleatory == 2:
                    self.power_ups.append(SmallHeart())
                elif aleatory == 3:
                    self.power_ups.append(Hammer())

                self.when_appers = random.randint( self.when_appers + 200, self.when_appers + 500)
        return self.power_ups
    
    def update (self, points, game_speed, dino):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update( game_speed, self.power_ups)
            if dino.dino_rect.colliderect(power_up.rect):
                if isinstance(power_up, Shield):
                    SOUNDS[7].play()
                    power_up.start_time = pygame.time.get_ticks()
                    dino.shield = True
                    dino.show_text = True
                    dino.type = power_up.type
                    time_random = random.randrange(5,8)
                    dino.shield_time_up = power_up.start_time + (time_random * 1000)
                elif isinstance(power_up, SmallHeart):
                    SOUNDS[6].play()
                    dino.extra_lives += 1
                elif isinstance(power_up, Hammer):
                    SOUNDS[4].play()
                    power_up.start_time = pygame.time.get_ticks()
                    dino.type = power_up.type
                    dino.hammering = True
                    time_random = random.randrange(5,8)
                    dino.hummer_time_up = power_up.start_time + (time_random * 1000)
                self.power_ups.remove(power_up)

    def draw (self,screen):
        for power_up in self.power_ups:
            power_up.draw(screen)