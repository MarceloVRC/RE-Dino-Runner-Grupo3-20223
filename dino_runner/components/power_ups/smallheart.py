from dino_runner.components.power_ups.powerup import PowerUp
from dino_runner.utils.constants import DEFAULT_TYPE, HEART


class SmallHeart(PowerUp):
    def __init__(self):
        super().__init__(HEART, DEFAULT_TYPE)