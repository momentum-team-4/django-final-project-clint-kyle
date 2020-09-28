"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from habits import views as habits_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', habits_views.habits_list, name='habits_list')
    path('habits/<int:pk>/', habits_views.habits_detail, name='habits_detail'),
    path('habits/create/', habits_views.habits_create, name='habits_create'),
    path('habits/update/<int:pk>/', habits_views.habits_update, name='habits_update'),
    path('habits/search/', habits_views.habits_search, name='habits_search'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
