from django.urls import path
from iottimeseries import views

urlpatterns = [
    path("timeSeries/get/<str:entityid>/<str:propertyname>/<str:from>/<str:to>", views.TimeSeriesOperationsClientViewGetTimeSeries.as_view()),
    path("timeSeries/put", views.TimeSeriesOperationsClientViewPutTimeSeries.as_view()),
    path("timeSeries/create/<str:entityid>/<str:propertyname>", views.TimeSeriesOperationsClientViewCreateTimeSeries.as_view()),
    path("timeSeries/delete/<str:entityid>/<str:propertyname>/<str:from>/<str:to>", views.TimeSeriesOperationsClientViewDeleteTimeSeries.as_view()),
]
