from django.urls import path, include
from tokentype import views

urlpatterns = [
    path('tokenType/toggle', views.TokenTypeView.as_view()),
    path('tenanttype/gettenant', views.TenantTypeView.as_view()),
    path('token/', views.TokenView.as_view()),
    path('logs/', views.LogsView.as_view()),
    path('cls/', views.LogsClearView.as_view()),
    path('', views.IndexView.as_view()),
]