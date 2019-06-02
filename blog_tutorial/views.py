from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog_tutorial/post_list.html', {})