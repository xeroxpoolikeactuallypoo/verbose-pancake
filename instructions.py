import pygame
import sys
from constants import WIDTH, HEIGHT

def instructions_screen(frame, background_image2, text):
    instructions = True
    while instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    display_instructions(frame, background_image2, text)
                    return True
                elif event.button == 3:  # Right mouse button
                    return False

        frame.blit(background_image2, (0, 0))
        ask_text = text.render("Would you like to see the instructions?", True, (0, 0, 0))
        instructions_text = text.render("Press Left Click to View Instructions", True, (0, 0, 0))
        exit_text = text.render("Press Right Click to Skip and Begin Game", True, (0, 0, 0))
        frame.blit(instructions_text, (WIDTH // 2 - 210, HEIGHT // 2 - 60))
        frame.blit(exit_text, (WIDTH // 2 - 240, HEIGHT // 2 + 60))
        frame.blit(ask_text, (WIDTH // 2 - 220, HEIGHT // 2 - 120))
        pygame.display.flip()

def display_instructions(frame, background_image2, text):
  instructions_text = text.render("Instructions:\n\n1. This is an example instruction.\n2. Add more instructions as needed.", True, (0, 0, 0))
  frame.blit(background_image2, (0, 0))
  frame.blit(instructions_text, (WIDTH // 2 - 200, HEIGHT // 2 - 100))
  pygame.display.flip()
  pygame.time.delay(5000)