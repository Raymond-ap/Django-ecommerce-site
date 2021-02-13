from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('products', products, name='products'),
    path('detail/<int:pk>', detail, name='detail'),
    path('addtocart/<int:pk>', addtocart, name='addtocart'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('registration', register, name='registration'),
    path('contact', contact, name='contact'),
    path('faq', questions, name='faq'),
    path('account', customer_account, name='account'),
    path('add_wishlist/<int:pk>', addWishList, name='add_wishlist'),
    path('wishlist', viewWishList, name='wishlist'),
    path('logout', logout_user, name='logout'),
    path('remove_cart_item/<int:pk>', removeCartItem, name='remove_cart_item'),
]
