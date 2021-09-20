from django.urls import path
from . import views
from .views import LigasListView

urlpatterns = [
    path('hello/', views.say_hello),
    path('leagues/', LigasListView.as_view, name='leagues_list')
]