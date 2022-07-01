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





# class Questions(models.Model):
#     q1 = models.CharField(max_length=255)

# class Pro(models.Model):
#     email = models.EmailField(max_length=100)
#     number=models.IntegerField()
#     q1 = models.BooleanField(verbose_name='yes,no')
#     q2 = models.BooleanField(verbose_name='yes,no')
#     q3 = models.CharField(max_length=200)
#     q4 = models.CharField(max_length=200)
#     q5 = models.BooleanField()
#     q6 = models.BooleanField()
#     q7 = models.BooleanField()
#     q8 = models.BooleanField()
#     q9 = models.BooleanField()
#     q10 = models.BooleanField()
#     q11= models.BooleanField()
#     q12 = models.BooleanField()
#     q13 = models.BooleanField()
#     q14 = models.BooleanField()
#     q15 = models.BooleanField()
#     q16 = models.BooleanField()
#     q17 = models.BooleanField()
#     q18 = models.BooleanField()
#     q19 = models.BooleanField()
#     q20 = models.BooleanField()
#     q21 = models.BooleanField()
#     q22 = models.BooleanField()
#     last = models.CharField(max_length=200)