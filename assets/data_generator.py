from assetmanagement.models import *
import random
import os


def get_random_number():
    return random.randint(1000, 209000)


def generate_file_input():
    file_name = "integ_" + str(get_random_number())
    path = os.path.dirname(os.path.abspath(__file__))
    sample_file = os.path.dirname(path) + r"/README.md"
    return sample_file, file_name


def generate_file_assignment(fileid):
    assignment = KeyedFileAssignment(file_id=fileid)
    return assignment


def generate_location_input():
    location = Location()
    location.country = "Austria"
    location.region = "dd 2"
    location.longitude = 53.5125546
    location.locality = "Innsbruck"
    location.latitude = 9.9763411
    location.postal_code = None
    return location


def generate_asset_input(type_id, parent_id):
    asset_dto = Asset()
    asset_dto.name = "BMW_"+str(get_random_number())
    asset_dto.parent_id = parent_id
    asset_dto.type_id = type_id
    return asset_dto


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
    return asset_type_id, asset_type_input


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
    return aspect_id, aspect_type_input


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
