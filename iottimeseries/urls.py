from django.urls import path
from iottimeseries import views

urlpatterns = [
    path("timeseries/puttimeseriesdata/<str:entityid>/<str:propertyname>", views.TimeSeriesOperationsClientViewCreateTimeSeriescall.as_view()),
    path("timeseries/puttimeseries", views.TimeSeriesOperationsClientViewPutTimeSeriescall.as_view()),
    path("timeseries/gettimeseries/<str:entityid>/<str:propertyname>", views.TimeSeriesOperationsClientViewGetTimeSeries.as_view()),
    path("timeSeries/put", views.TimeSeriesOperationsClientViewPutTimeSeries.as_view()),
    path("timeSeries/create/<str:entityid>/<str:propertyname>", views.TimeSeriesOperationsClientViewCreateTimeSeries.as_view()),
    path("timeSeries/delete/<str:entityid>/<str:propertyname>/<str:from>/<str:to>", views.TimeSeriesOperationsClientViewDeleteTimeSeries.as_view()),
]
