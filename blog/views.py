from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

def detail(reguest, post_id):
	return HttpResponse("You're looking at the question %s" % question_id)
	