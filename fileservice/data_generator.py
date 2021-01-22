import random
import os


def get_random_number():
    return random.randint(1000, 209000)


def generate_file_input():
    file_name = "integ_" + str(get_random_number())
    sample_file = os.path.dirname(os.path.abspath(__file__ + "/..")) + r'/README.md'
    with open(sample_file , 'r', errors='ignore') as f:
        file_part = f.read().splitlines()
    return file_part, file_name


def get_resources(part_num):
    with open(os.path.dirname(os.path.abspath(__file__ + "/..")) + os.path.join(
            "/fileservice") + os.path.join("/resources") + r"/filepart"+part_num+".txt", 'r', errors='ignore') as f:
        file_part = f.read().splitlines()
    return file_part
