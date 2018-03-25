from django.urls import path
from . import views

app_name = 'resolution'

urlpatterns = [
    path('', views.index, name='index'),

    path('<note_id>/', views.detail, name="detail"),
]
