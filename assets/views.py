from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework import status
from django.http import HttpResponse
from mindsphere_core import exceptions, serialization_filter
import sdk_util
from . import data_generator
from app.settings import logger
import json

class AspecttypeClientViewCreate(APIView):
    def get(self, request, **kwargs):
        """
        Create aspect type.
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                request_object = data_generator.generate_aspect_input(
                    tenant=request.GET.get("tenantName", None)
                )
                aspect = client.save_aspect_type(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(aspect.to_dict()) , content_type="application/json", status=status.HTTP_200_OK
            )


class AspecttypeClientViewEqualTo(APIView):
    def get(self, request, **kwargs):
        """
        List aspect type using filter equals to
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.get_aspect_types_equals_to(field_type=data_generator.FieldTypeEnum.NAME,
                                                             filter_value=request.GET.get("filterValue", None))
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )


class AspecttypeClientViewLike(APIView):
    def get(self, request, **kwargs):
        """
        List aspect type using filter like
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.get_aspect_types_like(data_generator.FieldTypeEnum.NAME, request.GET.getlist("filterValue", None))
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict()), content_type="application/json", status=status.HTTP_200_OK
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
                request_object = data_generator.generate_asset_type_input(
                    tenant=kwargs.get("tenant", ""),
                    aspect_id=request.GET.get("aspectid", None),
                    aspect_name=request.GET.get("aspectname", None),
                )
                aspect = client.save_asset_type(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(aspect.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )


class AssettypeClientViewEndsWith(APIView):
    def get(self, request, **kwargs):
        """
        Filter asset types using ends with
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.get_asset_types_ends_with(field_type=data_generator.FieldTypeEnum.NAME,
                                                             filter_value=request.GET.get("filterValue", None))
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )


class AssettypeClientViewContains(APIView):
    def get(self, request, **kwargs):
        """
        filter asset types which contains
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.get_asset_types_contains(field_type=data_generator.FieldTypeEnum.NAME,
                                                        filter_value=request.GET.get("filterValue", None))
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )


class AssetsClientViewPost(APIView):
    def get(self, request, **kwargs):
        """
        Create asset.
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                root = client.get_root_asset(data_generator.generate_root_asset_input())
                request_object = data_generator.generate_asset_input(
                    type_id=kwargs.get("typeid", ""),
                    parent_id=request.GET.get("parentid", None),
                )
                asset = client.add_asset(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(asset.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )


class AssetsClientViewStartWith(APIView):
    def get(self, request, **kwargs):
        """
        filtering asset which start with given filter value
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.get_assets_starts_with(field_type=data_generator.FieldTypeEnum.NAME,
                                                               filter_value=request.GET.get("filterValue", None))
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )


class AssetsClientViewOfAspectType(APIView):
    def get(self, request, **kwargs):
        """
        filtering asset which start with given filter value
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                response = client.get_assets_of_type(request.GET.get("filterValue", None))
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(response.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )


class AssetsClientViewGetById(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                request_object = data_generator.generate_get_asset_input(id=kwargs.get("id", ""),
                                                                         if_none_match=request.GET.get("ifnonematch", None))
                asset = client.get_asset(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(asset.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )


class AssetsClientViewDelete(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                request_object = data_generator.generate_delete_asset_input(id=kwargs.get("id", ""),
                                                                            if_match=kwargs.get("ifmatch", ""))
                client.delete_asset(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                'Deleted successfully.', content_type="application/json", status=status.HTTP_200_OK
            )


class AssetsClientViewDeleteWithConfirmation(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                request_object = data_generator.generate_delete_asset_with_confirmation_input(id=kwargs.get("id", ""),
                                                                                              if_match=
                                                                                              kwargs.get
                                                                                              ("ifmatch", ""))
                client.delete_asset_with_confirmation(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                'Asset deleted successfully.', content_type="application/json", status=status.HTTP_200_OK
            )


class AssetsClientViewGetAll(APIView):
    def get(self, request):
        """
        List all assets.
        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                request_object = data_generator.generate_list_assets_input()
                asset = client.list_assets(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(asset.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )


class AssetsClientViewUpdateFile(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                assignment = data_generator.generate_file_assignment(
                    fileid=request.GET.get("fileid", None)
                )
                request_object = data_generator.generate_save_asset_file_assignment_input(kwargs.get("id", ""),
                                                                                          request.GET.get("ifmatch", None),
                                                                                          request.GET.get("key", None),
                                                                                          assignment)
                asset = client.save_asset_file_assignment(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(asset.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )


class FilesClientViewPost(APIView):
    def get(self, request):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                sample_file, file_name = data_generator.generate_file_input()
                request_object = data_generator.generate_upload_file_input(sample_file, 'private', file_name)
                resource = client.upload_file(request_object)
                payload = serialization_filter.sanitize_for_serialization(resource)
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


class LocationsClientViewUpdate(APIView):
    def get(self, request, **kwargs):
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                request_object = data_generator.generate_location_update_input(if_match=kwargs.get("ifmatch", ""),
                                                                               id=kwargs.get("id", ""))
                client.save_asset_location(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                'Location updated successfully', content_type="application/json", status=status.HTTP_200_OK
            )



