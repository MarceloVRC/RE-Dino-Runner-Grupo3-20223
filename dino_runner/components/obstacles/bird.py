import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH

class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, 0)
        self.bird_rect = self.image[0].get_rect()
        self.rect.y = random.randint(200, 320)
        self.step_index = 0

    def draw(self,screen):
        if self.step_index >= 10:
            self.step_index = 0

        if self.step_index <= 5 :
            self.image = BIRD[0]
        else:
            self.image = BIRD[1]

        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.step_index += 1
        