import abc
import enum
import pydantic

class LetterResult(enum.Enum):
    CORRECT = "correct"
    INCORRECT = "incorrect"
    MISPLACED = "misplaced"
    

class GuessResult(pydantic.BaseModel):
    letter_results: list[LetterResult]


class TomdleBase(abc.ABC):
    def __init__(self):
        self._guesses = []

    @abc.abstractmethod
    def add_guess(self, guess: str) -> GuessResult:
        pass
