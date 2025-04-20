from src.tomdle import Tomdle
from src.tomdle_base import LetterResult, WordResult


def _check_word(guess: str, word_result: WordResult) -> bool:
    print("Target: ", end="")
    correct_word = True
    for guess_letter, letter_result in zip(guess, word_result.letter_results, strict=True):
        if letter_result.value == LetterResult.CORRECT.value:
            print(guess_letter, end=" ")
        elif letter_result.value == LetterResult.MISPLACED.value:
            print(f"{guess_letter}?", end=" ")
            correct_word = False
        else:
            print("_", end=" ")
            correct_word = False

    print("\t", end="")

    if correct_word:
        print("\nCongratulations! You've guessed the word!")
        return True

    return False

def main(word_count: int = 1, word_length: int = 5, max_guesses: int = 6) -> None:
    """Run the Tomdle game."""
    game = Tomdle(word_count=word_count, word_length=word_length, max_guesses=max_guesses)

    print("Welcome to Tomdle!")
    print("Try to guess the target word")
    correct_words: dict[str, bool] = {}
    while game.max_guesses > 0:
        guess = input("Enter your guess: ")
        result = game.add_guess(guess)

        for word_result in result.word_results:
            is_match = _check_word(guess, word_result)
            if is_match or word_result.target_word not in correct_words:
                correct_words[word_result.target_word] = is_match

        if all(correct_words.values()):
            print("Congratulations! You've guessed all the words!")
            break

        print()


if __name__ == "__main__":
    words = int(input("How many words do you want to guess? "))
    word_length = int(input("What is the length of the words? "))
    max_guesses = int(input("How many guesses do you want? "))
    main(words, word_length, max_guesses)
