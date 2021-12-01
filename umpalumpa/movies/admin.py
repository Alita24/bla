from django.contrib import admin

# Register your models here.
from movies.models import Movie, Director, Review

admin.site.register(Movie) 
admin.site.register(Director)
admin.site.register(Review)