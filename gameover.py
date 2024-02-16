import pygame
import sys
import sqlite3
from constants import WIDTH, HEIGHT
from nameinput import nameinput

def game_over_screen(points, frame, background_image2, background_image, text):

    playername = nameinput(frame, background_image2, background_image, text)

    database_connection = sqlite3.connect('scores.db')
    database_cursor = database_connection.cursor()

    database_cursor.execute("INSERT INTO leaderboard (name, score) VALUES (?, ?)",
       (playername, points))
    database_connection.commit()
  
    database_cursor.execute("SELECT * FROM leaderboard ORDER BY score DESC LIMIT 3")
    allscores = database_cursor.fetchall()

    for i, allscores in enumerate(allscores):
        player_name_text = text.render(f"{i + 1}. Name: {allscores[0]}", True, (0, 0, 0))
        score_text = text.render(f"Score: {allscores[1]}", True, (0, 0, 0))
  
        frame.blit(player_name_text, (WIDTH // 2 - 60, HEIGHT // 2 + 100))
        frame.blit(score_text, (WIDTH // 2 - 60, HEIGHT // 2 + 140))

    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return True
                elif event.button == 3:
                    pygame.quit()
                    sys.exit()

        frame.blit(background_image2, (0, 0))  # Fill the screen with a background color

        game_over_text = text.render("Game Over", True, (255, 0, 0))
        restart_text = text.render("Press Left Click to Restart", True, (0, 0, 0))
        exit_text = text.render("Press Right Click to Exit", True, (0, 0, 0))

        frame.blit(game_over_text, (WIDTH // 2 - 60, HEIGHT // 2 - 60))
        frame.blit(restart_text, (WIDTH // 2 - 128, HEIGHT // 2 + 20))
        frame.blit(exit_text, (WIDTH // 2 - 122, HEIGHT // 2 + 60))

        pygame.display.flip()
