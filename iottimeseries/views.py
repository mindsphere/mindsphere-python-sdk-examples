from rest_framework.views import APIView
import sdk_util
from django.http import HttpResponse
from mindsphere_core import exceptions, serialization_filter, log_config
from rest_framework import status
from timeseries import RetrieveTimeseriesRequest, UpdatedTimeSeries, TimeSeriesItem, TimeSeriesDataItem, \
    CreateOrUpdateTimeseriesRequest, CreateOrUpdateTimeseriesDataRequest, DeleteUpdatedTimeseriesRequest
import json

logger = log_config.default_logging()


class TimeSeriesOperationsClientViewGetTimeSeries(APIView):
    def get(self, request, **kwargs):
        """
        get time series

         route timeSeries/get/<str:entityid>/<str:propertyname>/<str:from>/<str:to>
         param entityId - unique identifier of the asset (entity)
         param propertyname - Name of the aspect (property set).
         param from - Beginning of the time range to be retrieved (exclusive).
         param to - End of the time range to be retrieved (inclusive).
         return Timeseries data on successful execution.

         description This method internally calls method retrieve_timeseries of
                       TimeSeriesOperationsClient class. This class is available as dependency
                       in timeseries-<version-here>-py3-none-any.whl.
                       entityId, propertySetName, from and to are passed in request object as given by user(path variables)
                       and hence incorrect/non-existent values for entiyId and/or propertyname  will result in MindsphereError.

         apiEndpoint : GET /api/iottimeseries/v3/timeseries/{entityId}/{propertySetName} of timeseries service.
                      service. service.
         apiNote Retrieve time series data for one combination of an asset (entity) and an(a) aspect (property set).
         throws MindsphereError if an error occurs while attempting to invoke the
                                      sdk call.

        """
        logger.info('timeSeries/get/<str:entityid>/<str:propertyname>/<str:from>/<str:to> invoked')
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entityid", "")
                property_name = kwargs.get("propertyname", "")
                _from = kwargs.get("from", "")
                to = kwargs.get("to", "")
                logger.info(
                    "Request params are- enitityID:" + entity_id + " propertyName: " + property_name + " from:" + _from + " to:" + to)
                request_object = RetrieveTimeseriesRequest()
                request_object.entity_id = entity_id
                request_object.property_set_name = property_name
                request_object._from = _from
                request_object.to = to
                timseriesList = client.retrieve_timeseries(request_object)
                timeseries_json = serialization_filter.sanitize_for_serialization(timseriesList)
                timeseries_json = json.dumps(timeseries_json)
                logger.info("Getting response successfully for gettimeSeries" + timeseries_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for gettimeSries" + err)
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
        logger.info('timeSeries/put invoked')
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
                logger.info("timeseries updated Successfully " + timeseries_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for puttimeSeries " + err)
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

         route timeSeries/create/<str:entityid>/<str:propertyname>
         param entityId - unique identifier of the asset (entity)
         param propertyname - Name of the aspect (property set).

         return "successfully uploaded timeseriesdata" on successful execution.

         description This method internally calls method create_or_update_timeseries_data of
                     TimeSeriesOperationsClient class. This class is available as dependency
                     in timeseries-<version-here>-py3-none-any.whl. Creation of timeseries requires `timeseries`
                     data structure to be passed in request body.
         apiEndpoint : PUT /api/iottimeseries/v3/timeseries of timeseries service.
                         service.
         apiNote Create or update time series data for mutiple unique asset-aspect (entity-property set) combinations.
         throws MindsphereError if an error occurs while attempting to invoke the
                sdk call.

        """
        logger.info("timeSeries/create/<str:entityid>/<str:propertyname> invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entityid", "")
                property_name = kwargs.get("propertyname", "")
                logger.info("Request params are- entityID: " + entity_id + "propertyname" + property_name)
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
                logger.info("timeseries uploaded Successfully ")
            except exceptions.MindsphereError as err:
                logger.info("Getting error while creating timeseries "+err)
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
        delete time series

         route timeSeries/delete/<str:entityid>/<str:propertyname>/<str:from>/<str:to>
         param entityId - unique identifier of the asset (entity), (required)
         param propertyname - Name of the aspect (property set), (required)
         param from - beginning of the timerange to delete (exclusive), (required)
         param to - end of the timerange to delete (inclusive),   (required)

         return "successfully deleted timeseriesdata" on successful execution.

         description This method internally calls method delete_timeseries of
                       TimeSeriesOperationsClient class. This class is available as dependency
                       in timeseries-<version-here>-py3-none-any.whl.
                       entityId, propertyname, from and to  are passed as given by user and
                       hence incorrect/non-existent values of entityId and/or propertyname  will result in MindsphereError.
         apiEndpoint : DELETE /api/iottimeseries/v3/timeseries/{entityId}/{propertySetName} of timeseries service.

         apiNote Delete time series data for one combination of an asset (entity) and an(a) aspect (property set).
                    All property values within the given time range are deleted.
         throws MindsphereError if an error occurs while attempting to invoke the
                sdk call.

        """
        logger.info("timeSeries/delete/<str:entityid>/<str:propertyname>/<str:from>/<str:to> invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entityid", "")
                property_name = kwargs.get("propertyname", "")
                _from = kwargs.get("from", "")
                to = kwargs.get("to", "")
                logger.info(
                    "Request params are- enitityID:" + entity_id + " propertyName: " + property_name + " from:" + _from + " to:" + to)
                request_object = DeleteUpdatedTimeseriesRequest()
                request_object.entity_id = entity_id
                request_object.property_set_name = property_name
                request_object._from = _from
                request_object.to = to
                client.delete_timeseries(request_object)
                logger.info("successfully deleted timeseriesdata")
            except exceptions.MindsphereError as err:
                logger.info("Getting error while deleting timeseries " + err)
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
