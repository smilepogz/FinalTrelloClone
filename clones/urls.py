from django.urls import path
from clones.views import ( RegisterView, LoginView, HomeBoardView,
BoardDetailView, CreateBoardView, CreateBoardList,CreateCardView)

from . import views

urlpatterns = [
    path('', HomeBoardView.as_view(), name="home"),
    path('<str:user>/<str:title>/', BoardDetailView.as_view(), name="dashboard"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('boards/<str:user>/addboard/', CreateBoardView.as_view(), name="addboard"),
    path('boards/<str:user>/card/', CreateCardView.as_view(), name="card"),
    path('boards/<str:user/createboardlist/', CreateBoardList.as_view(), name="cardlist"),
    # path('boards/<str:user>/cardlist/', CardListView.as_view(), name="dashboard"),
    # path('card/', CardDetailView.as_view(), name="dashboard"),
    

]




    # 'boards/<name>/edit/'
    # 'boards/<name>/lists/'
    # 'boards/<name>/lists/id/'
    # 'boards/<name>/lists/id/'
    # 'boards/<name>/lists/id/cards/'   
