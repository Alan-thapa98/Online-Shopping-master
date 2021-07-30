from django.urls import path
from Basic_App import views

app_name='Basic_App'
urlpatterns=[
path('',views.indexlist.as_view(),name="index"),
path('shop/',views.Shoplist.as_view(),name="shop"),
path('checkout/',views.checkout,name="checkout"),
path('product-details/<int:pk>/',views.indexDetailView.as_view(),name="product"),
path('shop-product-details/<int:pk>/',views.indexDetailView.as_view(),name="shop_product"),
path('cart/<int:pk>/',views.CartDetailView.as_view(),name='cart'),
path('carts/<int:pk>/',views.indexCartDetailView.as_view(),name='carttt'),
path('a/',views.indsercelist.as_view(),name='q'),
]
