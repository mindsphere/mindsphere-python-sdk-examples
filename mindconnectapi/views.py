import sdk_util
from rest_framework.views import APIView
import sdk_util
from django.http import HttpResponse
from mindsphere_core import exceptions, serialization_filter, log_config
from rest_framework import status
import json
from mindconnect.models import *

logger = log_config.default_logging()


class DiagnosticActivationsClientViewdiagnostic_activations_get(APIView):
    def get(self, request):
        """
        get Diagnostic Activations.

         route mindconnect/diagnosticActivationsGet

         return Diagnostic activations data in String format.

         description This method internally calls method diagnostic_activations_get of DiagnosticActivationsClient class.
                        This class is available as dependency in mindconnect-<version-here>-py3-none-any.whl.

         apiEndpoint : GET /api/mindconnect/v3/diagnosticActivations of mindconnect service.

         apiNote Gets diagnostic activations.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("mindconnect/diagnosticActivationsGet invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                requestObject = DiagnosticActivationsGetRequest()
                response = client.diagnostic_activations_get(requestObject)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
                logger.info("Getting response successfully for diagnosticActivationsGet" + respose_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for diagnosticActivationsGet" + err)
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
         create Diagnostic Activation.

         route mindconnect/diagnosticActivationsCreate/<str:agentid>/<str:status>
         param : agentid ---> Unique identifier of the agent.
         param : status --->  Status of the activation.
         return Created diagnostic activation data.

         description This method internally calls method diagnostic_activations_post of DiagnosticActivationsClient class.
                     This class is available as dependency in mindconnect-<version-here>-py3-none-any.whl.

         apiEndpoint : POST /api/mindconnect/v3/diagnosticActivations of mindconnect service.

         apiNote Creates a new diagnostic activation.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("mindconnect/diagnosticActivationsCreate/<str:agentid>/<str:status> invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                agent_id = kwargs.get("agentid", "")
                status = kwargs.get("status", "")
                logger.info("Request params are- agentid:" + agent_id + " status: " + status)

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
                logger.info("Getting response successfully for diagnosticActivationsCreate" + respose_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for diagnosticActivationsCreate" + err)
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
        """
         delete diagnostic activation.

         route mindconnect/diagnosticActivationsDelete/<str:id>
         param id - Unique identifier of diagnostic activation resource. (required)

         return successfully deleted activation on suceesful execution.
         description This method internally calls method diagnostic_activations_id_delete of DiagnosticActivationsClient class.
                     This class is available as dependency in mindconnect-<version-here>-py3-none-any.whl.

         apiEndpoint : DELETE /api/mindconnect/v3/diagnosticActivations/{id} of mindconnect service.
                       service.
         apiNote Delete a diagnostic activation.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("mindconnect/diagnosticActivationsDelete/<str:id> invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                did = kwargs.get("id", "")
                logger.info("Request param is - Id:"+did)
                request_object = DiagnosticActivationsIdDeleteRequest(
                    id=did
                )
                client.diagnostic_activations_id_delete(request_object)
                logger.info("successfully deleted activation")
            except exceptions.MindsphereError as err:
                logger.error("Getting error for diagnosticActivationsDelete" + err)
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                "successfully deleted activation",
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class DiagnosticActivationsClientViewdiagnosticactivationsgetbyID(APIView):
    def get(self, request, **kwargs):
        """
        get diagnostic activation by Id.

         route mindconnect/diagnosticActivationsGet/<str:id>
         param id - Unique identifier of diagnostic activation resource. (required)
         return Diagnostic activation data for given id.

         description This method - diagnosticActivationsIdGetTest internally calls method diagnosticActivationsIdGet of
                     DiagnosticActivationsClient class.
                     This class is available as dependency in mindconnect-<version-here>-py3-none-any.whl.

         apiEndpoint : GET /api/mindconnect/v3/diagnosticActivations/{id} of mindconnect service.

         apiNote Gets a diagnostic activation.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("mindconnect/diagnosticActivationsGet/<str:id> invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                did = kwargs.get("id", "")
                logger.info("Request param is - Id:" + did)
                request_object = DiagnosticActivationsIdGetRequest(
                    id=did
                )
                response = client.diagnostic_activations_id_get(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
                logger.info("Getting response successfully for diagnosticActivationsGet by id "+respose_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for diagnosticActivationsGet by id" + err)
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
        """

         route mindconnect/diagnosticActivationsGetbyidmessage/<str:id>
         param id - Unique identifier of diagnostic activation resource. (required)

         return Paged diagnostic information messages.

         description This method - diagnosticActivationsIdGetTest internally calls method diagnosticActivationsIdMessagesGet of
                     DiagnosticActivationsClient class. This class is available as dependency in mindconnect-<version-here>-py3-none-any.whl.

         apiEndpoint : GET /api/mindconnect/v3/diagnosticActivations/{id}/messages of mindconnect service.

         apiNote Get a diagnostic messages of specific activation resource.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("mindconnect/diagnosticActivationsGetbyidmessage/<str:id> invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                did = kwargs.get("id", "")
                logger.info("Request param is - Id:" + did)
                request_object = DiagnosticActivationsIdMessagesGetRequest(
                    id=did
                )
                response = client.diagnostic_activations_id_messages_get(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
                logger.info("Getting response successfully for diagnosticActivationsGetbyidmessage " + respose_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for diagnosticActivationsGetbyidmessage " + err)
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
        """

         route mindconnect/diagnosticActivationsputbyid/<str:id>/<str:status>
         param : id ---> Unique identifier of diagnostic activation resource. (required)
         param : status ---> Status of the activation.

         return Updated diagnostic  activation information on successful execution.

         description This method internally calls method diagnostic_activations_id_put of DiagnosticActivationsClient class.
                     This class is available as dependency in mindconnect-<version-here>-py3-none-any.whl.

         apiEndpoint : PUT /api/mindconnect/v3/diagnosticActivations/{id} of mindconnect service.
                      service.
         apiNote Update status of Diagnostic Activation.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("mindconnect/diagnosticActivationsputbyid/<str:id>/<str:status> invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                id = kwargs.get("id", "")
                status = kwargs.get("status", "")
                logger.info("Request params are- Id:" + id + " status: " + status)
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
                logger.info("Getting response successfully for diagnosticActivationsputbyid " + respose_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for diagnosticActivationsputbyid " + err)
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
        logger.info("mindconnect/diagnosticinfoget invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                requestObject = DiagnosticInformationGetRequest()
                response = client.diagnostic_information_get(requestObject)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
                logger.info("Getting response successfully for diagnosticinfoget " + respose_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for diagnosticinfoget " + err)
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
        """

         route mindconnect/datapointMappingGet

         return Data point mapping data.

         description This method internally calls method data_point_mappings_get of MappingsClient class.
                     This class is available as dependency in mindconnect-<version-here>-py3-none-any.whl.

         apiEndpoint : GET /api/mindconnect/v3/dataPointMappings of mindconnect service.
                      service.
         apiNote Get mappings.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("mindconnect/datapointMappingGet invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                request_object = DataPointMappingsGetRequest()
                response = client.data_point_mappings_get(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
                logger.info("Getting response successfully for datapointMappingGet " + respose_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for datapointMappingGet " + err)
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
        """

         route mindconnect/datapointMappingGet/<str:id>
         param id - Unique identifier of the mapping resource.

         return Data point mapping data for Id in String format.

         description This method - dataPointMappingsIdGetTest internally calls method dataPointMappingsIdGet of MappingsClient
                     class.
                     This class is available as dependency in mindconnect-<version-here>-py3-none-any.whl.

         apiEndpoint : GET /api/mindconnect/v3/dataPointMappings/{id} of mindconnect service.
                       service.
         apiNote Get a mapping by id.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("mindconnect/datapointMappingGet/<str:id> invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                id = kwargs.get("id", "")
                logger.info("Request param is- Id:"+id)
                request_object = DataPointMappingsIdGetRequest(
                    id=id
                )
                response = client.data_point_mappings_id_get(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
                logger.info("Getting response successfully for datapointMappingGet by id " + respose_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for datapointMappingGet by id" + err)
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
        """

         route mindconnect/datapointMappingCreate

         return Created data point mapping.

         description This method internally calls method data_point_mappings_post of MappingsClient class.
                        This class is available as dependency in mindconnect-<version-here>-py3-none-any.whl.

         apiEndpoint : POST /api/mindconnect/v3/dataPointMappings of mindconnect service.

         apiNote Create single mapping.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("mindconnect/datapointMappingCreate invoked.")
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
                logger.info("Getting response successfully for datapointMappingCreate " + respose_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for datapointMappingCreate " + err)
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
        """

         route mindconnect/datapointMappingdelete/<str:id>
         param id - Unique identifier of the mapping resource.

         return "Deleted successfully" on successful execution.

         description This method internally calls method data_point_mappings_id_delete of MappingsClient class.
                     This class is available as dependency in mindconnect-<version-here>-py3-none-any.whl.

         apiEndpoint : DELETE /api/mindconnect/v3/dataPointMappings/{id} of mindconnect service.
                       service.
         apiNote Delete a mapping.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("mindconnect/datapointMappingdelete/<str:id> invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                id = kwargs.get("id", "")
                logger.info("Request param i s- Id:"+id)
                request_object = DataPointMappingsIdDeleteRequest(
                    id=id
                )
                client.data_point_mappings_id_delete(request_object)
                logger.info("datapointmapping deleted successfully.")
            except exceptions.MindsphereError as err:
                logger.error("getting error while deleting datapointmapping "+err)
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
        """

         route mindconnect/recoverableRecordIDPost/<str:id>
         param id - Unique identifier of the recoverable record.

         return "created successfully" on successful execution.

         description This method internally calls method recoverable_records_id_replay_post of RecordRecoveryClient class.
                        This class is available as dependency in mindconnect-<version-here>-py3-none-any.whl.

         apiEndpoint : POST /api/mindconnect/v3/recoverableRecords/{id}/replay of mindconnect service.
                       service.
         apiNote Re-play a recoverable record.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("mindconnect/recoverableRecordIDPost/<str:id> invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                id = kwargs.get("id", "")
                logger.info("Request param i s- Id:" + id)
                request_object = RecoverableRecordsIdReplayPostRequest(
                    id=id
                )
                client.recoverable_records_id_replay_post(request_object)
                logger.info("recoverable record created successfully")
            except exceptions.MindsphereError as err:
                logger.error("getting error while creating recoverable record "+err)
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
        """

                 route mindconnect/recoverableRecordGet

                 return Recoverable record data on successful execution.

                 description This method internally calls method recoverable_records_get of RecordRecoveryClient class.
                                This class is available as dependency in mindconnect-<version-here>-py3-none-any.whl.

                 apiEndpoint : GET /api/mindconnect/v3/recoverableRecords of mindconnect service.

                 apiNote Get all recoverable records.
                 throws MindsphereError if an error occurs while attempting to invoke the sdk call.

                """
        logger.info("mindconnect/recoverableRecordGet invoked.")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                request_object = RecoverableRecordsGetRequest()
                response = client.recoverable_records_get(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
                logger.info("Getting response successfully for recoverableRecordGet "+respose_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for recoverableRecordGet "+err)
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
        """

         route mindconnect/recoverableRecordIdDownloadLinkGet/<str:id>
         param id - Unique identifier of the recoverable record.

         return Response of download link in String format.

         description This method internally calls method recoverable_records_id_download_link_get of RecordRecoveryClient class.
                     This class is available as dependency in mindconnect-<version-here>-py3-none-any.whl.

         apiEndpoint : GET /api/mindconnect/v3/recoverableRecords/{id}/downloadLink of mindconnect service.
                       service.
         apiNote Get download link of record payload.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("mindconnect/recoverableRecordIdDownloadLinkGet/<str:id> invoked")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                id = kwargs.get("id", "")
                logger.info("Request param is- Id:"+id)
                request_object = RecoverableRecordsIdDownloadLinkGetRequest(
                    id=id
                )
                response = client.recoverable_records_id_download_link_get(request_object)
                respose_json = serialization_filter.sanitize_for_serialization(response)
                respose_json = json.dumps(respose_json)
                logger.info("Getting response successfully for recoverableRecordIdDownloadLinkGet " + respose_json)
            except exceptions.MindsphereError as err:
                logger.error("Getting error for recoverableRecordIdDownloadLinkGet " + err)
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
        """

         route mindconnect/recoverableRecordIdDelete/<str:id>
         param id - Unique identifier of the recoverable record.

         return "Deleted Successfully" upon successful execution.

         description This method internally calls method recoverable_records_id_delete of RecordRecoveryClient class.
                        This class is available as dependency in mindconnect-<version-here>-py3-none-any.whl.

         apiEndpoint : DELETE /api/mindconnect/v3/recoverableRecords/{id} of mindconnect service.

         apiNote Delete a recoverable record.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
        logger.info("mindconnect/recoverableRecordIdDelete/<str:id> invoked.")
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                id = kwargs.get("id", "")
                logger.info("Request param is- Id:" + id)
                request_object = RecoverableRecordsIdDeleteRequest(
                    id=id
                )
                client.recoverable_records_id_delete(request_object)
                logger.info("Recoverable record deleted successfully.")
            except exceptions.MindsphereError as err:
                logger.error("Getting error while deleting Revoverable record "+err)
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
