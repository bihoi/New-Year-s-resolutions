from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from .models import YourResolutions



class IndexView(generic.ListView):
    template_name = 'resolution/index.html'

    def get_queryset(self):
        return YourResolutions.objects.all()


class DetailView(generic.DetailView):
    model = YourResolutions
    template_name = 'resolution/detail.html'



class ResolutionCreate(CreateView):
    model = YourResolutions
    fields = ['resolution_title', 'resolution_category', 'resolution_year']


class ResolutionUpdate(UpdateView):
    model = YourResolutions
    fields = ['resolution_title', 'resolution_category', 'resolution_year']


class ResolutionDelete(DeleteView):
    model = YourResolutions
    success_url = reverse_lazy('resolution:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'resolution/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # add user to database
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if cridentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('resolution:index')
        return render(request, self.template_name, {'form':form})
