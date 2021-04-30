from rest_framework.views import APIView
import sdk_util
from django.http import HttpResponse
from mindsphere_core import exceptions, serialization_filter
from rest_framework import status
from . import data_generator
import json


class FileServiceClientViewCreateFile(APIView):
    def get(self, request, **kwargs):
        """

         route files/fileservicecreate/<str:entity_id>
         param entityId - An Asset Id for which file needs to be created/stored.
         note Non existent/Incorrect entityId will result in MindsphereError.

         return "Successfully uploaded the file and file path :" <filepath-here> upon successful execution.

         description This method internally calls method put_file of
                       FileServiceClient class. This class is available as dependency
                       in iotfileservices-<version-here>-py3-none-any.whl.
                       The required fields are :
                       1)file string($binary) the file attached content.
                       2)entityId - unique identifier of the asset (entity)
                       3)filepath - url path of the file along with filename.
         apiEndpoint : PUT /api/iotfile/v3/files/{entityId}/{filepath} of iot file
                         service.
         apiNote Create or update a file for the specified asset (entity) and path,
                   with the provided content.
         throws MindsphereError if an error occurs while attempting to invoke the
                 sdk call.


        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entity_id", "")
                request_object = data_generator.generate_put_file_input(entity_id)
                client.put_file(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                "Successfully uploaded the file and file path :" + request_object.filepath,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class FileServiceClientViewUpdateFile(APIView):
    def get(self, request, **kwargs):
        """
         updating file
         route files/fileserviceupdate/<str:entity_id>/<str:path>
         param entityId - An Asset Id for which file needs to be updated.
         note Non existent/Incorrect entityId will result in MindsphereError.

         return "Successfully updated the file and file path :" + <filepath>,

         description This method internally calls method put_file of
                     FileServiceClient class. This class is available as dependency
                    in iotfileservices-<version-here>-py3-none-any.whl.
         apiEndpoint : PUT /api/iotfile/v3/files/{entityId} of iot file service.
                       service.
         apiNote Write a file.
         throws MindsphereError if an error occurs while attempting to invoke the
                                     sdk call.
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entity_id", "")
                path = kwargs.get("path", "")
                if_match = request.GET.get("if_match", "")
                request_object = data_generator.generate_update_file_input(entity_id, path, if_match)
                client.put_file(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                "Successfully updated the file and file path :" + request_object.filepath,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class FileServiceClientViewSearchFile(APIView):

    def get(self, request, **kwargs):
        """
        search file

         route files/fileservicesearch/<str:entity_id>
         param entityId - An Asset Id for which file needs to be searched.
         note Non existent/Incorrect entityId will result in MindsphereError.

         return List of Files.

         description This method internally calls method search_files of
                       FileServiceClient class. This class is available as dependency
                       in iotfileservices-<version-here>-py3-none-any.whl.
         apiEndpoint : GET /api/iotfile/v3/files/{entityId} of iot file service.
                       service.
         apiNote Search files for the specified asset (entity).
         throws MindsphereError if an error occurs while attempting to invoke the
                                     sdk call.
    """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entity_id", "")
                request_object = data_generator.generate_search_files_input(entity_id)
                # search Api call
                response = client.search_files(request_object)
                payload = serialization_filter.sanitize_for_serialization(response)
                payload = json.dumps(payload)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                payload, content_type="application/json", status=status.HTTP_200_OK
            )


