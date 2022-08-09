from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

def home(request):
    return render(request, 'blog/index.html')

def blogs(request):
    return render(request, 'blog/blogs.html')

def blogDetail(request, id):
    return render(request, 'blog/blog-details.html',{'id':id})