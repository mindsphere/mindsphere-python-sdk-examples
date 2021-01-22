from django.urls import path, include
from assets import views
from django.conf.urls import url

urlpatterns = [
    path("aspects/<str:tenant>/", views.AspecttypeClientViewCreate.as_view()),
    path("assettype/<str:tenant>", views.AssettypeClientViewCreate.as_view()),
    path("assets/<str:typeid>/", views.AssetsClientViewPost.as_view()),
    path("assetfiles/", views.FilesClientViewPost.as_view()),
    path("assetfiles/<str:id>", views.AssetsClientViewUpdateFile.as_view()),
    path("assetlocation/<str:id>/<str:ifmatch>", views.LocationsClientViewUpdate.as_view()),
    path("assetsget/<str:id>", views.AssetsClientViewGetById.as_view()),
    path("assetsdelete/<str:id>", views.AssetsClientViewDelete.as_view()),
    path("assets/", views.AssetsClientViewGetAll.as_view()),
]
