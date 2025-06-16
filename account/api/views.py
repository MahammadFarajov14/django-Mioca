from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.utils import swagger_auto_schema
from account.api.serializers import UserApiDocProfileSeriaizer, UserRefreshAPISeriaizer

class UserTokenObtainPairView(TokenObtainPairView):

    @swagger_auto_schema(responses={200: UserApiDocProfileSeriaizer(many=True)})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class UserTokenRefreshView(TokenRefreshView):

    @swagger_auto_schema(responses={200: UserRefreshAPISeriaizer(many=True)})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)