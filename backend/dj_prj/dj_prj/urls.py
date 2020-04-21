
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

class RootRouter(routers.DefaultRouter):
    def get_api_root_view(self, api_urls=None):
        api_root_dict = {}
        api_root_dict['user-login'] = 'user-login'
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = prefix
        return self.APIRootView.as_view(api_root_dict=api_root_dict)

router = RootRouter()




from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="WEZOM vebinar API",
      default_version='v1',
      description=''' Documentation
      The `ReDoc` view can be found [here](/doc).
      ''',
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="zdimon77@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

from account.views import LoginView



urlpatterns = [
    path('',include(router.urls)),
    path('user/login',LoginView.as_view(),name="user-login"),
    path('admin/', admin.site.urls),














    # swagger
   path(r'swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path(r'doc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
