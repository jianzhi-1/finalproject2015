from django.db import models
from django.core.urlresolvers import reverse
from accounts.models import UserProfile

# Create your models here

class Column(models.Model):
    
    header = models.CharField(max_length = 255)
    color = models.CharField(max_length=50, default = "yellow")
    fontcolor = models.CharField(max_length=50, default = "black")
    
    def __unicode__(self):
        return self.header

class Scoreboard(models.Model):
    user = models.ForeignKey(UserProfile, blank=True, null=True)
    name = models.CharField(max_length = 255)
    sid = models.CharField(max_length = 255)
    description = models.TextField()
    color = models.CharField(max_length=50, default = "yellow")
    fontcolor = models.CharField(max_length=50, default = "black")
    
    #other relationships
    student = models.ManyToManyField('Student', related_name="scoreboard", null=True, blank=True)
    columns = models.ManyToManyField('Column', related_name="scoreboard", null = True, blank = True)
    
    def __unicode__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("scoreboard_detail", kwargs={"pk":self.pk})


class Score(models.Model):
    
    numerator = models.CharField(max_length = 10)
    denominator = models.CharField(max_length = 10)
    column = models.ForeignKey(Column, blank=True, null=True)
    
class Student(models.Model):
    
    name = models.CharField(max_length = 255)
    points = models.ForeignKey(Score, blank=True, null=True)
    
    def __unicode__(self):
        return self.name
