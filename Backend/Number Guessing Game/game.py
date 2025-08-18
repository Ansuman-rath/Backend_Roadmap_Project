import json
import random
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional, Tuple


DIFFICULTY_TO_CHANCES: Dict[str, int] = {
    "easy": 10,
    "medium": 5,
    "hard": 3,
}


HIGHSCORES_FILENAME = "highscores.json"


@dataclass
class HighScore:
    attempts: int
    time_seconds: float

    def to_dict(self) -> Dict[str, float]:
        return {"attempts": self.attempts, "time_seconds": self.time_seconds}


def load_high_scores(file_path: Path) -> Dict[str, HighScore]:
    if not file_path.exists():
        return {}
    try:
        data = json.loads(file_path.read_text(encoding="utf-8"))
        scores: Dict[str, HighScore] = {}
        for difficulty, record in data.items():
            if (
                isinstance(record, dict)
                and "attempts" in record
                and "time_seconds" in record
            ):
                scores[difficulty] = HighScore(
                    attempts=int(record["attempts"]),
                    time_seconds=float(record["time_seconds"]),
                )
        return scores
    except Exception:
        return {}


def save_high_scores(file_path: Path, scores: Dict[str, HighScore]) -> None:
    try:
        serializable = {k: v.to_dict() for k, v in scores.items()}
        file_path.write_text(json.dumps(serializable, indent=2), encoding="utf-8")
    except Exception:
        pass


def select_difficulty() -> Tuple[str, int]:
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    while True:
        choice = input("\nEnter your choice (1-3): ").strip().lower()
        mapping = {"1": "easy", "2": "medium", "3": "hard", "easy": "easy", "medium": "medium", "hard": "hard"}
        if choice in mapping:
            difficulty = mapping[choice]
            chances = DIFFICULTY_TO_CHANCES[difficulty]
            print(f"\nGreat! You have selected the {difficulty.capitalize()} difficulty level.")
            print("Let's start the game!\n")
            return difficulty, chances
        print("Invalid choice. Please enter 1, 2, or 3 (or type easy/medium/hard).")


def format_elapsed(seconds: float) -> str:
    minutes = int(seconds // 60)
    secs = int(seconds % 60)
    if minutes > 0:
        return f"{minutes}m {secs}s"
    return f"{secs}s"


def maybe_show_high_score(
    high_scores: Dict[str, HighScore], difficulty: str
) -> None:
    if difficulty in high_scores:
        hs = high_scores[difficulty]
        print(
            f"Current high score for {difficulty.capitalize()}: "
            f"{hs.attempts} attempts in {format_elapsed(hs.time_seconds)}"
        )


def should_update_high_score(existing: Optional[HighScore], attempts: int, time_seconds: float) -> bool:
    if existing is None:
        return True
    if attempts < existing.attempts:
        return True
    if attempts == existing.attempts and time_seconds < existing.time_seconds:
        return True
    return False


def play_round(difficulty: str, total_chances: int) -> Tuple[bool, int, float]:
    secret_number = random.randint(1, 100)
    attempts_used_for_guesses = 0
    chances_remaining = total_chances
    max_hints = 2
    hints_used = 0

    # Track the feasible interval given feedback to produce better hints
    min_possible = 1
    max_possible = 100

    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {total_chances} chances to guess the correct number.")
    print("Type 'hint' to use a hint (costs 1 chance, up to 2 hints). Type 'quit' to give up this round.\n")

    start_time = time.perf_counter()

    while chances_remaining > 0:
        user_input = input("Enter your guess (1-100), 'hint', or 'quit': ").strip().lower()

        if user_input == "quit":
            print("You gave up this round.")
            break

        if user_input == "hint":
            if hints_used >= max_hints:
                print("No hints left.")
                continue
            if chances_remaining <= 1:
                print("You don't have enough chances left to use a hint.")
                continue

            # Provide a narrowed interval around the secret number
            spread = max(3, (max_possible - min_possible) // 4)
            lower_hint = max(min_possible, secret_number - spread)
            upper_hint = min(max_possible, secret_number + spread)
            # Ensure the interval is valid and contains the secret
            if lower_hint > secret_number:
                lower_hint = secret_number
            if upper_hint < secret_number:
                upper_hint = secret_number

            chances_remaining -= 1
            hints_used += 1
            print(f"Hint: The number is between {lower_hint} and {upper_hint}.")
            print(f"Chances remaining: {chances_remaining}\n")
            continue

        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a valid number, 'hint', or 'quit'.")
            continue

        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.")
            continue

        attempts_used_for_guesses += 1
        if guess == secret_number:
            elapsed = time.perf_counter() - start_time
            print(
                f"Congratulations! You guessed the correct number in {attempts_used_for_guesses} attempts."
            )
            print(f"Time taken: {format_elapsed(elapsed)}\n")
            return True, attempts_used_for_guesses, elapsed

        chances_remaining -= 1
        if guess < secret_number:
            min_possible = max(min_possible, guess + 1)
            print(f"Incorrect! The number is greater than {guess}.")
        else:
            max_possible = min(max_possible, guess - 1)
            print(f"Incorrect! The number is less than {guess}.")

        if chances_remaining > 0:
            print(f"Chances remaining: {chances_remaining}\n")

    elapsed = time.perf_counter() - start_time
    print(f"\nOut of chances! The correct number was {secret_number}.")
    print(f"Time taken: {format_elapsed(elapsed)}\n")
    return False, attempts_used_for_guesses, elapsed


def main() -> None:
    print("Welcome to the Number Guessing Game!")
    print("Rules:")
    print("- I'm thinking of a number between 1 and 100.")
    print("- Choose a difficulty to set how many chances you get.")
    print("- After each guess, you'll be told if the number is higher or lower.")
    print("- You can use up to 2 hints; each hint costs 1 chance.")
    print("- Win by guessing the number before you run out of chances.\n")

    highscores_path = Path(__file__).with_name(HIGHSCORES_FILENAME)
    high_scores = load_high_scores(highscores_path)

    while True:
        difficulty, chances = select_difficulty()
        maybe_show_high_score(high_scores, difficulty)

        won, attempts, elapsed = play_round(difficulty, chances)

        existing = high_scores.get(difficulty)
        if won and should_update_high_score(existing, attempts, elapsed):
            high_scores[difficulty] = HighScore(attempts=attempts, time_seconds=elapsed)
            save_high_scores(highscores_path, high_scores)
            print(
                f"New high score for {difficulty.capitalize()}! "
                f"{attempts} attempts in {format_elapsed(elapsed)}."
            )

        while True:
            again = input("Play again? (y/n): ").strip().lower()
            if again in {"y", "yes"}:
                print("")
                break
            if again in {"n", "no"}:
                print("Thanks for playing! Goodbye.")
                return
            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting. Thanks for playing!")
        sys.exit(0)


