from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse
from django.contrib import messages
from .forms import NewForm
from .models import News, Portal


def newsList(request):
    """
    function responsible for performing the 
    search and bringing news from the database end paginator the page
    """
    search = request.GET.get('search') # check if the form has something in it

    if search:
        news = News.objects.filter(title__icontains=search) # search the content in the database
    else:

        news_list = News.objects.all().order_by('-create_at') # shows all news from the bank in order of the most recent

        paginator = Paginator(news_list, 7) #shows 7 news per page

        try:
            page = int(request.GET.get('page', '1'))
        except ValueError:
            page = 1

        try:
            news = paginator.page(page)
        except (EmptyPage, InvalidPage):
            news = paginator.page(paginator.num_pages)

    return render(request, 'portal/list.html', {'news': news})


def newsView(request, id):
    """
    function that brings the other news fields
    """
    news = get_object_or_404(News, pk=id)
    return render(request, 'portal/news.html', {'news': news})