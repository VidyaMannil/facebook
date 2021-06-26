from django.urls import path
from. import views

urlpatterns=[
    path('fbpage',views.myfb,name='myfb')
]