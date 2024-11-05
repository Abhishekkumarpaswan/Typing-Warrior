import pygame
import sys
import time
import home_page

def display_typing_effect(paragraph, sound_file="i.mp3"):
    # Initialize Pygame
    pygame.init()

    # Screen setup for full-screen mode
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Typing Effect")
    screen_width, screen_height = screen.get_size()

    # Colors and font
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 48)  # Adjust font size as needed

    # Load typing sounds
    typing_sound = pygame.mixer.Sound(sound_file)

    # Set sound volumes
    typing_sound.set_volume(0.5)

    # Typing effect parameters
    typing_speed = 0.1  # Speed of typing in seconds per character
    lines = [""]
    char_index = 0
    line_spacing = 10  # Spacing between lines
    max_line_width = screen.get_size()[0] - 100  # Set a margin for readability

    # Main loop variables
    running = True
    last_char_time = time.time()
    last_sound_time = time.time()  # Timer for the second sound

    while running:
        # Load and display background image
        background_image = pygame.image.load("background2.jpg")
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        screen.blit(background_image, (0, 0))

        # Draw each line of text
        y_offset = screen.get_size()[1] // 2 - (len(lines) * (font.get_height() + line_spacing)) // 2
        for i, line in enumerate(lines):
            if line:  # Only render non-empty lines
                text_surface = font.render(line.strip(), True, WHITE)  # Use strip() to remove leading/trailing spaces
                text_rect = text_surface.get_rect(center=(screen.get_size()[0] // 2, y_offset + i * (font.get_height() + line_spacing)))
                screen.blit(text_surface, text_rect)

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key
                    if typing_sound:
                        typing_sound.stop()
                    home_page.main_menu()
                elif event.key == pygame.K_ESCAPE:  # Press ESC to exit full-screen mode
                    pygame.quit()
                    sys.exit()

        # Typing effect: add one character at a time
        if char_index < len(paragraph) and time.time() - last_char_time > typing_speed:
            next_char = paragraph[char_index]
            last_char_time = time.time()

            # Check if adding this character would exceed the max line width
            test_line = lines[-1] + next_char
            if font.size(test_line)[0] > max_line_width or next_char == '\n':
                lines.append("")  # Move to a new line
            
            lines[-1] += next_char
            char_index += 1
            
            # Play the sound
            typing_sound.play()

    # Quit Pygame
    pygame.quit()

# Example usage
if __name__ == "__main__":
    paragraph = ''' 
    YEAR 2147: EARTH UNDER SIEGE

    Alien forces have invaded, intent on destroying humanity. 

    Our only defense: disrupt their attack codes by typing alien words 
    that appear on the screen. Each correct word buys Earth more time; 
    each mistake brings destruction closer.

    You are Earth’s last hope.

    Type quickly. Type accurately. Save the world.

    Press ENTER to Begin -->
    '''
    display_typing_effect(paragraph)
