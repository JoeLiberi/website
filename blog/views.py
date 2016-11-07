from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
    	""" Return the last five published blog entries """
    	return Post.objects.order_by('created')[:5]

class DetailView(generic.DetailView):
	model = Post
	template_name = 'blog/detail.html'

# def index(request):
# 	latest_post_list = Post.objects.order_by('created')[:5]
# 	context = {'latest_post_list': latest_post_list}
# 	return render(request, 'blog/index.html', context)
	