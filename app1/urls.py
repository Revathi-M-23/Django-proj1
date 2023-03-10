from app1.views import *
from django.urls import path
app_name='smthng'
urlpatterns=[
    path('MSD/',MSD,name='MSD'),
    path('Raina/',Raina,name='Raina')
]