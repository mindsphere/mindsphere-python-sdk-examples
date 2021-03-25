from iottsaggregates import RetrieveAggregatesRequest
from rest_framework.views import APIView
import sdk_util
from django.http import HttpResponse
from mindsphere_core import exceptions,serialization_filter
from rest_framework import status
import json


class AggregatesClientViewGetAggregates(APIView):
    def get(self, request, **kwargs):
        """
        get time series
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entityid", "")
                property_name = kwargs.get("propertyname", "")
                request_object = RetrieveAggregatesRequest()
                request_object.asset_id = entity_id
                request_object.aspect_name = property_name
                aggregateList = client.retrieve_aggregates(request_object)
                aggregate_json = serialization_filter.sanitize_for_serialization(aggregateList)
                aggregate_json = json.dumps(aggregate_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                aggregate_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class AggregatesClientViewGetAggregatesFromTo(APIView):
    def get(self, request, **kwargs):
        """
        get time series
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entityid", "")
                property_name = kwargs.get("propertyname", "")
                _from = kwargs.get("from","")
                to = kwargs.get("to","")
                request_object = RetrieveAggregatesRequest()
                request_object.asset_id = entity_id
                request_object.aspect_name = property_name
                request_object._from = _from
                request_object.to = to
                aggregateList = client.retrieve_aggregates(request_object)
                aggregate_json = serialization_filter.sanitize_for_serialization(aggregateList)
                aggregate_json = json.dumps(aggregate_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                aggregate_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


from django.shortcuts import render

# Create your views here.
