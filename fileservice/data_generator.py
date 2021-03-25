import random
import os
import datetime
from iotfileservices.models import *


def get_random_number():
    return random.randint(1000, 209000)


def generate_put_file_input(entity_id):
    file_path = "integ_" + str(get_random_number())
    sample_file = os.path.dirname(os.path.abspath(__file__ + "/..")) + r'/README.md'
    with open(sample_file, 'r', errors='ignore', encoding="utf-8") as f:
        file_part = f.read().splitlines()
    request_object = PutFileRequest(file=file_part, entity_id=entity_id, filepath=file_path, description="trial",
                                    timestamp=str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')), type="txt")
    return request_object


def generate_update_file_input(entity_id, path, if_match):
    sample_file = os.path.dirname(os.path.abspath(__file__ + "..")) + r'/resources/se.png'
    time_stamp = str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'))
    with open(sample_file, 'rb') as f:
        file_part = f.read()
    request_object = PutFileRequest(file=file_part, entity_id=entity_id, filepath=path, description="trial",
                                    timestamp=time_stamp, type="png", if_match=if_match)
    return request_object


def generate_search_files_input(entity_id):
    request_object = SearchFilesRequest(entity_id=entity_id)
    return request_object


def generate_file_list_input(entity_id, path):
    request_object = GetFileListRequest(filepath=path, entity_id=entity_id)
    return request_object


def generate_file_input(entity_id, path):
    request_object = GetFileRequest(entity_id=entity_id, filepath=path)
    return request_object


def get_initiate_multi_part_input(entity_id, path):
    request_object = PutFileRequest(entity_id=entity_id, filepath=path, description="trial",
                                    timestamp=str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')), type="txt")
    return request_object


def generate_delete_file_input(entity_id, path):
    request_object = DeleteFileRequest(filepath=path, entity_id=entity_id)
    return request_object


def get_resources(entity_id, path, part_num):
    with open(os.path.dirname(os.path.abspath(__file__ + "/..")) + os.path.join(
            "/fileservice") + os.path.join("/resources") + r"/filepart"+str(part_num)+".txt", 'r', errors='ignore') as f:
        file_part = f.read().splitlines()
    request_object = PutFileRequest(file=file_part,part=part_num, entity_id=entity_id, filepath=path, description="trial",
                                    timestamp=str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')), type="txt")
    return request_object
