from django.urls import path
from .views import IndexView, NewsView, BiographyView
urlpatterns = [
    path('', IndexView.as_view()),
    path('news/', NewsView.as_view()),
    path('biography/', BiographyView.as_view()),
]