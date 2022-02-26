from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=250) #Имя
    email = models.EmailField(max_length = 254) #Почта
    text = models.TextField(blank=True) #Текст
    status = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #Статус(1-5)
    done = models.BooleanField(default=False) #Сделано
    byadmin = models.BooleanField(default=False) #Отредактировано админом