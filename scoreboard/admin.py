from django.contrib import admin
from .models import Scoreboard, Student, Column, Score
# Register your models here.
admin.site.register(Scoreboard)
admin.site.register(Student)
admin.site.register(Column)
admin.site.register(Score)