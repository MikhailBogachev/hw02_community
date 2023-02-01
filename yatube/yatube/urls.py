from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('posts.urls')),
    #path('group/<slug:slug>/', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]
