from django.contrib import admin


from .models import News, Portal
# Register your models here.

admin.site.register([News, Portal])
