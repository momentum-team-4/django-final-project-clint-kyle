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
    path('admin/', admin.site.urls),  # admin
    path('', habits_views.habits_list, name='habits_list'),  # main/list
    path('habits/<int:pk>/', habits_views.habits_detail,
         name='habits_detail'),  # details
    path('habits/create/', habits_views.habits_create,
         name='habits_create'),  # habits_create
    path('habits/update/<int:pk>/',
         habits_views.habits_update, name='habits_update'),  # habits_update
    # path('habits/search/', habits_views.habits_search, name='habits_search'),
    path('habits/delete/<int:pk>/',
         habits_views.habits_delete, name='habits_delete'),
    path('habits/daily_entry/<int:pk>/',
         habits_views.daily_entry, name='daily_entry'),
    path('users/create/', users_views.users_create,
         name='users_create'),  # create account
    path('users/login/', users_views.users_login, name='users_login'),  # login
    path('users/logout/', users_views.users_logout, name='users_logout')  # logout
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
