from django.urls import path
from .views import *

urlpatterns =[
    path('',Clas1,name='Clas1'),
    path('Clas/<str:title>',Clas2,name='Clas2'),
    path('clas3/',Clas3,name='Clas3'),
]