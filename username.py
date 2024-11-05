import pygame
import sys
import subprocess  # For launching another script

def get_user_name():
    # Initialize Pygame
    pygame.init()
    
    # Screen setup
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width, screen_height = screen.get_size()
    pygame.display.set_caption("Enter Your Name")
    
    pygame.mixer.music.load("i.mp3")
    pygame.mixer.music.play(-1)

    # Colors and font
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 100)  # Increased font size for user input
    instruction_font = pygame.font.Font(None, 50)  # Increased font size for instructions

    # Variables for storing the user input
    user_name = ""
    active = True

    while active:
        background_image = pygame.image.load("first.jpg")
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        screen.blit(background_image, (0, 0))

        # Display instruction
        instruction_text = instruction_font.render("PLEASE ENTER YOUR NAME AND PRESS ENTER:", True, WHITE)
        # Shift text to the upper part of the screen
        instruction_rect = instruction_text.get_rect(center=(screen_width // 2, screen_height // 4))
        screen.blit(instruction_text, instruction_rect)

        # Display user input as it's typed
        name_text = font.render(user_name, True, WHITE)
        # Position user input below the instruction text
        name_rect = name_text.get_rect(center=(screen_width // 2, screen_height // 4 + 100))
        screen.blit(name_text, name_rect)

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Save the name to a text file and exit the loop
                    with open("username.txt", "w") as file:
                        file.write(user_name)

                    active = False  # Exit input loop after saving
                   
                elif event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]  # Remove last character
                
                else:
                    # Add character to user_name, if it's not too long
                    if len(user_name) < 20:
                        user_name += event.unicode

    # End of function
    pygame.quit()
    
    # Launch the next script after quitting Pygame
    subprocess.run(["python", "story_page.py"])

if __name__ == "__main__":
    user_name = get_user_name()
    print("Username saved:", user_name)
