from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('novo', views.new, name='new'),
    path('<int:todo_id>/', views.detail, name='detail'),
    path('<int:todo_id>/form/', views.form, name='form'),
    path('<int:todo_id>/delete/', views.delete, name='delete')
]
