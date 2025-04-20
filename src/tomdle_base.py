import abc
import enum

import pydantic


class LetterResult(enum.Enum):
    CORRECT = "correct"
    INCORRECT = "incorrect"
    MISPLACED = "misplaced"

class WordResult(pydantic.BaseModel):
    letter_results: list[LetterResult]

class GuessResult(pydantic.BaseModel):
    word_results: list[WordResult]


class TomdleBase(abc.ABC):
    @abc.abstractmethod
    def add_guess(self, guess: str) -> GuessResult:
        pass
