from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('person/<int:person_id>', views.person, name='person'),
]