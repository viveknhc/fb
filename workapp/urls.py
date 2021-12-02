from django.urls import path
from . import views
urlpatterns=[
    path('workapp/',views.wrkfn,name='workapp'),
]