import pygame
import sys
import home_page
def display_username():
    # Initialize Pygame
    pygame.init()
    
    # Screen settings
    screen = pygame.display.set_mode((600, 400))
    screen_width, screen_height = screen.get_size()
    pygame.display.set_caption("Single Username Display")
    
    pygame.mixer.music.load("i.mp3")  # Make sure you have a celebration.mp3 file
    pygame.mixer.music.play(-1)
    # Colors and font
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 48)

    # Read the first username from the file
    def get_first_username():
        try:
            with open("username.txt", "r") as user_file:
                first_username = user_file.readline().strip()  # Read only the first line
            return first_username
        except FileNotFoundError:
            print("username.txt file not found.")
            return "No Username Found"

    # Load the first username
    username = get_first_username()

    # Main loop
    running = True
    while running:
        #screen.fill(WHITE)
        background_image = pygame.image.load("bg.jpg")
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        screen.blit(background_image, (0, 0))
        # Display the single username
        username_text = font.render("Hii "+username, True, WHITE)
        username_rect = username_text.get_rect(center=(300, 200))
        screen.blit(username_text, username_rect)

        # Update the display
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # enter
                  home_page.main_menu()  

    # Quit Pygame
    pygame.quit()
    sys.exit()


# Run the main menu function
if __name__ == "__main__":
   display_username()
