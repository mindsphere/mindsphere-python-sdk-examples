from rest_framework.views import APIView
import sdk_util
from django.http import HttpResponse
from mindsphere_core import exceptions, log_config
from rest_framework import status
from . import data_generator
import json

logger = log_config.default_logging()


class EventOperationsClientViewTopEvent(APIView):
    def get(self, request):
        """
        Top events

         route eventAnalytics/topevents
         return The most frequent events, which are sorted by the number of appearances in a dataset in a descending order.
         description This method internally calls method top_events of EventOperationsClient class.
                        This class is available as dependency in eventanalytics-<version-here>-py3-none-any.whl

         apiEndpoint : POST /api/eventanalytics/v3/findTopEvents of eventanalytics
                       service.
         apiNote Finds the most frequent events, which are sorted by the number of appearances in a dataset in a descending order.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("eventAnalytics/topevents invoked.")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.top_events(data_generator.get_top_events_data())
                logger.info("Getting response successfully for topevents "+ json.dumps(response))
            except exceptions.MindsphereError as err:
                logger.error("Getting error for topevents "+err)
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
      
         route eventAnalytics/filterEvents
         
         return List of events after filtering.
         
         description This method - filterEvents internally calls method filterEvents of EventOperationsClient class.
                        This class is available as dependency in eventanalytics-<version-here>-py3-none-any.whl. 
                        The request object is formed and passed dynamically.
                        This method takes data as part of request body.
                        `data` is a Data structure with two parts eventsMetadata, events.

                        eventsMetadata Metadata ->  for the events list specifying the property name of the item in the
                        events list that contains the text of the event (eventTextPropertyName) and time window length in
                        miliseconds of the period in which time interval will be split (splitInterval).

                        events List -->  with the events that will be processed.
                       
         apiEndpoint : POST /api/eventanalytics/v3/filterEvents of eventanalytics
                       service.
         apiNote  Simplifies the dataset to the most meaningful data. Filtering the dataset based on the text of the event.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("eventAnalytics/filterEvents invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.filter_events(data_generator.get_filter_events_data())
                logger.info("Getting response successfully for filterEvents " + json.dumps(response.to_dict))
            except exceptions.MindsphereError as err:
                logger.error("Getting error for filterEvents " + err)
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict), content_type="application/json", status=status.HTTP_200_OK
            )


class EventOperationsClientViewCountEvent(APIView):
    def get(self, request):
        """
        count events
        route eventAnalytics/countEvents
        return Output the given time interval (startTime, endTime) and the resulted number of event occurrences.

         description This method internally calls method countEvents of EventOperationsClient class.
                     This class is available as dependency in eventanalytics-<version-here>-py3-none-any.whl.
                     The request object is formed and passed dynamically. (see data_generator.get_count_events_data())
                     This method takes data as part of request body.
                     `data` is a Data structure with two parts eventsMetadata, events.
                     eventsMetadata Metadata ->  for the events list specifying the property name of the item in the events list
                     that contains the text of the event (eventTextPropertyName) and time window length in miliseconds of the
                     period in which time interval will be split (splitInterval).
                     events List -->  with the events that will be processed.

         apiEndpoint : POST /api/eventanalytics/v3/countEvents of eventanalytics
                       service.
         apiNote Determines the number of events for a required time resolution.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("eventAnalytics/countEvents invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.count_events(data_generator.get_count_events_data())
                logger.info("Getting response successfully for countEvents " + json.dumps(response.to_dict))
            except exceptions.MindsphereError as err:
                logger.error("Getting error for countEvents " + err)
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict), content_type="application/json", status=status.HTTP_200_OK
            )


class EventOperationsClientViewRemoveDuplicateEvent(APIView):
    def get(self, request):
        """
            remove duplicates events

            route eventAnalytics/removeDuplicateEvents
            return List of events after removal of duplicate events.
            description This method internally calls method remove_duplicate_events of EventOperationsClient class.
                        This class is available as dependency in eventanalytics-<version-here>-py3-none-any.whl.
                        The request object is formed and passed dynamically.(See data_generator.remove_duplicates_data())
                        This method takes data as part of request body.
                        `data` is a Data structure with two parts eventsMetadata, events.
                        eventsMetadata Metadata ->  for the events list specifying the property name of the item in the events
                        list that contains the text of the event (eventTextPropertyName) and time window length in miliseconds
                        of the period in which time interval will be split (splitInterval).
                        events List -->  with the events that will be processed.

            apiEndpoint : POST /api/eventanalytics/v3/removeDuplicateEvents of eventanalytics
                          service.
            apiNote Removes the duplicate events. Determine pre-existing relationships between events for a requested temporal
                  resolution (example 500ms) and reduce the data set by aggregating events with duplicate value.
            throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("eventAnalytics/removeDuplicateEvents invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.remove_duplicate_events(data_generator.remove_duplicates_data())
                logger.info("Getting response successfully for removeDuplicateEvents " + json.dumps(response.to_dict))
            except exceptions.MindsphereError as err:
                logger.error("Getting error for removeDuplicateEvents " + err)
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict), content_type="application/json", status=status.HTTP_200_OK
            )


class PatternOperationsClientViewMatchPatternsOverEvents(APIView):
    def get(self, request):
        """
        pattern matching events

         route eventAnalytics/matchEventPattern

         return List of events matching pattern.

         description This method internally calls method match_patterns_over_events of PatternOperationsClient
                        class.
                        This class is available as dependency in eventanalytics-<version-here>-py3-none-any.whl.
                        The request object is formed and passed dynamically.(See data_generator.get_pattern_matching_data())
                        This method takes data as part of request body.
                        Data structure with four parts - maxPatternInterval, patternsList, nonEvents and eventsInput.

                        maxPatternInterval ---> The maximum time length (in milliseconds) of the sliding window where the
                        pattern occurs (Maximum difference allowed between the first event of the pattern and the last one).

                        patternsList ---> The patterns to be found in events. The eventText can contain regular expressions.
                        The acceptable syntax for the regular expressions is the java syntax. minRepetitions and maxRepetitions
                        represent the minimum and maximum number of events of the specified type that are allowed to occur in
                        order for the pattern to be matched on the events.

                        nonEvents ---> A list of events that is not allowed to be part of a pattern. Any pattern which contains
                         a non-event is excluded from the final report.

                        eventsInput ---> Metadata for the events list specifying the property name of the item in the events list
                        that contains the text of the event and the list with the events that will be processed.

         apiEndpoint : POST /api/eventanalytics/v3/matchEventPatterns of eventanalytics
                       service.
         apiNote :   Applies the patterns specified in body on a list of events. Finds all instances of the specified pattern(s)
                   in a collection of events.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("eventAnalytics/matchEventPattern invoked.")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.match_patterns_over_events(data_generator.get_pattern_matching_data())
                logger.info("Getting response successfully for matchEventPattern " + json.dumps(response.to_dict))
            except exceptions.MindsphereError as err:
                logger.error("Getting error for matchEventPattern " + err)
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict), content_type="application/json", status=status.HTTP_200_OK
            )
