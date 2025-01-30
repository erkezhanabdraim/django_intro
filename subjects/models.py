from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.CharField(max_length=200)  # имя и фамилия преподавателя

    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
