from django.urls import path
from . import views

app_name = 'resolution'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    #user registration
    path('register/', views.UserFormView.as_view(), name='register'),


    path('<pk>/', views.DetailView.as_view(), name="detail"),

    # add resolution -  /resolution/resolution/add/
    path('resolution/add/$', views.ResolutionCreate.as_view(), name='resolution-add'),

    # edit resolutions - /resolution/resolution/2/
    path('resolution/<pk>/$', views.ResolutionUpdate.as_view(), name='resolution-update'),

    # delete resolution - /resolution/resolution/2/delete
    path('resolution/<pk>/delete/$', views.ResolutionDelete.as_view(), name='resolution-delete'),
]