class FileServiceClientViewMultiPart(APIView):

    def get(self, request, **kwargs):
        """
        create multi part file

         route files/fileservicecreatemultipartfile/<str:entity_id>/<str:path>
         param entityId - An Asset Id for which file needs to be stored.
         note Non existent/Incorrect entityId will result in MindsphereError.
         param filePath - url path of the file along with filename

         return "Successfully uploaded file for the path: " + <filePath> upon successful execution.

         description This method internally calls methods
                       initiate_multi_part_upload, create_multi_part_file, complete_multi_part_upload
                       of FileServiceClient class. This class is available as
                       dependency in iotfileservices-<version-here>-py3-none-any.whl.
         apiEndpoint : PUT /api/iotfile/v3/files/{entityId}/{filepath} of iot file
                         service.
         apiNote Create or update a file for the specified asset (entity) and path,
                  with the provided content.
         throws MindsphereError if an error occurs while attempting to invoke the
                                     sdk call.
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)

        if request.method == "GET":

            try:
                path = kwargs.get("path", "")
                entity_id = kwargs.get("entity_id", "")
                upload = request.GET.get("upload", None)
                part_num = request.GET.get("partNum", None)
                status_info = ""

                if upload == 'start':
                    request_object = data_generator.get_initiate_multi_part_input(entity_id, path)
                    client.initiate_multi_part_upload(request_object)
                    status_info = "Intitated file upload for the path : " + path
                elif upload == 'complete':
                    request_object = data_generator.get_initiate_multi_part_input(entity_id, path)
                    client.complete_multi_part_upload(request_object)
                    status_info = "Successfully uploaded file for the path : " + path
                else:
                    request_object = data_generator.get_resources(entity_id, path, part_num)
                    client.create_multi_part_file(request_object)
                    status_info = "Uploaded file for the part : " + part_num + " in the path : " + path;
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                status_info,
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class FileServiceClientViewDeleteFile(APIView):
    def get(self, request, **kwargs):
        """
        delete file

        route files/fileservicedelete/<str:entity_id>/<str:path>
        param entityId - An Asset Id for which file needs to be deleted.
        note Non existent/Incorrect entityId will result in MindsphereError.
        param filepath - path of the file along with filename.
        returns "Successfully deleted the file." upon successful execution.
        description This method internally calls method delete_file of
                    FileServiceClient class. This class is available as dependency
                    in iotfileservices-<version-here>-py3-none-any.whl.
        apiEndpoint : DELETE /api/iotfile/v3/files/{entityId}/{filepath} of iot file
                       service.
        apiNote Delete a file for the specified asset (entity) and path.
        throws MindsphereError if an error occurs while attempting to invoke the
                                      sdk call.

        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entity_id", "")
                path = kwargs.get("path", "")
                request_object = data_generator.generate_delete_file_input(entity_id, path)
                client.delete_file(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                "Successfully deleted the file.",
                content_type="application/json",
                status=status.HTTP_200_OK
            )


class FileServiceClientViewListMultiPart(APIView):

    def get(self, request, **kwargs):
        """
        list multi part file

         route files/fileservicelistmultipartfile/<str:entity_id>/<str:path>
         param entityId - An Asset Id for which multipart file needs to be retrieved.
         note Non existent/Incorrect entityId will result in MindsphereError.
         param filePath - path of the file along with filename.

         return List of files

         description This method internally calls method get_file_list of
                     FileServiceClient class. This class is available as dependency
                     in iotfileservices-<version-here>-py3-none-any.whl.

         apiEndpoint : GET /api/iotfile/v3/fileslist/{entityId}/{filepath} of iot file
                         service.
         apiNote list multi part uploads
         throws MindsphereError if an error occurs while attempting to invoke the
                                      sdk call.

        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                path = kwargs.get("path", "")
                entity_id = kwargs.get("entity_id", "")
                response = data_generator.generate_file_list_input(entity_id, path)
                payload = serialization_filter.sanitize_for_serialization(response)
                payload = json.dumps(payload)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                payload, content_type="application/json", status=status.HTTP_200_OK
            )


class FileServiceClientViewGetFile(APIView):

    def get(self, request, **kwargs):
        """
        get file content

         route files/fileservicegetfile/<str:entity_id>/<str:path>
         param entityId - An Asset Id for which file needs to be retrieved.
         note Non existent/Incorrect entityId will result in MindsphereError.
         param filePath - path of the file along with filename.

         return Content of file.

         description This method internally calls method get_file of
                     FileServiceClient class. This class is available as dependency
                     in iotfileservices-<version-here>-py3-none-any.whl.

         apiEndpoint : GET /api/iotfile/v3/files/{entityId}/{filepath} of iot file
                         service.
         apiNote Read a file for the specified asset (entity) and path.
         throws MindsphereError if an error occurs while attempting to invoke the
                                      sdk call.
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entity_id", "")
                path = kwargs.get("path", "")
                request_object = data_generator.generate_file_input(entity_id, path)
                response = client.get_file(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                response, content_type="application/json", status=status.HTTP_200_OK
            )
