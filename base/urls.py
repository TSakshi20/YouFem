from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name="home"),
    #path('',views.index,name="index"),

    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register-prof/',views.registerProf,name="register-prof"),
    path('register-user/',views.registerUser,name="register-user"),
    path('',views.landing,name="landing"),
    path('laws/<str:pk>/',views.laws,name="laws"),
    path('medical/',views.medical,name="medical"),
    path('mental/',views.mental,name="mental"),
    path('legal/',views.legal,name="legal"),
    path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	#path('prod_des/', views.productDes, name="prod_des"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]