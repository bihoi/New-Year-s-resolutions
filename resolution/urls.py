from django.urls import path
from . import views

app_name = 'resolution'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<pk>/', views.DetailView.as_view(), name="detail"),

    # add resolution
    path('resolution/add/$', views.ResolutionCreate.as_view(), name='resolution-add'),
]
