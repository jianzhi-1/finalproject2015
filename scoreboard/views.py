import re
import json

from django.shortcuts import render
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

#from .forms import FoodForm, RatingForm, RestaurantForm, FoodFormUpdate

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

def home(request):
    return render(request, 'scoreboard/home.html')
    
def notfound(request):
    return render(request, 'scoreboard/notfound.html')
    
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
        return Scoreboard.objects.all()
        
    #@method_decorator(login_required)
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
        
class ScoreboardUpdate(UpdateView):
    model = Scoreboard
    #form_class = ScoreboardFormUpdate
    #success_url = reverse_lazy('listing')
    success_url = '/list/'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ScoreboardUpdate, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(ScoreboardUpdate, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
    
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ScoreboardUpdate, self).get_object()
#        if not UserProfile.objects.get(user=self.request.user) == obj.user:
#            raise Http404
        return obj