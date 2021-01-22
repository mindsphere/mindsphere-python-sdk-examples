from django.urls import path
from fileservice import views

urlpatterns = [
    path("fileservicecreate/<str:entity_id>", views.FileServiceClientViewCreateFile.as_view()),
    path("fileservicesearch/<str:entity_id>", views.FileServiceClientViewSearchFile.as_view()),
    path("fileservicecreatemultipart/<str:entity_id>/<str:path>", views.FileServiceClientViewMultiPart.as_view()),
    path("fileservicelistmultipart/<str:entity_id>/<str:path>", views.FileServiceClientViewListMultiPart.as_view()),
    path("fileservicegetfile/<str:entity_id>/<str:path>", views.FileServiceClientViewGetFile.as_view()),
]
