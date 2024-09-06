
from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('contributions/', views.contributions_list, name='contributions_list'),  # New path for contributions
]
