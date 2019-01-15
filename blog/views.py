from django.shortcuts import render
from django.http import HttpResponse        
# Create your views here.

posts = [
    {
        'author': 'CoreyInDaHouse',
        'title':'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'JaneBro',
        'title':'Blog 2',
        'content': 'First Post Content',
        'date_posted': 'August 29, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About',})