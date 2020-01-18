from django.urls import path

from .import views

app_name = 'portal'

urlpatterns = [
    path('', views.newsList, name="news-list"),
    path('news/<int:id>', views.newsView, name="news-view"),
    path('newNews/', views.newNews, name="new-News"),
]
