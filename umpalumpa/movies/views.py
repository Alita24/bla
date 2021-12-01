from django.shortcuts import render
# from django.http import HttpResponse
from datetime import datetime
from movies.models import Movie, Review
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def hello_world(request):
    our_context = {"time": datetime.now()}
    return render(request, template_name="hello.html", context=our_context)

def main (request):
    return render(request,template_name="main_avo.html")

def kingdom (request):
    return render(request,template_name="avo.html")

def login (request):
    return render(request,template_name="login2.html")

def index(request):
    return render(request,template_name="main_avo.html")

def subpage(request):
    return render(request,template_name="subpage.html")

def profile_view(request):
    return render(request,template_name="avo.html")

def user_signup(request):
    if request.method == 'POST':
        # przetwarzanie formularzy
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name="registration/signup_complete.html")
    else:
        # nowy formularz, czysty
        form = UserCreationForm()
    return render(request, 
        template_name = 'registration/signup.html', 
        context = {'form': form}
    )
def signup_complete (request):
    return render(request,template_name="registration/signup_complete.html")


def list_films(request):
    my_context = {"movies": Movie.objects.all()}
    return render(request, template_name="list_films.html", context=my_context)

def list_review(request):
    my_context = {"reviews": Review.objects.all()}
    return render(request, template_name="list_review.html", context=my_context)

def movie_detail (request, movie_id):
    my_context = {"movie": Movie.objects.all(movie_id)}
    return render(request, template_name="movie_detail.html", context=my_context)
