import pygame
import sys
import random
import time
import home_page
import winner
def typing_game():
    # Initialize Pygame
    pygame.init()

    # Load background music
    bg_music = pygame.mixer.music.load("i.mp3")  
    pygame.mixer.music.play(-1)  # Background music loop
    
    # Screen settings for full screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width, screen_height = screen.get_size()  # Get screen dimensions
    pygame.display.set_caption("Typing Game")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    # Fonts
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)

    # Game variables
    words = [
    # Easy
    "cat", "dog", "bat", "hat", "pen", "book", "lamp", "cup", "star", "sun",
    "fish", "tree", "blue", "bird", "song", "walk", "run", "jump", "play", "love",
    "food", "cake", "home", "baby", "smile", "chair", "table", "water", "happy", "apple",
    "drink", "pizza", "house", "music", "laugh", "dance", "fruit", "bread", "sweet", "plant",
    
    # Medium
    "ocean", "island", "forest", "desert", "planet", "guitar", "violin", "flower", "garden", "butter",
    "school", "market", "beach", "singer", "family", "winter", "summer", "spring", "autumn", "season",
    "orange", "purple", "mountain", "friend", "holiday", "doctor", "camera", "travel", "sunset", "village",
    "animal", "nature", "mirror", "kitchen", "bedroom", "morning", "castle", "author", "writer", "painter",
    
    # Intermediate
    "paradise", "journey", "biology", "history", "science", "pyramid", "courage", "mystery", "fantasy", "fiction",
    "language", "culture", "adventure", "electric", "butterfly", "tropical", "volcano", "orchard", "harvest", "festival",
    "creative", "freedom", "gigantic", "journey", "isolation", "language", "research", "discovery", "exploration", "machinery",
    "professor", "molecule", "ecosystem", "civilization", "landscape", "reptilian", "aquarium", "cathedral", "landscape", "medieval",
    
    # Advanced
    "psychology", "philosophy", "architecture", "aesthetics", "allegiance", "independent", "phenomenon", "resilience", "authentic", "integrity",
    "perception", "innovation", "exceptional", "recognition", "historical", "equilibrium", "diversified", "intellectual", "sophisticated", "turbulence",
    "sustainable", "metropolitan", "collaboration", "imagination", "transformation", "legislature", "demonstration", "empowerment", "contemporary", "entrepreneur",
    "optimization", "extraordinary", "revolutionary", "proportional", "insurmountable", "extraordinary", "unprecedented", "accomplishment", "environmental", "communicative",
    
    # Difficult
    "infrastructure", "philanthropy", "circumference", "authoritarian", "consciousness", "differentiation", "constitutional", "international", "characteristic", "perpendicular",
    "administrative", "responsibility", "circumstantial", "misunderstood", "electromagnetic", "multidimensional", "individualistic", "unquestionable", "extraordinarily", "counterintuitive",
    "institutionalize", "thermodynamics", "parliamentarian", "interchangeable", "uncharacteristic", "revolutionary", "understanding", "unconventional", "comprehensibility", "misinterpretation",
    "phenomenological", "conceptualization", "multifunctional", "counterproductive", "disenfranchisement", "indistinguishable", "extraterrestrial", "nonproliferation", "overcompensation", "deinstitutionalize"
 ]

    
    current_word = random.choice(words)
    typed_word = ""
    score = 0
    time_limit = 5  # seconds to type each word
    start_time = time.time()

    # Function to save score
    def save_score(final_score):
        with open("score.txt", "w") as file:
            #file.write(f"Final Score: {final_score}")
            file.write(f"{final_score}")
    # End of game message function
    def last():
        background_image = pygame.image.load("destroy.jpg")
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        screen.blit(background_image, (0, 0))
        end_text = font.render("Game Over", True, WHITE)
        score_text = font.render(f"You have successfully cracked only {score} codes", True, WHITE)
        screen.blit(end_text, (screen_width // 2 - end_text.get_width() // 2, screen_height // 2 - 50))
        screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, screen_height // 2 + 50))
        pygame.display.flip()
        pygame.time.delay(3000)  # Wait before closing
        home_page.main_menu()
     
    # Winner page function
    def winner_page():
        pygame.mixer.music.stop()  # Stop background music
        winner.main_page()  # Call the main page from winner.py
    # Main game loop
    running = True
    while running:
        background_image = pygame.image.load("bg.jpg")
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
        screen.blit(background_image, (0, 0))

        # Check time
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            save_score(score)
            last()
            break

        # Render current word and typed word
        word_text = font.render(current_word, True, WHITE)
        word_text_rect = word_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
        screen.blit(word_text, word_text_rect.topleft)

        typed_text = font.render(typed_word, True, GREEN if typed_word == current_word else RED)
        typed_text_rect = typed_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(typed_text, typed_text_rect.topleft)

        # Display score and time remaining
        score_text = small_font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        time_text = small_font.render(f"Time Left: {int(time_limit - elapsed_time)}s", True, WHITE)
        screen.blit(time_text, (10, 50))

        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_score(score)
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    typed_word = typed_word[:-1]
                elif event.key == pygame.K_RETURN:
                    if typed_word == current_word:
                        score += 1
                        if score == 60:
                            save_score(score)
                            winner_page()  # Go to winner page
                            running = False
                            break
                        current_word = random.choice(words)  # Get a new word
                        typed_word = ""  # Clear typed word
                        start_time = time.time()  # Reset timer for new word
                        
                    else:
                        save_score(score)
                        last()
                        running = False
                        break
                else:
                    typed_word += event.unicode

    pygame.quit()

if __name__ == "__main__":
    typing_game()  # Run the game
