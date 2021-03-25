from rest_framework.views import APIView
import sdk_util
from django.http import HttpResponse
from mindsphere_core import exceptions,serialization_filter 
from rest_framework import status
from . import data_generator
import json

class FileServiceClientViewCreateFile(APIView):
    def get(self, request, **kwargs):
        """
        creating file
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
