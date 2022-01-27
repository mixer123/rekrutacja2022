from django.urls import path
#
from . import views
from .views import SignUpView, success


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('success/', views.success, name="success"),
]