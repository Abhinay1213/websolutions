from django.contrib import admin
from django.urls import path
from demoapp import views
from django.contrib.auth import views as auth_views  # Import LoginView from auth views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('submit/', views.submit_vendor, name='submit_vendor'),
    path('vendor-products/', views.vendor_products, name='vendor_products'),
    path('product-details/<int:product_id>/', views.product_details, name='product_details'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/logout-success/'), name='logout'),
    path('logout-success/', views.logout_success, name='logout_success'),
    
    #path('logout/', views.logout_view, name='logout'),

]
