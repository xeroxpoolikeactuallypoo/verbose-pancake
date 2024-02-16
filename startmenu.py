import pygame
import sys
from constants import WIDTH, HEIGHT
from nameinput import nameinput
from instructions import instructions_screen

def start_screen(frame, background_image, background_image2, text):
    start = False
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    nameinput(frame, background_image2, background_image, text)
                    return instructions_screen(frame, background_image2, text)
                elif event.button == 3:
                    pygame.quit()
                    sys.exit()

        frame.blit(background_image, (0, 0))
        start_text = text.render("Press Left Click to Start", True, (0, 0, 0))
        exit_text = text.render("Press Right Click to Exit", True, (0, 0, 0))
        frame.blit(start_text, (WIDTH // 2 - 128, HEIGHT // 2 - 60))
        frame.blit(exit_text, (WIDTH // 2 - 128, HEIGHT // 2 + 60))
        pygame.display.flip()