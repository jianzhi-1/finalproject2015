import re
import json

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q

from django.views.generic import View
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect

from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Scoreboard, Student, Column, Score

from .forms import ScoreboardForm, StudentForm, ColumnForm, ScoreForm, ScoreboardFormUpdate, StudentFormUpdate

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import UserProfile
from django.core.serializers.json import DjangoJSONEncoder

from django.http import Http404

#table
from django.shortcuts import render
from django_tables2   import RequestConfig
from scoreboard.models  import Student
from scoreboard.tables  import StudentTable
from django.template import RequestContext


class home(TemplateView):
    template_name = 'scoreboard/home.html'
    def dispatch(self, *args, **kwargs):
        return super(home, self).dispatch(*args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super(home, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            if UserProfile.objects.filter(user=self.request.user).exists():
                context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
    
def notfound(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
    
def credits(request):
    return render(request, 'scoreboard/credits.html')
    
def people(request, score_id):
    if request.method == 'GET':
        scoreboard = score_id
        listofscore = Scoreboard.objects.all()
        for score in listofscore:
            if scoreboard == score.sid:
                table = StudentTable(score.student.objects.all())
                RequestConfig(request).configure(table)
                return render(request, 'scoreboard/people.html', {'table': table})
        
        if scoreboard == "debug":
            table = StudentTable(Student.objects.all())
            RequestConfig(request).configure(table)
            return render(request, 'scoreboard/people.html', {'table': table})
        
        return render(request, 'scoreboard/findscore.html')
    else:
        print(request.POST.values())
        return redirect('/people/'+request.POST.values()[1])
        
def spectator(request):
    scoreboards = Scoreboard.objects.all()
    return render(request, 'spectator.html', {'scoreboards':scoreboards})
    

class ScoreboardList(ListView):
    model = Scoreboard
    
    def get_queryset(self):
        curruser = UserProfile.objects.get(user=self.request.user)
        return Scoreboard.objects.filter(user=curruser)
        
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ScoreboardList, self).dispatch(*args, **kwargs)
            
    def get_context_data(self, **kwargs):
        context = super(ScoreboardList, self).get_context_data(**kwargs)
        #provided so that the avatar can be displayed in base.html
        if self.request.user.is_authenticated():
            context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context

class ScoreboardDetail(DetailView):
    model = Scoreboard
    #@method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ScoreboardDetail, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(ScoreboardDetail, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
        
class ScoreboardSpectator(ListView):
    model = Scoreboard
    #@method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ScoreboardSpectator, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(ScoreboardSpectator, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
        
class ScoreboardUpdate(UpdateView):
    model = Scoreboard
    form_class = ScoreboardFormUpdate
    student_form_class = StudentForm
    column_form_class = ColumnForm
    score_form_class = ScoreForm
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ScoreboardUpdate, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        kwargs.setdefault("createstudent_form", self.student_form_class())
        kwargs.setdefault("createcolumn_form", self.column_form_class())
        kwargs.setdefault("createscore_form", self.score_form_class())
        context = super(ScoreboardUpdate, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ScoreboardUpdate, self).get_object()
        if not UserProfile.objects.get(user=self.request.user) == obj.user:
            raise Http404
        return obj

class StudentDetail(DetailView):
    model = Student
    #@method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentDetail, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(StudentDetail, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context

class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentFormUpdate
    score_form_class = ScoreForm
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(StudentUpdate, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        kwargs.setdefault("createscore_form", self.score_form_class())
        context = super(StudentUpdate, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
        
class MyView(TemplateView):

    student_form_class = StudentForm
    column_form_class = ColumnForm
    score_form_class = ScoreForm
    scoreboard_form_class = ScoreboardForm
    template_name = "scoreboard/scoreboard_hybrid.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyView, self).dispatch(*args, **kwargs)
    
    
    def get(self, request, *args, **kwargs):

        kwargs.setdefault("createstudent_form", self.student_form_class())
        kwargs.setdefault("createcolumn_form", self.column_form_class())
        kwargs.setdefault("createscore_form", self.score_form_class())
        kwargs.setdefault("createscoreboard_form", self.scoreboard_form_class())
        
        kwargs.setdefault('curruser', UserProfile.objects.get(user=self.request.user))
        return super(MyView, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form_args = {
            'data': self.request.POST,
        }
        
        print request.POST['form']
        
        if "btn_createscore" in request.POST['form']: 
            form = self.score_form_class(**form_args)
            if not form.is_valid():
                return self.get(request, createscore_form=form)
                
            else:
                form.save() 
                data = Score.objects.all() 
                result_list = list(data.values('id','numerator','denominator','column'))
                return HttpResponse(json.dumps(result_list, cls=DjangoJSONEncoder))
        elif "btn_createscoreboard" in request.POST['form']:
            print "i am in"
            form = self.scoreboard_form_class(**form_args)
            if not form.is_valid():
                print "form not valid"
                return self.get(request,createscoreboard_form=form) 
            else:
                try:
                    #Find out which user is logged in and get the correct UserProfile record.
                    curruser = UserProfile.objects.get(user=self.request.user)
                    obj = form.save(commit=False)
                    obj.user = curruser #Save the note note under that user
                    obj.save() #save the new object
                    
                except Exception, e:
                    print("errors" + str(e))
                response = {'status': 1, 'message':'ok'}
                return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder)) #return to ajax as success with all the new records.
        elif "btn_createstudent" in request.POST['form']:
            print "jjj"
            form = self.student_form_class(**form_args)

            if not form.is_valid():

                return self.get(request, createstudent_form=form)
            else:
                form.save()
                data = Student.objects.all()
                result_list = list(data.values('id','name'))
                return HttpResponse(json.dumps(result_list, cls=DjangoJSONEncoder))
        
        elif "btn_createcolumn" in request.POST['form']: 
            form = self.column_form_class(**form_args)
            if not form.is_valid():
                return self.get(request, createcolumn_form=form)
            else:
                form.save() 
                data = Column.objects.all() 
                result_list = list(data.values('id','header'))
                return HttpResponse(json.dumps(result_list, cls=DjangoJSONEncoder))#return to ajax as success with all the new records.
        
        
            
        return super(MyView, self).get(request)
        
class ScoreboardDelete(DeleteView):
    model = Scoreboard
    success_url = '/list/'
    #success_url = reverse_lazy('listing')
            #url = reverse('detail', args=str(food.id))
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ScoreboardDelete, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(ScoreboardDelete, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
        
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ScoreboardDelete, self).get_object()
        if not UserProfile.objects.get(user=self.request.user) == obj.user:
            raise Http404
        return obj
