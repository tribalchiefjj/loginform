from django.urls import path
from .views import register, login , LoginView, SignUpView, ForgotPasswordView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('api/accounts/login/', LoginView.as_view(), name='login'),
    path('api/accounts/signup/', SignUpView.as_view(), name='signup'),
    path('api/accounts/forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
]