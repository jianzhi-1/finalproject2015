from django.db import models
from django.core.urlresolvers import reverse
from accounts.models import UserProfile

# Create your models here

class Column(models.Model):
    
    header = models.CharField(max_length = 255)
    color = models.CharField(max_length=50, default = "yellow")
    fontcolor = models.CharField(max_length=50, default = "black")
    weight = models.FloatField(null = True, blank = True)
    denominator = models.IntegerField()
    
    def __unicode__(self):
        return self.header

class Scoreboard(models.Model):
    user = models.ForeignKey(UserProfile, blank=True, null=True)
    name = models.CharField(max_length = 255)
    sid = models.IntegerField(blank = True, null = True)
    description = models.TextField()
    color = models.CharField(max_length=50, default = "yellow")
    fontcolor = models.CharField(max_length=50, default = "black")
    
    #other relationships
    student = models.ManyToManyField('Student', related_name="scoreboard", null=True, blank=True)
    column = models.ManyToManyField('Column', related_name="scoreboard", null = True, blank = True)
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("scoreboard_detail", kwargs={"pk":self.pk})

class Score(models.Model):
    
    numerator = models.IntegerField()
    column = models.ForeignKey(Column, blank=True, null=True)
    
    def __unicode__(self):
        return self.column.header + ": " + str(self.numerator)


class Student(models.Model):
    
    name = models.CharField(max_length = 255)
    score = models.ManyToManyField('Score', related_name="student", null=True, blank=True)
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("student_detail", kwargs={"pk":self.pk})
