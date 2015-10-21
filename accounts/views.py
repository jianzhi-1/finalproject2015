from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import UserProfile
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from accounts.forms import UserForm, UserProfileForm

def registration(request):


    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'accounts/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )
            

class Profile(TemplateView):
    user_form_class = UserForm
    profile_form_class = UserProfileForm
    template_name = 'accounts/profile.html'
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        #Added curruser so that profile picture of curruser can be rendered.
        instance = UserProfile.objects.get(user=request.user)
        kwargs.setdefault('curruser', instance)
        kwargs.setdefault("user_form", self.user_form_class(instance=instance.user))
        kwargs.setdefault("profile_form", self.profile_form_class(instance=instance))
        return super(Profile, self).get(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and PublicForm.
        form_args = {
            'data': request.POST,
        }
        user_form = UserForm(data=request.POST, instance=request.user)
        instance = UserProfile.objects.get(user=request.user)
        kwargs.setdefault('curruser', instance)
        profile_form = UserProfileForm(data=request.POST, instance=instance)
        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now sort out the Public instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the Public model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            # Now we save the Public model instance.
            profile.save()
    
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors
        kwargs.setdefault("user_form", self.user_form_class(instance=instance.user))
        kwargs.setdefault("profile_form", self.profile_form_class(instance=instance))
        return super(Profile, self).get(request, *args, **kwargs)