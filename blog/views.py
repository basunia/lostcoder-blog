from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Post
from django.contrib.auth.models import User
# Create your views here.

posts = [
    {
        'author': 'Corey MS',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    },
    {
        'author': 'John Assam',
        'title': 'Blog post 3',
        'content': 'Third post content',
        'date_posted': 'August 29, 2018'
    }
]

def home(request : HttpRequest):
    posts = Post.objects.all()
    print('My post', posts)
    context = {
        'posts': posts
        }
    return render(request, 'blog/home.html', context)
 
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def register(request: HttpRequest):
    name = request.GET.get('name')
    user = User.objects.create_user(username=name)
    # user.is_staff = request.GET.get('is_stuff')
    user.is_superuser = request.GET.get('is_supper')
    user.save()
    return HttpResponse(f'Registering successfull, {name}')
    
def del_user(request: HttpRequest):
    try: 
        name = request.GET.get('name')
        print(f'dfdfd {name}')
        user = User.objects.first()
        print(f'Users {user}')
        user.delete()
        return HttpResponse(f'Delete user successfull {name}')
    except User.DoesNotExist:
        return HttpResponse(f'User not found {name}')
    except Exception as e:
        return HttpResponse(e.__str__())

    