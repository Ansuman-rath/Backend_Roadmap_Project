## Number Guessing Game (CLI)

A simple, fun command-line number guessing game built in Python. The computer picks a number between 1 and 100 and you try to guess it before you run out of chances.

### Features
- **Difficulty levels**: Easy (10 chances), Medium (5), Hard (3)
- **Higher/Lower feedback** after each guess
- **Hints**: up to 2 per round; each hint costs 1 chance
- **Timer**: see how long you took per round
- **Multiple rounds**: play again until you choose to quit
- **Persistent high scores** per difficulty (fewest attempts; tie-break by fastest time)
- **Graceful exit**: type `quit` during a round or press Ctrl+C anytime

### Requirements
- Python 3.8 or newer

### How to Run
- Windows (PowerShell or CMD):
```bash
python number_guessing_game.py
# or, if you have multiple Python versions installed
py -3 number_guessing_game.py
```

- macOS/Linux:
```bash
python3 number_guessing_game.py
```

### Sample Gameplay
```
Welcome to the Number Guessing Game!
Rules:
- I'm thinking of a number between 1 and 100.
- Choose a difficulty to set how many chances you get.
- After each guess, you'll be told if the number is higher or lower.
- You can use up to 2 hints; each hint costs 1 chance.
- Win by guessing the number before you run out of chances.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice (1-3): 2

Great! You have selected the Medium difficulty level.
Let's start the game!

I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
Type 'hint' to use a hint (costs 1 chance, up to 2 hints). Type 'quit' to give up this round.

Enter your guess (1-100), 'hint', or 'quit': 50
Incorrect! The number is less than 50.
Chances remaining: 4

Enter your guess (1-100), 'hint', or 'quit': 25
Incorrect! The number is greater than 25.
Chances remaining: 3

Enter your guess (1-100), 'hint', or 'quit': 35
Incorrect! The number is less than 35.
Chances remaining: 2

Enter your guess (1-100), 'hint', or 'quit': 30
Congratulations! You guessed the correct number in 4 attempts.
Time taken: 12s
```

### High Scores
- Saved to `highscores.json` in the same directory as the script.
- The best score is determined by:
  1. **Fewer attempts**
  2. If tied, **faster time**
- To reset, delete `highscores.json` and play again.

### Tips
- You can type `easy`, `medium`, or `hard` instead of 1/2/3 when selecting difficulty.
- Use `hint` strategically—each hint narrows the range but costs one chance.
- Type `quit` to abandon the current round without closing the program.


