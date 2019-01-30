from django.urls import path
from . import views

app_name = 'votes'
urlpatterns = [
    path('', views.index, name='index'),
    path('help/', views.help, name='help'),
    path('<int:candidate_id>/', views.candidate_detail, name='detail'),
    # path('<int:candidate_id>/update', views.candidate_update, name='update'),
    path('candidate_create/', views.candidate_create, name='create'),
    # path('position_create/', views.position_create, name='create'),
]
