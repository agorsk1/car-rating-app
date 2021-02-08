from rest_framework import permissions, authentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Car rating app",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.IsAuthenticated,),
   authentication_classes=(authentication.SessionAuthentication,)
)
