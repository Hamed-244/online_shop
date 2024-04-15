from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.store, name='store'),
    path('store/category/<str:category_name>/', views.store_category, name='store_category'),
    path('store/product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('place_order/', views.place_order, name='place_order'),
    path('show_order/', views.show_order, name='show_order'),
    path('show_feedback/', views.show_feedback, name='show_feedback'),
    path('login/', views.login, name='login'),
    path('cancel_order/', views.cancel_order, name='cancel_order'),
]