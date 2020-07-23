from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('import_metadata', views.import_metadata, name='import_metadata')
]