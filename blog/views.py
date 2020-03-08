from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
<<<<<<< HEAD
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
=======
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})
>>>>>>> 2667311d7550a8cdcc58d77ab7ccef8f669e6281

