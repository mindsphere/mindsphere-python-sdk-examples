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

         route assets/aspects
         param tenantName - Name of the tenant for which you want to create aspect type. Passed in request.
         return Created aspect type information object.
         description This method internally calls method save_aspect_type of AspecttypeClient class.
                        This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl

         apiEndpoint : PUT /api/assetmanagement/v3/aspecttypes/{id} of asset management service.

         apiNote Create or Update an aspect type
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

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

         route filteraspecttypename

         param filter_value - specify the value for field_type(here 'name') to look for while filtering aspect types.(passed
                              in request.)
         return List all aspect types available for tenant with provided filter.
         description This method internally calls method get_aspect_types_equals_to of AspecttypeClient class.
                        This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl

         apiEndpoint : GET /api/assetmanagement/v3/aspecttypes of asset management service.

         apiNote List all aspect types.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

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
        
     
         route filteraspecttypelike
         return List all aspect types available for tenant with provided filter(aspect types whose names are like
                provided filterValue).

         param filterValue - specify the value for fieldType(here `name`) to look for while filtering aspect types.
         description This method internally calls method get_aspect_types_like of AspecttypeClient class.
                     This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl.


         apiEndpoint : GET /api/assetmanagement/v3/aspecttypes of asset management service.

         apiNote List all aspect types.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

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
        Create asset type.


         route assets/assettype/<str:tenant>
         param tenant : Name of tenant for which you wish to create asset type.
         param aspectname : Name of an aspect type which you wish to associate with asset type.
         param  aspectid : Id of an aspect which you wish to associate with asset type.
         note : apsectname ans aspectid passed in request whereas tenant is passed in URL.
         return Created asset type.
         description This method internally calls method save_asset_type of AssettypeClient class.
                        This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl

         apiEndpoint : PUT /api/assetmanagement/v3/assettypes/{id} of asset management service.

         apiNote Create or Update an asset type.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

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
        Filter asset types using ends with.
        

         route filterassettypeendwith
         return List all asset types available for tenant with provided filter(asset types whose name ends with provided
                filterValue).

         param filterValue - specify the value for fieldType(name) to look for while filtering asset types..
         description This method internally calls method get_asset_types_ends_with of AssettypeClient
                     class. This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl.
         apiEndpoint : GET /api/assetmanagement/v3/assettypes of asset management service.

         apiNote List all asset types.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.
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

        route filterassettypecontains
        return List all asset types available for tenant with provided filter(asset types whose name contains provided
               filterValue).

        param filterValue - specify the value for fieldType(name) to look for while filtering asset types..
        description This method internally calls method get_asset_types_contains of AssettypeClient
                     class. This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl.
        apiEndpoint : GET /api/assetmanagement/v3/assettypes of asset management service.

        apiNote List all asset types.
        throws MindsphereError if an error occurs while attempting to invoke the sdk call.
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

         route assets/assets/<str:typeid>
         param typeid - Id of the assettype from which you want to create an
                             Asset. - passed as path variables
         param parentid    - Desired parentId of the asset. - passed in request.
         note Asset creation requires typeid and parentid to be provided in
                request body hence this two values cannot be empty. Values of this
                variables are passed as provided by user hence non existent/Incorrect
                values will result in MindsphereError.

         return Created asset on successful execution.

         description This method internally generates dynamic request
                       body for asset and calls method add_asset
                       AssetsClient.This class is available as part of dependency :
                       assetmanagement-sdk-<version-here>.jar.
                       
         apiEndpoint : POST /api/assetmanagement/v3/assets of assetmanagement service
         throws MindsphereError if an error occurs while attempting to invoke the
               sdk call.

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

         route filterassetsstartwith
         return List all assets available for tenant with provided filter.
         param field_type - specify a fields based on which assets should be filtered. Here field_type is taken as `name`.
         param filter_value - specify the value for field_type to look for while filtering assets.
         description This method internally calls method get_assets_starts_with of AssetsClient class.
                     Assets whose name starts with filter_value will be returned.
                        This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl

         apiEndpoint : GET /api/assetmanagement/v3/assets of asset management service.

         apiNote List all assets available for the authenticated user.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

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
        filtering asset which of given filter_value type.

         route filterassetsoftype
         return List all assets available for tenant with provided filter.

         param filter_value - specify the value  to look for while filtering assets.
         description This method internally calls method get_assets_starts_with of AssetsClient class.
                     Assets which are of provided type (filter_value)  will be returned.
                     This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl

         apiEndpoint : GET /api/assetmanagement/v3/assets of asset management service.

         apiNote List all assets available for the authenticated user.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.
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
        """
        get an asset by id

         route assets/assetsget/<str:id>
         param id : Unique identifier of an asset. (Passed via keyword argument.)
         return Returns an asset for provided Id.
         description This method internally calls method get_asset of AssetsClient class.
                        This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl

         apiEndpoint : GET /api/assetmanagement/v3/assets/{id} of asset management service.

         apiNote Returns an asset.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
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
        """
        delete an asset

         route assets/assetsdelete/<str:id>/<str:ifmatch>
         param id : Unique identifier for an asset.
         param ifmatch : Last known version to facilitate optimistic locking.
         note : both id and ifmatch are passed as keyword arguments.
         return 'Deleted successfully.' on successful execution.
         description This method internally calls method delete_asset of AssetsClient class.
                     This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl

         apiEndpoint : DELETE /api/assetmanagement/v3/assets/{id} of asset management service.

         apiNote Deletes an asset.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
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
        """

         route assetsdeletewithconfirmation/<str:id>/<str:ifmatch>
         param id : Unique identifier for an asset.
         param ifmatch : Last known version to facilitate optimistic locking.
         return  'Asset deleted successfully.' on successful execution.
         description This method internally calls method delete_asset_with_confirmation of AssetsClient class.
                     This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl.
                     Deletes an asset and confirms deletion. It internally checks existence of the
                     asset after we receive a confirmation from server. It retries 3 times for getting the confirmation from
                     server. After deletion only users with admin role can read it, but modification is not possible anymore.
                     Deletion is not possible to delete an asset if it has children.

         apiEndpoint : DELETE /api/assetmanagement/v3/assets/{id} of asset management service.

         apiNote Deletes an asset.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.
        """
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

         route /assets
         return List all assets available for tenant.
         description This method internally calls method list_assets of AssetsClient class.
                        This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl

         apiEndpoint : GET /api/assetmanagement/v3/assets of asset management service.

         apiNote List all assets available for the authenticated user.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

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
        """

         route assets/assetfiles/<str:id>
         return Details of uploaded file upon successful execution.
         param id : Unique identifier for an asset.
         param fileid : Unique identifier of file resource
         param ifmatch : Last known version to facilitate optimistic locking.
         note : id, ifmatch and key are passed via keyword arguments.
         param key : Keyword for the file to be assigned to an asset.
         description This method internally calls method save_asset_file_assignment of AssetsClient class.
                        This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl

         apiEndpoint : PUT /api/assetmanagement/v3/assets/{id}/fileAssignments/{key} of asset management service.
         apiNote Save a file assignment to a given asset.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
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
        """

         route assets/assetfiles
         return Details of uploaded file upon successful execution.

         description This method internally calls method upload_file of FilesClient class.
                     This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl.
                     Sample data required for POST call is generated via generate_file_input method in data_generator module.

         apiEndpoint : POST /api/assetmanagement/v3/files of asset management service.

         apiNote Upload files to be used in Asset Management.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
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
        """

         route assets/assetlocation/<str:id>/<str:ifmatch>
         param assetId : Unique identifier of an asset.

         return 'Location updated successfully' on successful execution.
         description This method internally calls method save_asset_location of LocationsClient class.
                     This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl.
                     If the given asset has own location, this endpoint will update that location.  If the given asset has4
                     no location, this endpoint will create a new location and update the given asset.
                     If the given asset has inherited location, this endpoint will create a new location and update the
                     given asset.

         apiEndpoint : PUT /api/assetmanagement/v3/assets/{id}/location of asset management service.

         apiNote   Create or Update location assigned to given asset.
                   If the given asset has own location, this endpoint will update that location.
                   If the given asset has no location, this endpoint will create a new location and update the given asset.
         throws MindsphereError if an error occurs while attempting to invoke the sdk call.

        """
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


class StructureClientViewAspectsOfAsset(APIView):
    def get(self, request, **kwargs):
        """

         route <str:id>/aspects
         return List of all aspects for provided asset id.
         param id : Unique identifier of an asset. (passed in keyword arguments.)
         description This method internally calls method list_asset_aspects of StructureClient class.
                     This class is available as dependency in assetmanagement-<version-here>-py3-none-any.whl

         apiEndpoint : GET /api/assetmanagement/v3/assets/{id}/aspects of asset management service.

         apiNote Get all static and dynamic aspects of a given asset.
         throws Error if an error occurs while attempting to invoke the sdk call.

        """
        client = sdk_util.build_sdk_client(self.__class__.__name__, request)
        if request.method == "GET":
            try:
                request_object = data_generator.generate_aspects_of_asset_request(id=kwargs.get("id", ""))
                aspects_of_asset = client.list_asset_aspects(request_object)
            except exceptions.MindsphereError as err:
                return HttpResponse(
                    err,
                    content_type="application/json",
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            return HttpResponse(
                json.dumps(aspects_of_asset.to_dict()), content_type="application/json", status=status.HTTP_200_OK
            )
