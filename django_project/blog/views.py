from django.shortcuts import render

posts = [
    {
        'author': 'Karen Villmones',
        'title': 'Blog post no. 1',
        'content': 'First post! Yay!',
        'date_posted': 'August 27, 2018'
    },
        {
        'author': 'Jane Doe',
        'title': 'Bloggie!!',
        'content': 'yey this ma blog',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


# Create your views here.
