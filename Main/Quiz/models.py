from django.db import models
# Create your models here.

class QuizModel(models.Model):
    method=models.CharField(blank=True,max_length=20,choices=[("With Spaces","With Spaces"),("Without Spaces","Without Spaces"),("Characteres","Characteres"),("Words","Words"),("Sentences","Sentences")])
    text=models.TextField(blank=True)
    result=models.CharField(blank=True,max_length=100)

class QuizChooseModel(models.Model):
    whichQ=models.CharField(max_length=20,choices=[("Geonra1","Geonra1"),("Geonra2","Geonra2")])
