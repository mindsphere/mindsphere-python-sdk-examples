from assetmanagement.models import *
from assetmanagement.models.field_type_enum import FieldTypeEnum
from assetmanagement.models.delete_asset_confirmation_request import DeleteAssetConfirmationRequest
import random
import os


def get_random_number():
    return random.randint(1000, 209000)


def generate_file_input():
    file_name = "integ_" + str(get_random_number())
    path = os.path.dirname(os.path.abspath(__file__))
    sample_file = os.path.dirname(path) + r"/README.md"
    return sample_file, file_name


def generate_upload_file_input(sample_file, scope, file_name):
    request_object = UploadFileRequest(sample_file, scope, file_name, file_name)
    return request_object


def generate_file_assignment(fileid):
    assignment = KeyedFileAssignment(file_id=fileid)
    return assignment


def generate_location_update_input(if_match, id):
    location = Location()
    location.country = "Austria"
    location.region = "dd 2"
    location.longitude = 53.5125546
    location.locality = "Innsbruck"
    location.latitude = 9.9763411
    location.postal_code = None
    request_object = SaveAssetLocationRequest(if_match, location, id)
    return request_object


def generate_asset_input(type_id, parent_id):
    asset_dto = Asset()
    asset_dto.name = "BMW_"+str(get_random_number())
    asset_dto.parent_id = parent_id
    asset_dto.type_id = type_id
    request_object = AddAssetRequest(asset=asset_dto)
    return request_object


def generate_root_asset_input():
    request_object = GetRootAssetRequest(if_none_match=0)
    return request_object


def generate_get_asset_input(id, if_none_match):
    request_object = GetAssetRequest(if_none_match, id)
    return request_object


def generate_delete_asset_input(id, if_match):
    request_object = DeleteAssetRequest(if_match, id)
    return request_object


def generate_delete_asset_with_confirmation_input(id, if_match):
    request_object = DeleteAssetConfirmationRequest(if_match, id)
    return request_object


def generate_list_assets_input():
    request_object = ListAssetsRequest(page=0, size=10, sort=None, filter=None, if_none_match=None)
    return request_object


def generate_save_asset_file_assignment_input(id, if_match, key, assignment):
    request_object = SaveAssetFileAssignmentRequest(if_match, assignment, id, key)
    return request_object

# Aspect type data generator:


def generate_asset_type_input(tenant, aspect_id, aspect_name):
    name = "AssetWheel_" + str(get_random_number())
    asset_type_id = tenant + "." + name
    aspect = AssetTypeAspects(name=aspect_name, aspect_type_id=aspect_id)
    asset_type_aspects_list = [aspect]
    def_list = []
    file_assignments = []
    asset_type_input = AssetType(
        name=name,
        description="Basic agent type for the Asset Management Service.",
        parent_type_id="core.basicasset",
        instantiable=None,
        scope="private",
        variables=def_list,
        file_assignments=file_assignments,
        aspects=asset_type_aspects_list,
    )
    request_object = SaveAssetTypeRequest(if_match=None, id=asset_type_id, assettype=asset_type_input)
    return request_object


def generate_aspect_input(tenant):
    name = "AspectWheel_" + str(get_random_number())
    aspect_variable_list = get_aspect_variable_list()
    aspect_type_input = AspectType(
        name=name,
        category="dynamic",
        scope="private",
        description="",
        variables=aspect_variable_list,
    )
    aspect_id = tenant + "." + name
    request_object = SaveAspectTypeRequest(id=aspect_id, aspecttype=aspect_type_input, if_match='0')
    return request_object


def get_aspect_variable_list():
    aspect_variable1 = AspectVariable(
        name="flwheel",
        data_type="DOUBLE",
        unit="C",
        searchable=False,
        length=None,
        default_value=None,
        quality_code=False,
    )
    aspect_variable2 = AspectVariable(
        name="frwheel",
        data_type="DOUBLE",
        unit="C",
        searchable=False,
        length=None,
        default_value=None,
        quality_code=False,
    )
    aspect_variable_list = [aspect_variable1, aspect_variable2]
    return aspect_variable_list


def generate_aspects_of_asset_request(id):
    request_object = ListAssetAspectsRequest(id=id)
    return request_object
