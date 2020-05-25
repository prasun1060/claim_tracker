from django.urls import path
from . import views

app_name = "dailytracker"
urlpatterns = [
    path('', views.tracker_view, name='tracker-home'),
    path('team/', views.team, name='team'),
    path('export/', views.export_claims_csv, name='export'),
]