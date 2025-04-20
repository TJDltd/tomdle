from src.tomdle import Tomdle
from src.tomdle_base import LetterResult


def main() -> None:
    """Run the Tomdle game."""
    game = Tomdle(word_count=1, word_length=5, max_guesses=6)

    print("Welcome to Tomdle!")
    print("Try to guess the target word.")# Hint: {game._words[0]}")
    while game.max_guesses > 0:
        guess = input("Enter your guess: ")
        result = game.add_guess(guess)
        correct_word = True

        for word_result in result.word_results:
            for guess_letter, letter_result in zip(guess, word_result.letter_results, strict=True):
                if letter_result.value == LetterResult.CORRECT.value:
                    print(guess_letter, end=" ")
                elif letter_result.value == LetterResult.MISPLACED.value:
                    print(f"{guess_letter}?", end=" ")
                    correct_word = False
                else:
                    print("_", end=" ")
                    correct_word = False

            if correct_word:
                print("\nCongratulations! You've guessed the word!")
                break
            print()
        if correct_word:
            break


if __name__ == "__main__":
    main()
