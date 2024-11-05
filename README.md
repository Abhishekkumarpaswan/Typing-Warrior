
# Python Multimedia Game Project

This repository contains a Python-based multimedia game project that integrates graphical and audio components to create an engaging user experience. The project includes multiple game stages, score tracking, and user interactivity.

## Features

- **Multiple Screens and Stages**: Each stage is presented in different scripts, such as `first_page.py` (main menu), `home_page.py`, and `story_page.py`.
- **Username and Score Tracking**: Users can input their usernames, and high scores are saved for reference.
- **Graphics and Sounds**: Custom backgrounds and sound effects enhance the user experience with `.jpg`, `.png` images and `.mp3` files.

## Project Structure

The project is organized as follows:

- **Python Scripts**: Contains the main logic and individual pages/stages of the game.
  - `first_page.py`: Main menu or introductory page.
  - `home_page.py`: Secondary page in the game sequence.
  - `story_page.py`: Contains the story or narrative part of the game.
  - `username.py`, `usernamedisplay.py`: Manage user input and display for usernames.
  - `highscore.py`: Handles high score tracking.
  - `winner.py`: Processes win conditions or end-game events.
  - `second.py`: Represents an additional stage or gameplay section.

- **Media Assets**: Visuals and sound assets used in the game.
  - **Images**: Backgrounds and in-game visuals (`background.jpg`, `earth.jpg`, etc.).
  - **Audio**: Background music and sound effects (`typing.mp3`, `happy-outro-8110.mp3`).

- **Data Files**: Text files for storing scores and usernames.
  - `score.txt`: High score storage.
  - `username.txt`: Stores player usernames.

## Getting Started

### Prerequisites

- **Python 3.x** is required to run the scripts.
- Install any necessary libraries mainly 'pygame'

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourprojectname.git
   cd yourprojectname
   ```

2. Run the main Python script to start the game:
   ```bash
   python username.py
   ```

### Notes

- Ensure the media files (images and audio) are accessible from the paths used in the code.
- For optimal experience, run the game in a Python environment that supports multimedia modules (e.g., `pygame`).

## Contributors

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
