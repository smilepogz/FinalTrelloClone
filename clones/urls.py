from django.urls import path
from clones.views import ( RegisterView, LoginView, HomeBoardView,
BoardDetailView, CreateBoardView )

from . import views

urlpatterns = [
    path('', HomeBoardView.as_view(), name="home"),
    path('<str:user>/<str:title>/', BoardDetailView.as_view(), name="dashboard"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('addboard/', CreateBoardView.as_view(), name="addboard" )
    
]
