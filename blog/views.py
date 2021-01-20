from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse

# Create your views here.

"""
posts = [
  {
    'author': 'Corey Smith',
    'title': 'Blog Post 1',
    'content': 'First post 1',
    'date posted': 'August 21st 1952'
  },
    {
    'author': 'Brian Mester',
    'title': 'Blog Post 2',
    'content': 'Second post 2',
    'date posted': 'March 21st 2010'
  }
]
"""

# Handlses the processing of requests from the browser. <Step 1>
# Provides the HTML code
# Create urls.py in Blog folder <Step 2>

# def render(
# request: HttpRequest, // request
# template_name: Union[str,Sequence[str]], 
# context: Optional[Mapping[str, Any]]=..., content_type: Optional[str]=..., 
# status: Optional[int]=..., using: Optional[str]=...)
 
# path as defined in 2nd argument is relative to the templates folder
def home (request):
  context = {
    'posts': Post.objects.all()
  }
  return render(request, 'blog/home.html', context)
#  return HttpResponse('<h1>Blog Home</h1>')   // alternative


def about (request):
  return render(request, 'blog/about.html', { 'title': 'About'})

  