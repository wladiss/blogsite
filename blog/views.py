from django.shortcuts import render
from .models import Post

# Write your views here
def index(request):
    post = Post.objects.all().order_by('-fecha')
    return render(request, 'index.html', {'post':post})