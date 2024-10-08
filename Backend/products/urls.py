from django.urls import path

from . import views
urlpatterns = [
    path('',views.product_list_create_view, name="product-list"),
    path('<int:pk>/delete',views.ProductDestroyAPIView.as_view()),
    path('<int:pk>/update',views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/',views.ProductDetailAPIView.as_view(), name="product-detail"),
]
