import pygame
import sys
from shared import is_click_on_pause_button
from constants import WIDTH, HEIGHT

def pause_screen(frame, pause_background, text, pause_button_rect):
    error_message = ""
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = event.pos
                if is_click_on_pause_button(click_pos, pause_button_rect):
                    return False  # Continue the game
                elif event.button == 1:  # Left click
                    return False  # Unpause the game
                else:
                    error_message = "Invalid input. Please use left click."

        frame.blit(pause_background, (0, 0))
        pause_text = text.render("PAUSED", True, (255, 0, 0))
        resume_text = text.render("Left Click to Resume", True, (0, 0, 0))
        error_message_text = text.render(error_message, True, (255, 0, 0))

        frame.blit(pause_text, (WIDTH // 2 - 70, HEIGHT // 2 - 60))
        frame.blit(resume_text, (WIDTH // 2 - 135, HEIGHT // 2 + 60))
        frame.blit(error_message_text, (WIDTH // 2 - 200, HEIGHT // 2 + 120))

        pygame.display.flip()

    return True