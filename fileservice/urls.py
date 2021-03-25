from django.urls import path
from fileservice import views

urlpatterns = [
    path("files/fileservicecreate/<str:entity_id>", views.FileServiceClientViewCreateFile.as_view()),
    path("files/fileserviceupdate/<str:entity_id>/<str:path>", views.FileServiceClientViewUpdateFile.as_view()),
    path("files/fileservicesearch/<str:entity_id>", views.FileServiceClientViewSearchFile.as_view()),
    path("files/fileservicecreatemultipartfile/<str:entity_id>/<str:path>", views.FileServiceClientViewMultiPart.as_view()),
    path("files/fileservicelistmultipartfile/<str:entity_id>/<str:path>", views.FileServiceClientViewListMultiPart.as_view()),
    path("files/fileservicegetfile/<str:entity_id>/<str:path>", views.FileServiceClientViewGetFile.as_view()),
    path("files/fileservicedelete/<str:entity_id>/<str:path>", views.FileServiceClientViewDeleteFile.as_view()),
]
