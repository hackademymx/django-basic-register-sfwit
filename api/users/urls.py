from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(),),
]
