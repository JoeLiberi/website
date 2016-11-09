from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views import generic
from optiontools.models import Position
from blog.models import Post


class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'list_of_objs'

    def get_queryset(self):
    	pos = list(Position.objects.order_by('created')[:5])
    	posts = list(Post.objects.order_by('created')[:5])
    	return [posts, pos]