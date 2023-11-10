from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('', include('akanapp.urls')),  # Include your app's URLs
]




