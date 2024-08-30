
from .views import *
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
   openapi.Info(
      title="Employee Management API",
      default_version='v1',
      description="API documentation for the Employee Management app",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@employeemanagement.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('v1/getAllEmployees/', getAllEmployees,name="getAllEmployees"),
    path('v1/createEmployee/', createEmployee,name="createEmployee"),
    path('v1/updateEmployee/<int:pk>', updateEmployee,name="updateEmployee"),
    path('v1/deleteEmployee/<int:pk>', deleteEmployee,name="deleteEmployee"),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('new/register/', register, name='register'),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
