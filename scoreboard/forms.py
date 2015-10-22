from django import forms
from .models import Scoreboard, Column, Score, Student
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Hidden, Button, HTML, Div, Field, Row, Fieldset

class ScoreboardForm(forms.ModelForm):
    class Meta:
        model = Scoreboard
        exclude = ('user',)
        
    def __init__(self, *args, **kwargs):
        super(ScoreboardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "scoreboardform"
        #self.helper.add_input(Submit('submit', 'Submit'))
        
        student = Div('student', css_class="col-xs-12", style = "padding:0px;")
        self.helper.layout.pop(4)
        self.helper.layout.insert(4,Fieldset("Select Students",student, Button("createstudentmodal", value="Add a Student", css_class="btn btn-primary btn-sm col-xs-12 ", data_toggle="modal", data_target="#myModal")))
        
        column = Div('column',css_class = "col-xs-12", style="padding:0px;") 
        self.helper.layout.pop(5)
        self.helper.layout.insert(5, Fieldset("Select Column",column, Button("createcolumnmodal", value="Create New Column", css_class="btn btn-primary btn-sm col-xs-12", data_toggle="modal", data_target="#myModal2")))
        
        self.helper.layout.append(Button('btn_createscoreboard', 'Create Scoreboard', css_class='createscoreboard', style="margin-top:15px;"))
        self.helper.layout.append(Hidden(name='btn_createscoreboard', value="btn_createscoreboard"))
        
    def full_clean(self):
        super(ScoreboardForm, self).full_clean()
        if 'student' in self._errors:
            self.cleaned_data['student'] = []
            print("remove student errors")
            del self._errors['student']

        
    
#template
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "studentform"
        
        score = Div('score',css_class = "col-xs-12", style="padding:0px;") 
        self.helper.layout.pop(1)
        self.helper.layout.insert(1, Fieldset("Select Score",score, Button("createscoremodal", value="Add a New Score", css_class="btn btn-primary btn-sm col-xs-12", data_toggle="modal", data_target="#myModal3")))
        
        
        self.helper.layout.append(Hidden(name='btn_createstudent', value="btn_createstudent"))
        self.helper.layout.append(Button('btn_createstudent', 'Create Student', css_class='createstudent', data_dismiss="modal"))
        

class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(ColumnForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "columnform"
        
        self.helper.layout.append(Hidden(name='btn_createcolumn', value="btn_createcolumn"))
        self.helper.layout.append(Button('btn_createcolumn', 'Create Column', css_class='createcolumn', data_dismiss="modal"))
        
        
class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ScoreForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "scoreform"
        self.helper.layout.append(Hidden(name='btn_createscore', value="btn_createscore"))
        self.helper.layout.append(Button('btn_createscore', 'Create Score', css_class='createscore', data_dismiss="modal"))

class ScoreboardFormUpdate(forms.ModelForm):
    class Meta: 
        model = Scoreboard
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super(ScoreboardFormUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "scoreboardformupdate"
        
        student = Div('student', css_class="col-xs-12", style = "padding:0px;")
        self.helper.layout.pop(4)
        self.helper.layout.insert(4,Fieldset("Select Students",student, Button("createstudentmodal", value="Add a Student", css_class="btn btn-primary btn-sm col-xs-12 ", data_toggle="modal", data_target="#myModal")))
        
        column = Div('column',css_class = "col-xs-12", style="padding:0px;") 
        self.helper.layout.pop(5)
        self.helper.layout.insert(5, Fieldset("Select Column",column, Button("createcolumnmodal", value="Create New Column", css_class="btn btn-primary btn-sm col-xs-12", data_toggle="modal", data_target="#myModal2")))
        
        self.helper.add_input(Submit('submit', 'Update'))

class StudentFormUpdate(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(StudentFormUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "studentformupdate"
        score = Div('score',css_class = "col-xs-12", style="padding:0px;") 
        self.helper.layout.pop(1)
        self.helper.layout.insert(1, Fieldset("Select Score",score, Button("createscoremodal", value="Add a New Score", css_class="btn btn-primary btn-sm col-xs-12", data_toggle="modal", data_target="#myModal")))
        self.helper.add_input(Submit('submit', 'Update'))        