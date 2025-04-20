from english_words import get_english_words_set

from tomdle_base import GuessResult, LetterResult, TomdleBase, WordResult

WEB2LOWERSET = get_english_words_set(["web2"], lower=True, alpha=True)

class Tomdle(TomdleBase):
    """Tomdle game implementation.

    Stores game state and allows guessing target words.
    """

    def __init__(self, word_count: int = 1, word_length: int = 5, max_guesses: int = 6) -> None:
        self._guesses = []
        self._words = []
        self._word_count = word_count
        self._word_length = word_length
        self.max_guesses = max_guesses

        self._generate_words(word_count, word_length)

    def _generate_words(self, count: int, length: int) -> None:
        self._words = [self._generate_word(length) for _ in range(count)]

    def _generate_word(self, length: int) -> str:
        word = ""
        while len(word) != length:
            word = WEB2LOWERSET.pop()

        return word

    def _compare_words(self, guess: str, target: str) -> WordResult:
        if len(guess) != len(target):
            m = "Guess and target words must be of the same length."
            raise ValueError(m)

        letter_results = []
        for idx, letter in enumerate(guess):
            if letter == target[idx]:
                letter_results.append(LetterResult.CORRECT)
            elif letter in target:
                letter_results.append(LetterResult.MISPLACED)
            else:
                letter_results.append(LetterResult.INCORRECT)

        return WordResult(letter_results=letter_results, target_word=target)

    def add_guess(self, guess: str) -> GuessResult:
        """Add a guess to the game and return the result.

        Args:
            guess (str): The guessed word.

        Returns:
            GuessResult: The result of the guess.

        """
        if len(guess) != self._word_length:
            m = f"Guess must be {self._word_length} letters long."
            raise ValueError(m)
        if not guess.isalpha():
            m = "Guess must only contain letters."
            raise ValueError(m)
        if len(self._guesses) >= self.max_guesses:
            m = "Maximum number of guesses reached."
            raise ValueError(m)
        if guess in self._guesses:
            print("Guess has already been made.")
        if guess not in WEB2LOWERSET:
            print("Guess is not a valid word.")

        self._guesses.append(guess)

        word_results = []
        for idx, _ in enumerate(self._words):
            word_results.append(self._compare_words(guess, self._words[idx]))

        return GuessResult(word_results=word_results)
