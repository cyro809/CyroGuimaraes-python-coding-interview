from django.urls import path
from .views import ListProducts, ProductCreate, ProductActivation

app_name = 'store'

urlpatterns = [
    path('products', ListProducts.as_view()),
    path('products/create', ProductCreate.as_view()),
    path('products/<int:pk>/<slug:activate>', ProductActivation.as_view())
]
