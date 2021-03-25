from rest_framework.views import APIView
import sdk_util
from django.http import HttpResponse
from mindsphere_core import exceptions
from rest_framework import status
from . import data_generator
import json

class EventOperationsClientViewTopEvent(APIView):
    def get(self, request):
        """
        Top events
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.top_events(data_generator.get_top_events_data())
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response), content_type="application/json", status=status.HTTP_200_OK
            )


class EventOperationsClientViewFilterEvent(APIView):
    def get(self, request):
        """
        filter events
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.filter_events(data_generator.get_filter_events_data())
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )


class EventOperationsClientViewCountEvent(APIView):
    def get(self, request):
        """
        count events
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.count_events(data_generator.get_count_events_data())
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )


class EventOperationsClientViewRemoveDuplicateEvent(APIView):
    def get(self, request):
        """
        remove duplicates events
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.remove_duplicate_events(data_generator.remove_duplicates_data())
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )


class PatternOperationsClientViewMatchPatternsOverEvents(APIView):
    def get(self, request):
        """
        pattern matching events
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.match_patterns_over_events(data_generator.get_pattern_matching_data())
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )

