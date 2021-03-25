from rest_framework.views import APIView
import sdk_util
from django.http import HttpResponse
from mindsphere_core import exceptions,serialization_filter
from rest_framework import status
from timeseries import RetrieveTimeseriesRequest, UpdatedTimeSeries, TimeSeriesItem, TimeSeriesDataItem, \
    CreateOrUpdateTimeseriesRequest, CreateOrUpdateTimeseriesDataRequest ,DeleteUpdatedTimeseriesRequest
import json


class TimeSeriesOperationsClientViewGetTimeSeries(APIView):
    def get(self, request, **kwargs):
        """
        get time series
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entityid", "")
                property_name = kwargs.get("propertyname", "")
                _from = kwargs.get("from", "")
                to = kwargs.get("to", "")
                request_object = RetrieveTimeseriesRequest()
                request_object.entity_id = entity_id
                request_object.property_set_name = property_name
                request_object._from = _from
                request_object.to = to
                timseriesList = client.retrieve_timeseries(request_object)
                timeseries_json = serialization_filter.sanitize_for_serialization(timseriesList)
                timeseries_json = json.dumps(timeseries_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                timeseries_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class TimeSeriesOperationsClientViewPutTimeSeries(APIView):
    def get(self, request, **kwargs):
        """
        put time series
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                timeseries = UpdatedTimeSeries()
                timeSeriesItem = TimeSeriesItem()
                timeSeriesItem.entity_id = "535140e4980e413497d112015ddd47ff"
                timeSeriesItem.property_set_name = "testaspect2812"

                timeSeriesDataItem = TimeSeriesDataItem()
                timeSeriesDataItem.fields = {
                    "test": 15
                }
                timeSeriesDataItem.time = "2020-11-11T02:52:00Z"
                timeSeriesDataItems = [timeSeriesDataItem]
                timeSeriesItem.data = timeSeriesDataItems
                timeSeriesItems = [timeSeriesItem]
                timeseries.timeseries = tim = timeSeriesItems
                createOrUpdateTimeseriesRequest = CreateOrUpdateTimeseriesRequest()
                createOrUpdateTimeseriesRequest.timeseries = timeseries
                response = client.create_or_update_timeseries(createOrUpdateTimeseriesRequest)
                timeseries_json = serialization_filter.sanitize_for_serialization(response)
                timeseries_json = json.dumps(timeseries_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                timeseries_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class TimeSeriesOperationsClientViewCreateTimeSeries(APIView):
    def get(self, request, **kwargs):
        """
        put time series
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entityid", "")
                property_name = kwargs.get("propertyname", "")
                requestObject = CreateOrUpdateTimeseriesDataRequest();
                requestObject.entity_id = entity_id
                requestObject.property_set_name = property_name
                timeSeriesDataItem = TimeSeriesDataItem()
                timeSeriesDataItem.fields = {
                    "test": 15
                }
                timeSeriesDataItem.time = "2020-11-11T02:52:00Z"
                timeSeriesDataItems = [timeSeriesDataItem]
                requestObject.timeseries = timeSeriesDataItems
                client.create_or_update_timeseries_data(requestObject)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                "successfully uploaded timeseriesdata",
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class TimeSeriesOperationsClientViewDeleteTimeSeries(APIView):
    def get(self, request, **kwargs):
        """
        get time series
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entityid", "")
                property_name = kwargs.get("propertyname", "")
                _from = kwargs.get("from", "")
                to = kwargs.get("to", "")
                request_object = DeleteUpdatedTimeseriesRequest()
                request_object.entity_id = entity_id
                request_object.property_set_name = property_name
                request_object._from = _from
                request_object.to = to
                client.delete_timeseries(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                "successfully deleted timeseriesdata",
                content_type="application/json",
                status=status.HTTP_200_OK
            )



from django.shortcuts import render

# Create your views here.
