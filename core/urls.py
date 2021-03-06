from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='front-end/index.html')),
]