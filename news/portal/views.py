from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse
from django.contrib import messages

from .forms import NewForm

from .models import News, Portal


def newsList(request):

    search = request.GET.get('search')

    if search:
        news = News.objects.filter(title__icontains=search)
    else:

        news_list = News.objects.all().order_by('-create_at')

        paginator = Paginator(news_list, 7)

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
    news = get_object_or_404(News, pk=id)
    return render(request, 'portal/news.html', {'news': news})


def newNews(request):
    if request.method == 'POST':
        form = NewForm(request.POST)

        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            return redirect('/')


# #==============================================
# #++++++++++++++++++++++++++++++++++++++++
# #jeito facil
# #++++++++++++++++++++++++++++++++++++++++
# from rest_framework import viewsets
# from .serializers import NewsSerializer
# from django.shortcuts import render

# from .models import News

# class NewsViewSet(viewsets.ModelViewSet):
#   serializer_class = NewsSerializer
#   queryset = News.objects.all()


# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class Index(viewsets.ModelViewSet):
#   renderer_classes = TemplateHTMLRenderer
#   template_name = 'templates/index.html'

#   def get(self, request):
#     queryset = News.objects.all()

#     return Response(['news', queryset])


# ==============================================
# ==============================================
# ++++++++++++++++++++++++++++++++++++++++
# jeito medio
# ++++++++++++++++++++++++++++++++++++++++


# from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView

# from .serializers import NewsSerializer

# from .models import News


# # Create your views here.

# class NewsApiView(ListAPIView):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer
#     # def get(self, request):
#     #     news = News.objects.all()
#     #     serializer = NewsSerializer(news, many=True)
#     #     return Response(serializer.data)

#     # def post(self, request):
#     #     return Response()

# class NewsCreateView(CreateAPIView):
#   queryset = News.objects.all()
#   serializer_class = NewsSerializer


# class NewsUpdateView(UpdateAPIView):
#   queryset = News.objects.all().select_related('portal')
#   serializer_class = NewsSerializer


# news_view = NewsApiView.as_view()
# news_create_view = NewsCreateView.as_view()
# news_update_view = NewsUpdateView.as_view()
# ==============================================
# ==============================================
# ++++++++++++++++++++++++++++++++++++++++
# jeito mais dificil
# ++++++++++++++++++++++++++++++++++++++++


# import json
# from django.http import HttpResponse
# from .models import News, Portal
# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.renderers import TemplateHTMLRenderer
# eturn HttpResponse(str(news))


# def news_view(APIView):
#   news = News.objects.all()
#   return HttpResponse(str(news))


# @api_view(['GET', 'POST'])
# def news_view(request):
#     if request.method == 'GET':
#         news = News.objects.all()
#         output = [{
#             'title': new.title,
#             'portal': new.portal
#         } for new in news]
#     elif request.method == 'POST':
#         news = News.objects.create(title=request.data.get('title'),
#                                    portal=request.data.get('portal'))
#         output = {
#             'title': new.title,
#             'portal': new.portal
#         }

#     return Response(output)
# ==============================================
