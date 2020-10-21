#  clasificados URL Configuration

# Django
from django.contrib import admin
from django.urls import path

# Local views
from items import views as Item
from users import views as Users

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # App
    path('', Users.login_view, name='home'),
    path('items/', Item.view_item, name='items'),
    path('login/', Users.login_view, name="login"),
    path('register/', Users.register_view, name='register'),
    path('logout/', Users.logout_view, name='logout'),

    # App - seller
    path('seller/', Item.view_seller, name='seller'),
    path('seller/my-items/', Item.view_my_items, name='seller_my_items'),
    path('seller/update/<str:id>', Item.view_edit, name="seller_edit"),
    path('seller/delete/<str:id>', Item.delete, name='seller_delete')
]
