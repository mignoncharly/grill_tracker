from django.contrib import admin
from django.urls import path, include
from tracker import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Redirects homepage to category list
    path('tracker/', include('tracker.urls')),  # Includes the tracker app URLs
    path('admin/', admin.site.urls),  # Django admin URL
]
