from django.shortcuts import render

posts = [
    {
        'author': 'John and Johnson',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 22 2020'
    },
    {
        'author': 'DoDo',
        'title': 'Blog Post 2',
        'content': 'Second post thing',
        'date_posted': 'August 22 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
