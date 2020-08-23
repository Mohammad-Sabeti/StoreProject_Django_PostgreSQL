from django.urls import path
from Store import views
app_name = 'Store'
urlpatterns = [
    path('product/list/', views.product_list, name='product_list'),

]