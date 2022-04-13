from django.urls import path
from .views import ListProducts, ProductCreate

app_name = 'store'

urlpatterns = [
    path('products', ListProducts.as_view()),
    path('products/create', ProductCreate.as_view())
]
