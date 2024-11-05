import pygame
import sys
import home_page
def display_high_score():
    # Initialize Pygame
    pygame.init()
    
    # Screen settings
    screen = pygame.display.set_mode((600, 400))
    screen_width, screen_height = screen.get_size()
    pygame.display.set_caption("High Score Display")

    # Colors and font
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 48)
   
    pygame.mixer.music.load("i.mp3")
    pygame.mixer.music.play(-1)
    # Function to get the highest score and associated username
    def get_highest_score():
        try:
            with open("username.txt", "r") as user_file, open("score.txt", "r") as score_file:
                usernames = [line.strip() for line in user_file.readlines()]
                scores = [int(line.strip()) for line in score_file.readlines()]

            # Find the highest score and corresponding username
            max_score = max(scores)
            max_index = scores.index(max_score)
            top_user = usernames[max_index]

            return top_user, max_score
        except Exception as e:
            print(f"Error reading files: {e}")
            return "N/A", 0  # Default values if an error occurs

    # Retrieve top user and score
    top_user, top_score = get_highest_score()

    # Main loop
    running = True
    while running:
        #screen.fill(WHITE)
        background_image = pygame.image.load("bg.jpg")
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        screen.blit(background_image, (0, 0))
        # Display high score text
        title_text = font.render("High Score", True, WHITE)
        title_rect = title_text.get_rect(center=(300, 100))
        screen.blit(title_text, title_rect)

        # Display top user and score
        user_text = font.render(f"User: {top_user}", True, WHITE)
        score_text = font.render(f"Score: {top_score}", True, WHITE)
        user_rect = user_text.get_rect(center=(300, 200))
        score_rect = score_text.get_rect(center=(300, 250))

        screen.blit(user_text, user_rect)
        screen.blit(score_text, score_rect)

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


if __name__ == "__main__":
    display_high_score()  # Run the function to display high score

