import pygame
import sys
import random

def main_page():
    # Initialize Pygame
    pygame.init()
    
    # Screen settings
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width, screen_height = screen.get_size()  # Get screen dimensions
    pygame.display.set_caption("Congratulations!")

    # Colors
    WHITE = (255, 255, 255)
    YELLOW = (255, 223, 0)
    BLUE = (0, 191, 255)
    RED = (255, 69, 0)
    GREEN = (50, 205, 50)
    PURPLE = (147, 112, 219)
    COLORS = [YELLOW, BLUE, RED, GREEN, PURPLE]

    # Load celebration music
    pygame.mixer.music.load("happy-outro-8110.mp3")  # Make sure you have a celebration.mp3 file
    pygame.mixer.music.play(-1)  # Loop celebration music

    # Fonts
    font_large = pygame.font.Font(None, 80)
    font_small = pygame.font.Font(None, 50)

    # Text messages
    win_text = font_large.render("Congratulations, You've saved Earth!", True, YELLOW)
    win_text_rect = win_text.get_rect(center=(screen_width // 2, screen_height // 3 - 130))  # Move up by 130 pixels

    appreciation_text = font_small.render("You've reached the top score! Amazing job!", True, WHITE)
    appreciation_text_rect = appreciation_text.get_rect(center=(screen_width // 2, screen_height // 2 - 80))  # Move up by 80 pixels

    # Reduce gap between sentences
    appreciation_text_rect.y = win_text_rect.y + win_text_rect.height + 20  # Set directly below the first sentence

    # Confetti settings
    confetti_particles = []
    for _ in range(100):  # Adjust number of particles
        x = random.randint(0, screen_width)
        y = random.randint(-screen_height, 0)  # Start above the screen
        speed = random.randint(2, 10)
        color = random.choice(COLORS)
        confetti_particles.append({"x": x, "y": y, "speed": speed, "color": color})

    clock = pygame.time.Clock()
    running = True
    while running:
        background_image = pygame.image.load("save.jpg")
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        screen.blit(background_image, (0, 0))

        # Display text
        screen.blit(win_text, win_text_rect.topleft)
        screen.blit(appreciation_text, appreciation_text_rect.topleft)

        # Update and draw confetti particles
        for particle in confetti_particles:
            pygame.draw.circle(screen, particle["color"], (particle["x"], particle["y"]), 5)
            particle["y"] += particle["speed"]  # Move particle down

            # Reset particle to top once it leaves the screen
            if particle["y"] > screen_height:
                particle["y"] = random.randint(-50, -10)
                particle["x"] = random.randint(0, screen_width)
                particle["speed"] = random.randint(2, 10)
                particle["color"] = random.choice(COLORS)

        pygame.display.flip()  # Update the display

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN or event.type == pygame.K_ESCAPE):
                pygame.mixer.music.stop()  # Stop the celebration music
                pygame.quit()
                sys.exit()

        clock.tick(30)  # Control frame rate

if __name__ == "__main__":
    main_page()
