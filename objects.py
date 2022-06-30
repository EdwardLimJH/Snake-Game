from pkgutil import ImpImporter
import random as rand
from constant import *

class Snake:

    def __init__(self) -> None:
        self.body = [(rand.randint(0,SCREEN_WIDTH),rand.randint(0,SCREEN_HEIGHT))]
        
