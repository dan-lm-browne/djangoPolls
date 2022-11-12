from django.db import models

# These are data models i.e. fields and behaviour of the data
# They are represented by classes
# Any changes or additional models need to be updated in the database so that
# it is aware of new fields. SO, go to the manage.py console (ctrl+Alt+R) and type:
# makemigrations polls (to create the migration file)
# migrate (to update sql)


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)