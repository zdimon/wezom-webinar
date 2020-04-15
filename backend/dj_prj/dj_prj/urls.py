
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

from account.views import LoginView

urlpatterns = [
    path('',include(router.urls)),
    path('user/login',LoginView.as_view(),name="user-login"),
    path('admin/', admin.site.urls),
]
