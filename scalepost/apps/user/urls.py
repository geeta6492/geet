from django.urls import include, path
from .views import SignUpView
from . import views
from .views import LoginFormView


urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('social-auth/', include('social_django.urls', namespace='social'))
   # path('accounts/', include('django.contrib.auth.urls')),
]