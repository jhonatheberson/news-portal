from django.urls import path
from .import views

app_name = 'portal'

# routes of my application

urlpatterns = [
    # main router
    path('', views.newsList, name="news-list"),
    # router for more details of the news
    path('news/<int:id>', views.newsView, name="news-view"),
]
