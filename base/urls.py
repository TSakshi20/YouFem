from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register-user/',views.customer_register.as_view(),name="register-user"),
    path('register-prof/',views.prof_register.as_view(),name="register-prof"),
    path('',views.landing,name="landing"),
    path('laws/<str:pk>/',views.laws,name="laws"),
    path('medical/',views.medical,name="medical"),
    path('mental/',views.mental,name="mental"),
    path('legal/',views.legal,name="legal"),
    path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('professional-profile/', views.profile, name="professional-profile"),
]