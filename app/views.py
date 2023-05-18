from django.shortcuts import render
from app.forms import*
# Create your views here.
from django.views.generic import FormView
from django.http import HttpResponse

class cbvform(FormView):
    form_class=SchoolForm
    template_name='cbvform.html'

    def form_valid(self, form):
        form.save()
        return HttpResponse('data inserted successfuly')


