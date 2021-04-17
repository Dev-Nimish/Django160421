from django.urls import path
from app1 import views

app_name = "app1"


urlpatterns = [
    path('',views.page1, name = 'page1'),
    path('page2/<data>',views.page2, name = 'page2'),
]
