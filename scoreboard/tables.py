import django_tables2 as tables
from scoreboard.models import Student

class StudentTable(tables.Table):
    name = tables.Column(verbose_name="Name") #heading for table
    class Meta:
        model = Student
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}