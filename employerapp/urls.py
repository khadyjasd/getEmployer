from django.urls import path
from .views import *

urlpatterns = [
    path('dyja', dyja),
    path('showdyja', showdyja),
    path('', showdyja),
    path('deletedyja/<str:pk>', deletedyja),
    path('editdyja/<str:pk>', editdyja), 
    path('updatedyja/<str:pk>', updatedyja), 
]
