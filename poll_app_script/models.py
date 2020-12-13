from django.db import models

# Create your models here.
class Question(models.Model):
    name = models.TextField(max_length=500,blank=False)
    choice1 = models.CharField(max_length=30,blank=True)
    choice2 = models.CharField(max_length=30,blank=True)
    choice3 = models.CharField(max_length=30,blank=True)
    choice4 = models.CharField(max_length=30,blank=True)
    choice5 = models.CharField(max_length=30,blank=True)
    choice6 = models.CharField(max_length=30,blank=True)
    choice7 = models.CharField(max_length=30,blank=True)
    choice8 = models.CharField(max_length=30,blank=True)
    choice9 = models.CharField(max_length=30,blank=True)
    choice10 = models.CharField(max_length=30,blank=True)
    choice11 = models.CharField(max_length=30,blank=True)
    choice12 = models.CharField(max_length=30,blank=True)
    choice13 = models.CharField(max_length=30,blank=True)
    choice14 = models.CharField(max_length=30,blank=True)
    choice_answer_1 = models.IntegerField(default=0)
    choice_answer_2 = models.IntegerField(default=0)
    choice_answer_3 = models.IntegerField(default=0)
    choice_answer_4 = models.IntegerField(default=0)
    choice_answer_5 = models.IntegerField(default=0)
    choice_answer_6 = models.IntegerField(default=0)
    choice_answer_7 = models.IntegerField(default=0)
    choice_answer_8 = models.IntegerField(default=0)
    choice_answer_9 = models.IntegerField(default=0)
    choice_answer_10 = models.IntegerField(default=0)
    choice_answer_11 = models.IntegerField(default=0)
    choice_answer_12 = models.IntegerField(default=0)
    choice_answer_13 = models.IntegerField(default=0)
    choice_answer_14 = models.IntegerField(default=0)
    choice_count = models.IntegerField(default=2,blank=True)
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
    def __str__(self):
        return self.name

        
        
