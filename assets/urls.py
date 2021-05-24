from django.urls import path, include
from assets import views
from django.conf.urls import url

urlpatterns = [
    path("assets/putassettype/<str:id>/<str:ifmatch>", views.AssettypeClientViewput.as_view()),
    path("assets/putaspect/<str:id>/<str:ifmatch>", views.AspecttypeClientViewput.as_view()),
    path("assets/postasset", views.AssetsClientViewPostAsset.as_view()),
    path("assets/aspects", views.AspecttypeClientViewCreate.as_view()),
    path("filteraspecttypename", views.AspecttypeClientViewEqualTo.as_view()),
    path("filteraspecttypelike", views.AspecttypeClientViewLike.as_view()),
    path("assets/assettype/<str:tenant>", views.AssettypeClientViewCreate.as_view()),
    path("assets/assets/<str:typeid>", views.AssetsClientViewPost.as_view()),
    path("filterassetsstartwith", views.AssetsClientViewStartWith.as_view()),
    path("filterassetsoftype", views.AssetsClientViewOfAspectType.as_view()),
    path("filterassettypeendwith", views.AssettypeClientViewEndsWith.as_view()),
    path("filterassettypecontains", views.AssettypeClientViewContains.as_view()),
    path("assets/assetfiles", views.FilesClientViewPost.as_view()),
    path("assets/assetfiles/<str:id>", views.AssetsClientViewUpdateFile.as_view()),
    path("assets/assetlocation/<str:id>/<str:ifmatch>", views.LocationsClientViewUpdate.as_view()),
    path("assets/assetsget/<str:id>", views.AssetsClientViewGetById.as_view()),
    path("assets/assetsdelete/<str:id>/<str:ifmatch>", views.AssetsClientViewDelete.as_view()),
    path("assetsdeletewithconfirmation/<str:id>/<str:ifmatch>", views.AssetsClientViewDeleteWithConfirmation.as_view()),
    path("assets/assets", views.AssetsClientViewGetAll.as_view()),
    path("<str:id>/aspects", views.StructureClientViewAspectsOfAsset.as_view()),
    path("assets/root", views.AssetsClientViewGetroot.as_view())
]
