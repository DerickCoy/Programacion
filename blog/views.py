from django.shortcuts import render
from django.utils import timezone
# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

