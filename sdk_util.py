from mindsphere_core import RestClientConfig, exceptions, UserToken, TenantCredentials, AppCredentials
from assetmanagement.clients import AspecttypeClient,AssetsClient,AssettypeClient, LocationsClient,FilesClient
from assetmanagement.clients import StructureClient
from iotfileservices.clients import FileServiceClient
from eventanalytics.clients import EventOperationsClient, PatternOperationsClient
from iottsbulk.clients import BulkImportOperationsClient,ReadOperationsClient
from timeseries.clients import TimeSeriesOperationsClient
from iottsaggregates.clients import  AggregatesClient
from mindconnect.clients import RecordRecoveryClient,DiagnosticActivationsClient,DiagnosticInformationClient,MappingsClient
from app.settings import logger
import os

PROXY_HOST = "194.138.0.25"
PROXY_PORT = "9400"
TOKEN_CIRCULAR_GROUP = ['TENANT', 'USER', 'APP']
TOKEN_SELECTOR = 0


def build_sdk_client(class_name, request):

    if TOKEN_CIRCULAR_GROUP[TOKEN_SELECTOR] == TOKEN_CIRCULAR_GROUP[1]:
        if request.META.get('HTTP_AUTHORIZATION') is None:
            logger.error('To work with technical token,'
                         ' application should receieve authorization header.', request.get_full_path())
            raise exceptions.MindsphereError('To work with technical token,'
                                             ' application should receieve authorization header.',
                                             request.get_full_path())
        else:
            credentials = UserToken(authorization=str(request.META.get('HTTP_AUTHORIZATION'))[7::])
            logger.info('Using User Token for ' + request.get_full_path())
    elif TOKEN_CIRCULAR_GROUP[TOKEN_SELECTOR] == TOKEN_CIRCULAR_GROUP[0]:
        logger.info('Using Technical Token for ' + request.get_full_path())
        if 'MINDSPHERE_CLIENT_ID' in os.environ:
            var_value = os.environ['MINDSPHERE_CLIENT_ID']
            credentials = TenantCredentials(client_id=var_value)
    elif TOKEN_CIRCULAR_GROUP[TOKEN_SELECTOR] == TOKEN_CIRCULAR_GROUP[2]:
        credentials = AppCredentials()
    else:
        logger.error('Unpredicted use case, used token type not available', request.get_full_path())
        raise exceptions.MindsphereError('Unpredicted use case, used token type not available',request.get_full_path())
    if _is_locally_hosted(request):
        config = RestClientConfig()
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
