from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterView.as_view(), name='register'),
]
