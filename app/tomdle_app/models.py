from django.db import models


class Answer(models.Model):
    answer_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.answer_text

class Guess(models.Model):
    guess_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")
    is_correct = models.BooleanField(default=False)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.guess_text
