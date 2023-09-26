from django.urls import path
from main.views import index

urlpatterns = [
    path('', (index)),
    path('about/', (views.about))
]