from django.urls import path, include
from mindconnectapi import views
from django.conf.urls import url

urlpatterns = [
    path("mindconnect/diagnosticActivationsGet", views.DiagnosticActivationsClientViewdiagnostic_activations_get.as_view()),
    path("mindconnect/diagnosticActivationsCreate/<str:agentid>/<str:status>",views.DiagnosticActivationsClientViewdiagnosticactivationscreate.as_view()),
    path("mindconnect/diagnosticActivationsDelete/<str:id>", views.DiagnosticActivationsClientViewImportjobdelete.as_view()),
    path("mindconnect/diagnosticActivationsGet/<str:id>", views.DiagnosticActivationsClientViewdiagnosticactivationsgetbyID.as_view()),
    path("mindconnect/diagnosticActivationsGetbyidmessage/<str:id>", views.DiagnosticActivationsClientViewdiagnosticactivationsgetbyIDMessage.as_view()),
    path("mindconnect/diagnosticActivationsputbyid/<str:id>/<str:status>", views.DiagnosticActivationsClientViewdiagnosticactivationsputbyid.as_view()),
    path("mindconnect/diagnosticinfoget", views.DiagnosticInformationClientViewdiagnosticinfoget.as_view()),
    path("mindconnect/datapointMappingGet", views.MappingsClientViewdatapointMappingGet.as_view()),
    path("mindconnect/datapointMappingGet/<str:id>", views.MappingsClientViewdatapointMappingGetbyId.as_view()),
    path("mindconnect/datapointMappingCreate", views.MappingsClientViewdatapointMappingCreate.as_view()),
    path("mindconnect/datapointMappingdelete/<str:id>", views.MappingsClientViewdatapointMappingDelete.as_view()),
    path("mindconnect/recoverableRecordIDPost/<str:id>", views.RecordRecoveryClientViewidPost.as_view()),
    path("mindconnect/recoverableRecordGet", views.RecordRecoveryClientViewGet.as_view()),
    path("mindconnect/recoverableRecordIdDownloadLinkGet/<str:id>", views.RecordRecoveryClientViewIdDownloadLinkGet.as_view()),
    path("mindconnect/recoverableRecordIdDelete/<str:id>", views.RecordRecoveryClientViewIdDelete.as_view()),

]
