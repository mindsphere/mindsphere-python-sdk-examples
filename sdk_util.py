from mindsphere_core import RestClientConfig, MindsphereCredentials, exceptions
from assetmanagement.clients import AspecttypeClient,AssetsClient,AssettypeClient, LocationsClient,FilesClient
from assetmanagement.clients import StructureClient
from iotfile.clients import FileServiceClient
from eventanalytics.clients import EventOperationsClient, PatternOperationsClient
from app.settings import logger

PROXY_HOST = "194.138.0.25"
PROXY_PORT = "9400"
TECHNICAL_TOKEN = False


def build_sdk_client(class_name, request):

    if TECHNICAL_TOKEN and request.META.get('HTTP_AUTHORIZATION') is not None:
        # To be tested on developer cockpit
        credentials = MindsphereCredentials(authorization=str(request.META.get('HTTP_AUTHORIZATION'))[7::])
        logger.info('Using TECHNICAL Token for '+request.get_full_path())
    elif not TECHNICAL_TOKEN:
        logger.info('Using USER Token for ' + request.get_full_path())
        credentials = MindsphereCredentials()
    else:
        logger.error('To work with technical token,'
              ' application should receieve authorization header.', request.get_full_path())
        raise exceptions.MindsphereError('To work with technical token,'
              ' application should receieve authorization header.',request.get_full_path())
    if _is_locally_hosted(request):
        config = RestClientConfig(PROXY_HOST, PROXY_PORT)
    else:
        config = RestClientConfig()
    class_name = class_name[0:class_name.rindex('View')]
    klass = globals()[class_name]
    instance = klass(config, credentials)
    return instance


def _is_locally_hosted(request):

    if '127.0.0.1:8000' in request.get_host():
        return True
    else:
        return False
