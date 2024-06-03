from django.urls import path

from . import views

app_name = "check_arrangement"
urlpatterns = [
    path('', views.index, name='index'),
    path('add_apartment/', views.add_apartment, name='add_apartment'),
    path('delete_apartment/<int:apartment_id>', views.delete_apartment, name='delete_apartment'),
    path('delete_issue/<int:apartmentissues_id>/', views.delete_issue, name='delete_issue'),
    path('<int:apartment_id>/', views.detail, name="detail"),
    path('<int:apartment_id>/results/', views.results, name="results"),
]
