from django.db import models

# Create your models here.
class Choices(models.Model):
    options=models.TextField()
    def __str__(self):
        return self.options
class YesNo(models.Model):
    answer = models.CharField(max_length=10)
    def __str__(self):
        return self.answer


class Profile(models.Model):
    email=models.EmailField(max_length=100)
    number=models.IntegerField()
    answer=models.ManyToManyField(YesNo)
    q3 = models.CharField(max_length=200)
    q4 = models.CharField(max_length=200)
    option = models.ManyToManyField(Choices)
    q6 = models.CharField(max_length=200)

    def __str__(self):
        return self.email


# class Pro(models.Model):
#     email = models.EmailField(max_length=100)
#     number=models.IntegerField()
#     q1 = models.BooleanField()
#     q3 = models.CharField(max_length=200)
#     q4 = models.CharField(max_length=200)
#
#     q6 = models.CharField(max_length=200)