from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('sitemap', sitemap, name = "sitemap"),
    path('', home, name = "home"),
    path('dashboard', dashboard, name = "dashboard"),
    path('payment', payment, name = "payment"),
    path('products_view', products_view, name = "products_view"),
    path('view_product', view_product, name = "view_product"),
    path('profile', profile, name = "profile"),
    path('signin', signin, name = "signin"),
    path('signout', signout, name = "signout"),
    path('profile', profile, name='profile'),
    path('signout', signout, name = "signout"),
    path("register", register, name="register"),
    path("product/<str:pk>", product, name="product"),
    path("delete/<str:pk>", delete, name="delete"),
    path("add_product", add_product, name="add_product"),
    path("<store>", store_category, name="store_category"),
    path("categories/<category>/", product_category, name="product_category"),
    path("update_product/<str:pk>", UpdateProduct.as_view(), name ="update_product" ),
    path("delete_product/<str:pk>", delete_product, name ="delete_product" ),
    
    
    
    
    
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete')

]
