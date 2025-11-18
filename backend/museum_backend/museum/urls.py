from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.PersonListView.as_view(), name='people-list'),
    path('people/<int:id>/', views.PersonDetailView.as_view(), name='person-detail'),
    path('groups/', views.GroupListView.as_view(), name='groups-list'),
]