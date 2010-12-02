from django.db import models

class Test(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=255)
    test = models.ForeignKey(Test)

    def __unicode__(self):
        return self.title

class Answer(models.Model):
    title = models.CharField(max_length=255)
    question = models.ForeignKey(Question)
    is_true = models.BooleanField()

    def __unicode__(self):
        return self.title
