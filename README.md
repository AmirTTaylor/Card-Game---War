# Card Game - War

## Description
This is a Python implementation of the classic card game **War**. The game is played between two players who each receive half of a standard deck of 52 cards. Players reveal the top card of their deck simultaneously, and the player with the higher card wins both cards. In the event of a tie, a "war" occurs, and additional cards are drawn to determine the winner. The game continues until one player has all the cards or a pre-determined stopping condition is met.

## Features
- Simulates the War card game between two players.
- Automatically shuffles and deals cards at the start.
- Implements the rules of War, including battles and wars.
- Displays the progress of the game round by round.
- Ends when one player wins all the cards.

## How to Run
1. Ensure you have Python installed (Python 3.x recommended).
2. Clone this repository:
   ```bash
   git clone https://github.com/AmirTTaylor/Card-Game---War.git
   ```
3. Navigate to the project directory:
   ```bash
   cd Card-Game---War
   ```
4. Run the script:
   ```bash
   python War.py
   ```

## Requirements
- Python 3.x
- No external dependencies (uses built-in Python libraries)

## Rules of War
1. Each player starts with half of the deck (26 cards each).
2. Players reveal the top card of their deck at the same time.
3. The player with the higher card wins both cards and places them at the bottom of their deck.
4. If the cards are equal in rank, a "war" occurs:
   - Each player places three additional cards face-down and one card face-up.
   - The player with the higher face-up card wins all the cards.
   - If there is another tie, the process repeats.
5. The game continues until one player has all the cards, or an optional limit is reached.

## Future Enhancements
- Implement a graphical interface
- Add Face Cards

## Contributing
Contributions are welcome! If you find bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is open-source and available under the MIT License.

## Author
Developed by **Amir T. Taylor**. Check out more projects at [GitHub](https://github.com/AmirTTaylor).

