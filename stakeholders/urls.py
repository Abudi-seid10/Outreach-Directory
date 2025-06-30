from django.urls import path
from . import views

urlpatterns = [
    path('', views.stakeholder_list, name='stakeholder_list'),
    path('stakeholder/<int:pk>/', views.stakeholder_detail, name='stakeholder_detail'),
    path('stakeholder/new/', views.stakeholder_new, name='stakeholder_new'),
    path('stakeholder/<int:pk>/edit/', views.stakeholder_edit, name='stakeholder_edit'),
    path('stakeholder/<int:pk>/delete/', views.stakeholder_delete, name='stakeholder_delete'),
    path('export-csv/', views.export_stakeholders_csv, name='export_stakeholders_csv'),
    path('import-csv/', views.import_stakeholders_csv, name='import_stakeholders_csv'),
]