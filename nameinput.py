import pygame
import sys
from constants import WIDTH, HEIGHT
from instructions import instructions_screen

def nameinput(frame, background_image2, background_image, text):
    playername = ""
    error = ""
    inputname = True

    while inputname:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(playername) > 8 or not playername.isalpha():
                        error = "Invalid name. Please enter a name with 8 characters or less and only letters."
                    else:
                        instructions = instructions_screen(frame, background_image2, text)
                        return playername, instructions
                elif event.key == pygame.K_BACKSPACE:
                    playername = playername[:-1]
                    error = ""
                elif event.unicode.isalpha() and len(playername) < 8:
                    playername += event.unicode
                    error = ""
  
        frame.blit(background_image2, (0, 0))
        input_text = text.render(f"Enter Your Name: {playername}", True, (0, 0, 0))
        error_message_text = text.render(error, True, (255, 0, 0))
        frame.blit(error_message_text, (WIDTH // 2 - 150, HEIGHT // 2))
        frame.blit(input_text, (WIDTH // 2 - 150, HEIGHT // 2 - 60))
        pygame.display.flip()
  
    return playername
