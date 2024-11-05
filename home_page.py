import pygame
import sys
import first_page
import highscore
import usernamedisplay
def main_menu():
    # Initialize Pygame
    pygame.init()
    pygame.mixer.init()

    # Set up screen size and colors
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Typing Game")
    screen_width, screen_height = screen.get_size()
    button_color = (0,0,205)
    #hover_color = (100, 149, 237)
    hover_color=(255,215,0)
    text_color = (255, 255, 255)
    font = pygame.font.Font(None, 74)

    # Load background music
    bg_music = pygame.mixer.music.load("i.mp3")  
    pygame.mixer.music.play(-1)  # Background music loop
     # Load and play background music
    

    # Button setup
    button_texts = ["New Game", "High Score", "Username", "Quit"]
    buttons = []
    button_width, button_height = 300, 100
    spacing = 40

    # Define button positions and create rectangles for them
    for i, text in enumerate(button_texts):
        x = (screen_width - button_width) // 2
        y = (screen_height - ((button_height + spacing) * len(button_texts))) // 2 + i * (button_height + spacing)
        buttons.append((pygame.Rect(x, y, button_width, button_height), text))

    # Function to draw buttons and handle hovering
    def draw_buttons():
        for rect, text in buttons:
            color = hover_color if rect.collidepoint(pygame.mouse.get_pos()) else button_color
            pygame.draw.rect(screen, color, rect)
            button_text = font.render(text, True, text_color)
            text_rect = button_text.get_rect(center=rect.center)
            screen.blit(button_text, text_rect)

    # Main loop
    running = True
    while running:
        # Load and display background image
        background_image = pygame.image.load("bg.jpg")
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        screen.blit(background_image, (0, 0))

        # Draw the buttons
        draw_buttons()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse click
                for rect, text in buttons:
                    if rect.collidepoint(event.pos):
                        if text == "New Game":
                            print("New Game button clicked")
                            first_page.typing_game()  # Call typing_game function from first_page module

                        elif text == "High Score":
                            print("High Score button clicked")
                            highscore.display_high_score()
                            # High Score functionality here
                        elif text == "Username":
                            print("Username button clicked")
                            usernamedisplay.display_username()
                            # Username functionality here
                        elif text == "Quit":
                            pygame.quit()
                            sys.exit()

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

# Run the main menu function
if __name__ == "__main__":
    main_menu()
