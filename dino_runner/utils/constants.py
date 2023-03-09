import pygame
import os

# Global Constants
TITLE = "Dino"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30

DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
HAMMER_TYPE = 'hammer'

START_IMAGE = pygame.image.load(os.path.join(DIR, "Dino/DinoStart.png"))
DIE_IMAGE = pygame.image.load(os.path.join(DIR, "Dino/DinoDead.png"))
RESET_BUTTON = pygame.image.load(os.path.join(DIR, 'Other/Reset.png'))

pygame.mixer.init()

SOUNDS = [
    # 0 DIE
    pygame.mixer.Sound(os.path.join(DIR,'Other/die.wav')),
    # 1 JUMP
    pygame.mixer.Sound(os.path.join(DIR, 'Other/jump.wav')),
    # 2 POINT
    pygame.mixer.Sound(os.path.join(DIR, 'Other/point.wav')),
    # 3 HUMMERING
    pygame.mixer.Sound(os.path.join(DIR, 'Other/008865223_prev.wav')),
    # 4 HUMMER
    pygame.mixer.Sound(os.path.join(DIR, 'Other/008887041_prev.wav')),
    # 5 -LIVE
    pygame.mixer.Sound(os.path.join(DIR, 'Other/pacman-eating-cherry.wav')),
    # 6 +LIVE
    pygame.mixer.Sound(os.path.join(DIR, 'Other/pacman-eating-ghost.wav')),
    # 7 SHIELD
    pygame.mixer.Sound(os.path.join(DIR, 'Other/kirby-super-star-1up.wav'))
]
GAME_OVER = pygame.image.load(os.path.join(DIR, 'Other/GameOver.png'))