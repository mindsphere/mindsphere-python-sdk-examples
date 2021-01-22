from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework import status
from django.http import HttpResponse
from mindsphere_core import exceptions

import sdk_util
from . import data_generator
from app.settings import logger


class AspecttypeClientViewCreate(APIView):
    def get(self, request, **kwargs):
        """
        Create aspect type.
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                aspect_id, aspect_type_input = data_generator.generate_aspect_input(
                    tenant=kwargs.get("tenant", "")
                )
                aspect = client.save_aspect_type(aspect_id, aspect_type_input)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                aspect, content_type="application/json", status=status.HTTP_200_OK
            )


class AssettypeClientViewCreate(APIView):

    # url for this : /assettype/mdspsdk/?aspectname=AspectWheel_662&aspectid=mdspsdk.AspectWheel_662
    def get(self, request, **kwargs):
        """
        Create aspect type.
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                aspect_id, asset_type_input = data_generator.generate_asset_type_input(
                    tenant=kwargs.get("tenant", ""),
                    aspect_id=request.GET.get("aspectid", None),
                    aspect_name=request.GET.get("aspectname", None),
                )
                aspect = client.save_asset_type(aspect_id, asset_type_input)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                aspect, content_type="application/json", status=status.HTTP_200_OK
            )


class AssetsClientViewPost(APIView):
    def get(self, request, **kwargs):
        """
        Create asset.
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                root = client.get_root_asset()
                asset_dto = data_generator.generate_asset_input(
                    type_id=kwargs.get("typeid", ""),
                    parent_id=root.asset_id,
                )
                asset = client.add_asset(asset_dto)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                asset, content_type="application/json", status=status.HTTP_200_OK
            )


class AssetsClientViewGetById(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                asset = client.get_asset(id=kwargs.get("id", ""), if_none_match=request.GET.get("ifnonematch", None))
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                asset, content_type="application/json", status=status.HTTP_200_OK
            )


class AssetsClientViewDelete(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                client.delete_asset(id=kwargs.get("id", ""), if_match=request.GET.get("ifmatch", None))
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                'Deleted successfully.', content_type="application/json", status=status.HTTP_200_OK
            )


class AssetsClientViewGetAll(APIView):
    def get(self, request):
        """
        List all assets.
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                asset = client.list_assets(
                    page=0, size=10, sort=None, filter=None, if_none_match=None
                )
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                asset, content_type="application/json", status=status.HTTP_200_OK
            )


class AssetsClientViewUpdateFile(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:

                assignmnet = data_generator.generate_file_assignment(
                    fileid=request.GET.get("fileid", None)
                )
                asset = client.save_asset_file_assignment(
                    id=kwargs.get("id", ""),
                    if_match=request.GET.get("ifmatch", None),
                    key=request.GET.get("key", None),
                    assignment=assignmnet,
                )
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                asset, content_type="application/json", status=status.HTTP_200_OK
            )


class FilesClientViewPost(APIView):
    def get(self, request):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:

                sample_file, file_name = data_generator.generate_file_input()
                resource = client.upload_file(file=sample_file, name=file_name, scope='private')
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                resource, content_type="application/json", status=status.HTTP_200_OK
            )


class LocationsClientViewUpdate(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:

                location = data_generator.generate_location_input()
                client.save_asset_location(if_match=kwargs.get("ifmatch", "0"), id=kwargs.get("id", ""), location=location)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                'Location updated successfully', content_type="application/json", status=status.HTTP_200_OK
            )



