from django.urls import path
from .views import index, add, update, delete

urlpatterns = [
    path('', index, name='home'),
    path('add', add, name='add'),
    path('update/<int:todo_id>', update, name='update'),
    path('delete/<int:todo_id>', delete, name='delete'),
]
