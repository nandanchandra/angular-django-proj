from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from api.account import views
urlpatterns = [
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/token/', views.MyTokenObtainPairView.as_view(), name='custom_token'),
    path('createuser/', views.CreateUserView.as_view(), name='createuser'),
]