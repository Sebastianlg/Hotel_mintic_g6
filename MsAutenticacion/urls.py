
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from autenticacionApp.views import registroView, VerifyTokenView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', VerifyTokenView.as_view()),
    path('users/', registroView.as_view())
]