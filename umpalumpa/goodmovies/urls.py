"""goodmovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movies import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')), # <-- nowe
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world),
    path("main/", views.main, name='main'),
    path("profile/", views.kingdom),
    path("login/", views.login, name='login'),
    path("",views.index),
    path("subpage/",views.subpage, name="subpage"),
    path('films/',views.list_films, name='list_films'),
    path('list-review/',views.list_review, name='list_review'),
    path('films/<int:movie_id>',views.movie_detail , name='movie_detail'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('accounts/signup/', views.user_signup, name="user_signup"),
    path('accounts/signup_complete/', views.signup_complete, name="signup_complete"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
