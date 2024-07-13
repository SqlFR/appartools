from django.urls import path

from . import views

app_name = "check_arrangement"
urlpatterns = [
    path('', views.index, name='index'),

    # Aparts
    path('add_apartment/', views.index, name='add_apartment'),
    path('delete_apartment/<int:apartment_id>', views.delete_apartment, name='delete_apartment'),

    # Issues
    path('delete_issue/<int:apartmentissue_id>/', views.delete_issue, name='delete_issue'),
    path('add_issue/<int:apartment_id>/', views.add_issue, name="add_issue"),
    path('edit_issue/<int:apartmentissue_id>/', views.edit_issue, name='edit_issue'),

    # Sheets
    path('sheets/<int:apartment_id>/', views.sheets, name='sheets'),
    path('sheets/to_delivery/<int:apartment_id>/', views.to_delivery, name='to_delivery'),
    path('sheets/delivery/<int:sheet_id>/', views.delivery, name='delivery'),
    path('sheets/handled/<int:sheet_id>/', views.handled, name='handled'),
    path('sheets/unavailable/<int:sheet_id>/', views.unavailable, name='unavailable'),
    path('sheets/update_to_not_handled/<int:apartment_sheet_handled_id>/', views.update_to_not_handled, name='update_to_not_handled'),

    # Results
    path('<int:apartment_id>/results/', views.results, name="results"),
]
