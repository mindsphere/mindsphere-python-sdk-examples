from django.urls import path, include
from iottsaggregate import views
from django.conf.urls import url

urlpatterns = [
    path("timeseriesaggregate/get/<str:entityid>/<str:propertyname>", views.AggregatesClientViewGetAggregates.as_view()),
    path("timeseriesaggregate/get/<str:entityid>/<str:propertyname>/<str:from>/<str:to>", views.AggregatesClientViewGetAggregatesFromTo.as_view()),
]
