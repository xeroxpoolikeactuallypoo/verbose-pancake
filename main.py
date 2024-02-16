import pygame
import sys
import random
import time
from pause import pause_screen
from gameover import game_over_screen
from shared import is_click_on_pause_button
from constants import WIDTH, HEIGHT
from startmenu import start_screen

pygame.init()

COLOUR = (255, 255, 255)
SPRITESIZE = 100

frame = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whack A Mole")
pause_button_rect = pygame.Rect(WIDTH - 50, 10, 40, 40)

# Load background and mole images
background_image = pygame.image.load('background.png')  # Replace with your background image path.
mole_image = pygame.image.load('mole.png')  # Replace with your mole image path.
background_image2 = pygame.image.load('grass.png')
pause_background = pygame.image.load('darkgrass.png')

mw = 80
mh = 80
resized_mole_image = pygame.transform.scale(mole_image, (mw, mh))

cl = pygame.time.Clock()
FRPESE = 60

class Mole:
  def __init__(self):
      self.moleappearance = [
          (190, 60), (360, 60), (535, 60),
          (190, 240), (360, 240), (535, 240),
          (190, 420), (360, 420), (535, 420)
      ]
      self.visible = False
      self.disappear_time = 0  # Updated from appear_time
      self.randomize_position()

  def randomize_position(self):
      self.x, self.y = random.choice(self.moleappearance)

  def appear(self):
      self.visible = True
      self.randomize_position()
      self.disappear_time = time.time() + 1.5  # Updated from appear_time

  def disappear(self):
      self.visible = False
      self.randomize_position()

  def should_disappear(self):
      return self.visible and time.time() >= self.disappear_time
      

moles = [Mole() for _ in range(3)]
points = 0
text = pygame.font.Font(None, 36)

start_screen(frame, background_image, background_image2, text)

start_time = pygame.time.get_ticks()
duration = 2000
paused = False

while pygame.time.get_ticks() - start_time < duration:
    cl.tick(FRPESE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for mole in moles:
                if mole.visible and mole.x <= event.pos[0] <= mole.x + mw and mole.y <= event.pos[1] <= mole.y + mh:
                    points += 1
                    mole.disappear()
            click_pos = event.pos
            if is_click_on_pause_button(click_pos, pause_button_rect):
                paused = pause_screen(frame, pause_background, text, pause_button_rect)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            paused = pause_screen(frame, pause_background, text, pause_button_rect)

    if not paused:
        frame.blit(background_image, (0, 0))

        for mole in moles:
            if mole.should_disappear():
                mole.disappear()
            if not mole.visible and time.time() >= mole.disappear_time and pygame.time.get_ticks() - start_time < duration:
                mole.appear()
            if mole.visible:
                frame.blit(resized_mole_image, (mole.x, mole.y))

        displaypoints = text.render(f"Total points: {points}", True, (0, 0, 0))
        frame.blit(displaypoints, (10, 10))

        remaining_time = max(0, (duration - (pygame.time.get_ticks() - start_time)) // 1000)
        timer_text = text.render(f"Time: {remaining_time}", True, (0, 0, 0))
        frame.blit(timer_text, (WIDTH - 120, 10))

        pygame.display.flip()

game_over_screen(points, frame, background_image2, background_image, text)
