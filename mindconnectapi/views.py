import sdk_util
from rest_framework.views import APIView
import sdk_util
from django.http import HttpResponse
from mindsphere_core import exceptions, serialization_filter
from rest_framework import status
import json
from mindconnect.models import *


class DiagnosticActivationsClientViewdiagnostic_activations_get(APIView):
    def get(self, request):
        """
        get Diagnostic Activation
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                requestObject = DiagnosticActivationsGetRequest()
                response = client.diagnostic_activations_get(requestObject)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                respose_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class DiagnosticActivationsClientViewdiagnosticactivationscreate(APIView):
    def get(self, request, **kwargs):
        """
        create Diagnostic Activation
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                agent_id = kwargs.get("agentid", "")
                status = kwargs.get("status", "")
                diagnosticActivation = DiagnosticActivation(
                    agent_id=agent_id,
                    status=status
                )
                request_object = DiagnosticActivationsPostRequest(
                    diagnostic_activation=diagnosticActivation
                )

                response = client.diagnostic_activations_post(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                respose_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class DiagnosticActivationsClientViewImportjobdelete(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                did = kwargs.get("id", "")
                request_object = DiagnosticActivationsIdDeleteRequest(
                    id=did
                )
                client.diagnostic_activations_id_delete(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                "successfully uploaded timeseries",
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class DiagnosticActivationsClientViewdiagnosticactivationsgetbyID(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                did = kwargs.get("id", "")
                request_object = DiagnosticActivationsIdGetRequest(
                    id=did
                )
                response = client.diagnostic_activations_id_get(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                respose_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class DiagnosticActivationsClientViewdiagnosticactivationsgetbyIDMessage(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                did = kwargs.get("id", "")
                request_object = DiagnosticActivationsIdMessagesGetRequest(
                    id=did
                )
                response = client.diagnostic_activations_id_messages_get(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                respose_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class DiagnosticActivationsClientViewdiagnosticactivationsputbyid(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                id = kwargs.get("id", "")
                status = kwargs.get("status", "")
                diagnosticActivationStatus = DiagnosticActivationStatus(
                    status=status
                )
                request_object = DiagnosticActivationsIdPutRequest(
                    id=id,
                    diagnostic_activation_status=diagnosticActivationStatus
                )
                response = client.diagnostic_activations_id_put(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                respose_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class DiagnosticInformationClientViewdiagnosticinfoget(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                requestObject = DiagnosticInformationGetRequest()
                response = client.diagnostic_information_get(requestObject)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                respose_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class MappingsClientViewdatapointMappingGet(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                request_object = DataPointMappingsGetRequest()
                response = client.data_point_mappings_get(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                respose_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class MappingsClientViewdatapointMappingGetbyId(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                id = kwargs.get("id", "")
                request_object = DataPointMappingsIdGetRequest(
                    id=id
                )
                response = client.data_point_mappings_id_get(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                respose_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class MappingsClientViewdatapointMappingCreate(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                mapping = Mapping(
                    agent_id="ad22f8a7ebb24b8fb41767afd2c63f08",
                    data_point_id="SDKDP13",
                    entity_id="078b1908bc9347678168760934465587",
                    property_set_name="TyreTemperature",
                    property_name="FLWheel",
                    keep_mapping=False
                )
                request_object = DataPointMappingsPostRequest(
                    mapping=mapping
                )
                response = client.data_point_mappings_post(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                respose_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class MappingsClientViewdatapointMappingDelete(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                id = kwargs.get("id", "")
                request_object = DataPointMappingsIdDeleteRequest(
                    id=id
                )
                client.data_point_mappings_id_delete(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                "Deleted successfully",
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class RecordRecoveryClientViewidPost(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                id = kwargs.get("id", "")
                request_object = RecoverableRecordsIdReplayPostRequest(
                    id=id
                )
                client.recoverable_records_id_replay_post(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                "created successfully",
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class RecordRecoveryClientViewGet(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                request_object = RecoverableRecordsGetRequest()
                response = client.recoverable_records_get(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                respose_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class RecordRecoveryClientViewIdDownloadLinkGet(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                id = kwargs.get("id", "")
                request_object = RecoverableRecordsIdDownloadLinkGetRequest(
                    id=id
                )
                response = client.recoverable_records_id_download_link_get(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                respose_json,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class RecordRecoveryClientViewIdDelete(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                id = kwargs.get("id", "")
                request_object = RecoverableRecordsIdDeleteRequest(
                    id=id
                )
                client.recoverable_records_id_delete(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                "Deleted Successfully",
                content_type="application/json",
                status=status.HTTP_200_OK
            )
