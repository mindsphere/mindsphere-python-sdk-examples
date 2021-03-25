from django.urls import path
from iotbulk import views

urlpatterns = [
    path("iotbulk/retrievetimeseries/<str:entityid>/<str:propertyname>/<str:from>/<str:to>", views.ReadOperationsClientViewImportjob.as_view()),
    path("iotbulk/importjobget/<str:id>", views.BulkImportOperationsClientViewImportjobget.as_view()),
    path("iotbulk/importjobpost", views.BulkImportOperationsClientViewImportjobpost.as_view()),
]
