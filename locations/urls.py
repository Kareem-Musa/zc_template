from django.urls import path
from . import views

app_name = 'locations'
urlpatterns = [
    path('states', views.state_list, name='states'),
    path('add_state', views.add_state, name='add_state'),
    # localities
    path('locality_list', views.locality_list, name='locality_list'),
    path('add_locality', views.add_locality, name='add_locality'),
    # Unities
    path('unity_list', views.unity_list, name='unity_list'),
    path('add_unity', views.add_unity, name='add_unity'),
]
