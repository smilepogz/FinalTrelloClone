from django.urls import path
from clones.views import ( RegisterView, LoginView, HomeBoardView,
BoardDetailView, CreateBoardView, CreateCardForm, CreateBoardList, CardListView )

from . import views

urlpatterns = [
    path('', HomeBoardView.as_view(), name="home"),
    path('<str:user>/<str:title>/', BoardDetailView.as_view(), name="dashboard"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('addboard/', CreateBoardView.as_view(), name="addboard"),
    path('card/', CreateCardForm.as_view(), name="card" ),
    path('cardlist/', CreateBoardList.as_view(), name="cardlist"),
    path('c/', CardListView.as_view(), name="dashboard"),
]