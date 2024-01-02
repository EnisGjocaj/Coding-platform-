from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Quiz(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):

        return (f"{self.question} - {self.text} - {self.is_correct}")


class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.question.text} - {self.selected_answer.text}"



class LabScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    attempts = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - Score: {self.score}, Attempts: {self.attempts}"
    