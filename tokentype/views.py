from django.views.decorators.cache import never_cache
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse
from mindsphere_core import RestClientConfig, exceptions
from mindsphere_core import RestClientConfig, exceptions, UserToken, AppCredentials, mindsphere_core, token_service, \
    commonutil
import os
from sdk_util import PROXY_HOST, PROXY_PORT
import sdk_util
from app.settings import logger
import jwt
from django.shortcuts import render


class TokenTypeView(APIView):

    def get(self, request):
        """
        List all assets.
        """
        sdk_util.TOKEN_SELECTOR = (sdk_util.TOKEN_SELECTOR + 1) % len(sdk_util.TOKEN_CIRCULAR_GROUP)
        return HttpResponse(
            'Token type is switched to :' + sdk_util.TOKEN_CIRCULAR_GROUP[sdk_util.TOKEN_SELECTOR] + ' Credentials',
            content_type='application/text', status=status.HTTP_200_OK)


class TenantTypeView(APIView):

    def get(self, request):
        """
        List all assets.
        """
        
        return HttpResponse(os.environ['MDSP_USER_TENANT'], content_type='application/string', status=status.HTTP_200_OK)


class TokenView(APIView):

    def get(self, request):
        """
        List all assets.
        """
        if sdk_util.TOKEN_CIRCULAR_GROUP[sdk_util.TOKEN_SELECTOR] == sdk_util.TOKEN_CIRCULAR_GROUP[0] \
                and request.META.get('HTTP_AUTHORIZATION') is not None:
            token_type = "User Token"
            credentials = UserToken(authorization=request.META.get('HTTP_AUTHORIZATION'))
        elif sdk_util.TOKEN_CIRCULAR_GROUP[sdk_util.TOKEN_SELECTOR] == sdk_util.TOKEN_CIRCULAR_GROUP[1]:
            token_type = "App Creds"
            credentials = AppCredentials()
        else:
            logger.error('To work with technical token,'
                         ' application should receieve authorization header.')
            raise exceptions.MindsphereError('To work with technical token,'
                                             ' application should receieve authorization header.')
        if sdk_util._is_locally_hosted(request):
            config = RestClientConfig(PROXY_HOST, PROXY_PORT)
        else:
            config = RestClientConfig()
        try:
            token = token_service.fetch_token(config, credentials)
            payload = commonutil._decode_jwt(token)
            # payload = jwt.decode(token, "secret", verify=False, algorithms=["RS256"])
        except Exception as e:
            return HttpResponse(token_type + "::" + str(e),
                                content_type='application/json', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return HttpResponse("Decoded " + token_type + "::" + "\n" + str(payload),
                            content_type='application/json', status=status.HTTP_200_OK)


class LogsView(APIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        print(request.user)
        lines_to_display = request.GET.get("lines", "100")
        log_file = os.path.dirname(os.path.abspath(__file__ + "/..")) + r'/log_storage.log'
        with open(log_file, 'rb') as f:
            last_lines = tail(f, int(lines_to_display)).decode('utf-8')
        return HttpResponse(last_lines,
                            content_type='application/json', status=status.HTTP_200_OK)


class LogsClearView(APIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.user.is_superuser:
            log_file = os.path.dirname(os.path.abspath(__file__ + "/..")) + r'/log_storage.log'
            with open(log_file, 'w'):
                pass
            return HttpResponse("Cleared",
                                content_type='application/json', status=status.HTTP_200_OK)
        else:
            return HttpResponse("Only super user can clear the logs.",
                                content_type='application/json', status=status.HTTP_401_UNAUTHORIZED)


class IndexView(APIView):

    @never_cache
    def get(self, request):
        template_name = 'test_urls.html'
        return render(request, template_name)


def tail(f, window):
    """
    Returns the last `window` lines of file `f` as a list of bytes.
    """
    if window == 0:
        return b''
    buf_size = 1024
    f.seek(0, 2)
    end = f.tell()
    nlines = window + 1
    data = []
    while nlines > 0 and end > 0:
        i = max(0, end - buf_size)
        nread = min(end, buf_size)

        f.seek(i)
        chunk = f.read(nread)
        data.append(chunk)
        nlines -= chunk.count(b'\n')
        end -= nread
    return b'\n'.join(b''.join(reversed(data)).splitlines()[-window:])
