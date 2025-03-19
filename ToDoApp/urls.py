from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.add_task,name= 'add_task'),
    path('complete_task/<int:pk>',views.complete_task,name='complete_task'),
    path('undone_task/<int:pk>',views.undone_task,name='undone_task'),
    
]
