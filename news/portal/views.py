


#==============================================
#++++++++++++++++++++++++++++++++++++++++
#jeito facil 
#++++++++++++++++++++++++++++++++++++++++




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
# #from django.http import HttpResponse
# #from rest_framework.decorators import api_view
# from rest_framework.response import Response
# #from rest_framework.views import APIView

# # @api_view(['GET', 'POST'])
# # def news_view(request):
# #     if request.method == 'GET':
# #         news = News.objects.all()
# #         output = [{
# #             'title': new.title,
# #             'portal': new.portal
# #         } for new in news]
# #     elif request.method == 'POST':
# #         news = News.objects.create(title=request.data.get('title'),
# #                                    portal=request.data.get('portal'))
# #         output = {
# #             'title': new.title,
# #             'portal': new.portal
# #         }

# #     return Response(output)
#==============================================