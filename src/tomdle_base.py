import abc
import enum

import pydantic


class LetterResult(enum.Enum):
    """Outcomes for each letter in a guess word."""

    CORRECT = "correct"
    INCORRECT = "incorrect"
    MISPLACED = "misplaced"

class WordResult(pydantic.BaseModel):
    """Result of comparing guess word to target word."""

    letter_results: list[LetterResult]
    target_word: str

class GuessResult(pydantic.BaseModel):
    """Result of comparing guess word to all target words."""

    word_results: list[WordResult]


class TomdleBase(abc.ABC):
    """Base class for the Tomdle game."""

    @abc.abstractmethod
    def add_guess(self, guess: str) -> GuessResult:
        """Add a guess to the game and return the result.

        Args:
            guess (str): The guessed word.

        Returns:
            GuessResult: The result of the guess.

        """
