import json
from django.http import HttpResponse
from .models import News, Portal
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer



def index(request):
  return HttpResponse('Hello world')

def newsList(request):
  news = News.objects.all()
  return render(request, 'portal/list.html', {'news': news})

def news(request, title):
  return render(request, 'portal/news.html', {'title': title})


def news_view(APIView):
  news = News.objects.all()
  return HttpResponse(str(news))




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



#==============================================
#==============================================
#++++++++++++++++++++++++++++++++++++++++
#jeito medio 
#++++++++++++++++++++++++++++++++++++++++




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
#==============================================
#==============================================
#++++++++++++++++++++++++++++++++++++++++
#jeito mais dificil
#++++++++++++++++++++++++++++++++++++++++



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
#==============================================