from django.urls import path
from .views import home_view, edit_people

urlpatterns = [
    path('', home_view, name="home"),
    path('formset/', edit_people, name="edit_person"),
    path('formset/', edit_people, name="edit_person"),
]
