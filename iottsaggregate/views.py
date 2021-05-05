from iottsaggregates import RetrieveAggregatesRequest
from rest_framework.views import APIView
import sdk_util

from django.http import HttpResponse
from mindsphere_core import exceptions, serialization_filter, log_config
from rest_framework import status
import json

logger = log_config.default_logging()


class AggregatesClientViewGetAggregates(APIView):

    def get(self, request, **kwargs):
        """
                get time series
                route : timeseriesaggregate/get/<str:entityid>/<str:propertyname>
                requestparam : entityId - An Asset Id for which aggregates are to be retrieved.
                requestparam :  propertySetName - property setname for which aggregates will be be retrieved.
                note :  Non existent/Incorrect entityId and propertySetName will result in MindsphereError.
                param --->  request - HttpRequest object
                returns : Time series aggregates in String format.
                returnType : String
                description : This method - get internally calls method retrieve_aggregates of AggregatesClient class.
                            This class is available as dependency in tsaggregates-<version-here>-py3-none-any.whl.
                            For retrieve_aggregates, two parameters are passed - entityId - An Asset Id for which aggregates
                            are to be retrieved and property setname for which aggregates will be be retrieved.
                            With an absence of any other parameters aggregates will be returned by following rule :
                            The parameters from, to, intervalUnit, intervalValue, and count are used to determine the time
                            range and interval length to return aggregates for. Intelligent auto-completion is applied to allow
                            clients to only provide a subset of the parameters, according to the following rules:
                            In case none of the parameters is provided, intervalUnit is set to DAY, intervalValue is set to 1,
                            to is set to the current time, and from is set to the current time minus 7 days.
                apiEndpoint : GET /api/iottsaggregates/v4/aggregates of aggregate service.
                           service.
                apiNote : Returns a list of aggregates for a given asset and aspect. The time range of the aggregates can be defined by a
                        combination of parameters; such as from, to, intervalUnit, intervalValue and count. Time range can be specified anywhere
                        in past or future for which timeseries data is present. In the case no time series data was available for an aggregation
                        interval, no aggregate will be returned. Pre-computed aggregates are aligned with the tenant's time zone.
                throws MindsphereError : if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("timeseriesaggregate/get/<str:entityid>/<str:propertyname> invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entityid", "")
                property_name = kwargs.get("propertyname", "")
                logger.info("Request params are- enitityID:" + entity_id + " propertyName: " + property_name)
                request_object = RetrieveAggregatesRequest()
                request_object.asset_id = entity_id
                request_object.aspect_name = property_name
                aggregateList = client.retrieve_aggregates(request_object)
                aggregate_json = serialization_filter.sanitize_for_serialization(aggregateList)
                aggregate_json = json.dumps(aggregate_json)
                logger.info("Getting response successfully for timeseriesaggregate" + aggregate_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for timeseriesaggregate" + err)
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
                route : timeseriesaggregate/get/<str:entityid>/<str:propertyname>/<str:from>/<str:to>
                param --> entityId - An Asset Id for which aggregates are to be retrieved.
                param -->  propertySetName - property set name for which aggregates will be be retrieved.
                note :  Non existent/Incorrect entityId and propertySetName will result in MindsphereError.
                param  --->  from :  Point in time from which aggregates are to be retrieved.
                param  --->  to : 	Point in time to which aggregates are to be retrieved.
                param  --->  request : HttpRequest object.
                returns : Time series aggregates in String format.

                description :   This method - get internally calls method retrieve_aggregates of AggregatesClient class.
                                This class is available as dependency in tsaggregates-<version-here>-py3-none-any.whl.
                                The parameters from, to, intervalUnit, intervalValue, and count are used to determine
                                the time range and interval length to return aggregates for.
                                If intervalUnit and intervalValue are not provided, the largest available interval length
                                fitting into the used time range is chosen.
                                If count is not provided, but the other parameters are, count will be derived based on the
                                time range divided by the intervalUnit and intervalValue.
                                In case parameters from or to are provided but do not coincide with the pre-calculated interval
                                boundaries of the used interval, from and to are shifted such that the overall time range
                                contains the provided one and time range boundaries coincide with interval boundaries.
                                If from, to and count are provided, intervalUnit, intervalValue is determined based on the time
                                range divided by count.
                apiEndpoint : GET /api/iottsaggregates/v4/aggregates of aggregate service.
                           service.
                apiNote : Returns a list of aggregates for a given asset and aspect. The time range of the aggregates can be defined by a
                        combination of parameters; such as from, to, intervalUnit, intervalValue and count. Time range can be specified anywhere
                        in past or future for which timeseries data is present. In the case no time series data was available for an aggregation
                        interval, no aggregate will be returned. Pre-computed aggregates are aligned with the tenant's time zone.
                throws MindsphereError : if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("timeseriesaggregate/get/<str:entityid>/<str:propertyname>/<str:from>/<str:to>")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entityid", "")
                property_name = kwargs.get("propertyname", "")
                _from = kwargs.get("from", "")
                to = kwargs.get("to", "")
                logger.info(
                    "Request params are- enitityID:" + entity_id + " propertyName: " + property_name + " from:" + _from + " to:" + to)
                request_object = RetrieveAggregatesRequest()
                request_object.asset_id = entity_id
                request_object.aspect_name = property_name
                request_object._from = _from
                request_object.to = to
                aggregateList = client.retrieve_aggregates(request_object)
                aggregate_json = serialization_filter.sanitize_for_serialization(aggregateList)
                aggregate_json = json.dumps(aggregate_json)
                logger.info("Getting response successfully for timeseriesaggregate" + aggregate_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for timeseriesaggregate" + err)
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
