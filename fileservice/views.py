from rest_framework.views import APIView
import sdk_util
from django.http import HttpResponse
from mindsphere_core import exceptions
from rest_framework import status
from . import data_generator


class FileServiceClientViewCreateFile(APIView):
    def get(self, request, **kwargs):
        """
        creating file
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                entity_id = kwargs.get("entity_id", "")
                file_part, file_name = data_generator.generate_file_input()
                client.put_file(file_part, entity_id, file_name)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                "Successfully uploaded the file and file path :" + file_name,
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
                # search Api call
                response = client.search_files(entity_id=kwargs.get("entity_id", ""))
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                response, content_type="application/json", status=status.HTTP_200_OK
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
                part_num = request.GET.get("part_num", None)
                if part_num is not None:
                    file_data = data_generator.get_resources(part_num)
                else:
                    file_data = None
                client.create_multi_part_file(file_data, entity_id, path, part_num, upload)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

            if upload == "start":
                return HttpResponse(
                    "Initiated file upload for the path : " + path,
                    content_type="application/json", status=status.HTTP_200_OK
                )
            elif upload == "complete":
                return HttpResponse(
                    "Successfully uploaded file for the path : " + path,
                    content_type="application/json", status=status.HTTP_200_OK
                )
            else:
                return HttpResponse(
                    "Uploaded file for the part" + part_num,
                    content_type="application/json", status=status.HTTP_200_OK
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
                response = client.get_file_list(entity_id, path)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                response, content_type="application/json", status=status.HTTP_200_OK
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
                response = client.get_file(entity_id, path)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                response, content_type="application/json", status=status.HTTP_200_OK
            )
