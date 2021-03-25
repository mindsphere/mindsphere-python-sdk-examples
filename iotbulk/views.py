from rest_framework.views import APIView
import sdk_util
from django.http import HttpResponse
from mindsphere_core import exceptions
from rest_framework import status
from iottsbulk import RetrieveTimeseriesRequest, CreateImportJobRequest, BulkImportInput, FileInfo,Data
from iottsbulk import RetrieveImportJobRequest
import json
from app.settings import logger


class BulkImportOperationsClientViewImportjobget(APIView):
    def get(self, request,**kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                id = kwargs.get("id", "")
                request = RetrieveImportJobRequest()
                request.id = id
                response = client.retrieve_import_job(request)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response), content_type="application/json", status=status.HTTP_200_OK
            )


class ReadOperationsClientViewImportjob(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entityid", "")
                property_name = kwargs.get("propertyname", "")
                _from = kwargs.get("from", "")
                to = kwargs.get("to", "")
                retrieveTimeseriesRequest = RetrieveTimeseriesRequest()
                retrieveTimeseriesRequest.entity = entity_id
                retrieveTimeseriesRequest.property_set_name = property_name
                retrieveTimeseriesRequest._from = _from
                retrieveTimeseriesRequest.to = to
                response = client.retrieve_timeseries(retrieveTimeseriesRequest)
                logger.info("Response")
                logger.info(response)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )


class BulkImportOperationsClientViewImportjobpost(APIView):
    def get(self, request):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                createImportJobRequest = CreateImportJobRequest()
                bulkImportInput = BulkImportInput()
                data = Data()
                data.entity = "5908ae5c5e4f4e18b0be58cd21ee675f"
                data.property_set_name = "test_2020_11_11"

                fileInfo = FileInfo()
                fileInfo.file_path = "test11.json"
                fileInfo._from = "2020-12-16T04:30:00.01Z"
                fileInfo.to = "2020-12-16T04:35:00.30Z"
                fileInfoList = [fileInfo]

                data.timeseries_files = fileInfoList
                dataList = [data]

                bulkImportInput.data = dataList
                createImportJobRequest.bulk_import_input = bulkImportInput
                response = client.create_import_job(createImportJobRequest)
                logger.info("Response")
                logger.info(response)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )
