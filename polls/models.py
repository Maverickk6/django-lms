from django.db import models

# Create your models here.

class Questions(models.Model):
    question_text = models.CharField(max_length=255)
    question_description = models.CharField(max_length=255, default="Basic Description")
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.question_text


class Choices(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.question} ---> {self.choice_text}"

   

   