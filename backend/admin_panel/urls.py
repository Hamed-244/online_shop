from django.urls import path, include
from rest_framework import routers
from admin_panel import views

# define viewsets urls
router = routers.DefaultRouter()
router.register(r'users', views.UsersCrudViewSet)
router.register(r'products', views.ProductCrudViewSet)
router.register(r'categories', views.CategoryCrudViewSet)
router.register(r'product-images', views.ProductImagesCrudViewSet)
router.register(r'shipping-addresses', views.ShippingAddressCrudViewSet)
router.register(r'orders', views.OrderCrudViewSet)
router.register(r'order-items', views.OrderItemCrudViewSet)
router.register(r'payments', views.PaymentCrudViewSet)
router.register(r'feedbacks', views.FeedbackCrudViewSet)
router.register(r'notices', views.NoticeCrudViewSet)

urlpatterns = [
    path('dashboard-info', views.DashboardInfoApi.as_view())
]

# add viewsets urls to urlpatterns
urlpatterns += router.urls