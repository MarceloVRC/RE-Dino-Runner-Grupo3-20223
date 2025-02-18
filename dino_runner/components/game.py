import random
import pygame
from dino_runner.components import text_utils
from dino_runner.components.dino import Dino
from dino_runner.components.obstacles.obstaclemanager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.components.power_ups.smallheart import SmallHeart

from dino_runner.utils.constants import BG, CLOUD, DIE_IMAGE, GAME_OVER, HEART, ICON, RESET_BUTTON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, SOUNDS, START_IMAGE, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dino()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.running = True
        self.death_count = 0
        self.max_score = 0
        self.x_pos_cloud = SCREEN_WIDTH
        self.power_up_manager = PowerUpManager()

    def run(self):
        # Game loop: events - update - draw
        self.create_components()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.player.check_invincibility(self.screen)
        self.player.check_hammering(self.screen)
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_clouds()
        self.score()
        self.screen.blit(HEART, (35, 20) )
        extra_lives, extra_lives_rect = text_utils.get_centered_message('     x '+ str(self.player.extra_lives) , 70, 33, 18)
        self.screen.blit(extra_lives, extra_lives_rect)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def execute (self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):
        white_color = (255,255,255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_menu_elements(self):
        if self.death_count == 0:
            text, text_rect = text_utils.get_centered_message('Press any Key to start')
            self.screen.blit(text, text_rect)
            #tarea
        else: 
            self.die_screen()
            return

        self.screen.blit(BG , (0,380))
        self.screen.blit(START_IMAGE , (80,310))

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN :
                self.run()

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        if self.points % 1000 == 0:
            SOUNDS[2].play()
        text, text_rect = text_utils.get_score_element(self.points)
        hi, hi_rect = text_utils.get_centered_message('HI : '+ str(self.max_score) ,900,50,16)
        self.screen.blit(hi, hi_rect)
        self.screen.blit(text, text_rect)
    
    def set_max_score(self, score):
        if score > self.max_score:
            self.max_score = score

    def reset_game(self):
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.x_pos_cloud = SCREEN_WIDTH
        self.obstacle_manager.reset_obstacles()
        self.player.extra_lives = 0

    def die_screen(self):
        white_color = (255,255,255)
        self.screen.fill(white_color)
        self.print_die_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_die_elements(self):
        text, text_rect = text_utils.get_centered_message('Press any Key to play again', 90 , 10, 12)
        self.screen.blit(text, text_rect)
        self.screen.blit(BG , (0,380))
        self.screen.blit(DIE_IMAGE , (80, 310) )
        self.screen.blit(RESET_BUTTON , (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2-50))
        self.screen.blit(GAME_OVER , (SCREEN_WIDTH // 2-  200, SCREEN_HEIGHT // 2-150))
        deaths, deaths_rect = text_utils.get_centered_message('DEATHS: '+ str(self.death_count) , 1000, 50, 16)
        self.screen.blit(deaths, deaths_rect)
        max_score, max_score_rect = text_utils.get_centered_message('HIGH SCORE: '+ str(self.max_score) , 1000, 70, 16)
        self.screen.blit(max_score, max_score_rect)

    def draw_clouds(self):
        ## EN DESARROLLO
        self.screen.blit(CLOUD, (self.x_pos_cloud, 50))
        self.screen.blit(CLOUD, (self.x_pos_cloud - 200, 70))
        self.screen.blit(CLOUD, (self.x_pos_cloud + 200, 130))
        self.screen.blit(CLOUD, (self.x_pos_cloud + 600, 100))
        self.screen.blit(CLOUD, (self.x_pos_cloud + 1000, 180))
        self.x_pos_cloud -= 1
        if self.x_pos_cloud < -200:
            self.x_pos_cloud = SCREEN_WIDTH

    def create_components(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points)

    def check_shield(self):
        if self.player.shield == True:
            return True
        else:
            return False
    
    def check_extra_lives(self):
        if self.player.extra_lives == 0:
            return True
        else:
            return False