from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from .models import Position

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'optiontools/index.html'

    def get_queryset(self):
    	""" Return all entered positions """
    	return Position.objects.order_by('created')