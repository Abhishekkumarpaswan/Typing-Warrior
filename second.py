import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Second Screen")

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 74)

def run_second_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
         #   elif event.type == pygame.KEYDOWN:
          #      if event.key == pygame.K_ESCAPE:
           #         return  # Press ESC to go back to first.py

        screen.fill(GREEN)
        text = font.render("Second Screen", True, BLACK)
        screen.blit(text, (250, 250))
        info_text = font.render("Press ESC to Return", True, BLACK)
        screen.blit(info_text, (100, 400))

        pygame.display.flip()


if __name__ == "__main__":
    run_second_screen()
