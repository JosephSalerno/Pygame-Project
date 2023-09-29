from modules.vector2D import Vector2


SCREEN_SIZE = Vector2(510, 780)

SCALE = 3
UPSCALED = SCREEN_SIZE


def adjustMousePos(mousePos):
   return Vector2(*mousePos)