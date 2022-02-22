from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name="first"),
    path('register', views.register, name="register"),
    path('log', views.log, name="log"),
    path('login', views.login, name="login"),
    path('adminpage', views.adminpage, name="adminpage"),
    path('adminside', views.adminside, name="adminside"),
    path('SearchEvent', views.SearchEvent, name="SearchEvent"),
    path('Fourth/<id>', views.Fourth, name="Fourth"),
    path('logout_view', views.logout_view, name="logout_view"),
    path('booking/<id>', views.booking, name="booking"),
    path('first', views.first, name="first"),
    path('second', views.second, name="second"),
    path('paymentop', views.paymentop, name="paymentop"),
    path('pp', views.pp, name="pp"),
    path('ss', views.ss, name="ss"),
    path('bookhistory', views.bookhistory, name="bookhistory"),
    path('Forgotpass', views.Forgotpass, name="Forgotpass"),
    path('change', views.change, name="change"),
    path('changepass', views.changepass, name="changepass"),
    path('ME', views.ME, name="ME"),
    path('Registered_user', views.Registered_user, name="Registered_user"),
    path('bookhistoryad', views.bookhistoryad, name="bookhistoryad"),
    path('bookhistoryEV', views.bookhistoryEV, name="bookhistoryEV"),
    path('deleteing', views.deleteing, name="deleteing"),
    path('main', views.main, name="main"),

]
